import importlib.util
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import requests


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "zabbix_data_pull_tool.py"

spec = importlib.util.spec_from_file_location("zabbix_data_pull_tool", SCRIPT)
zabbix_tool = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(zabbix_tool)


class FailingSession:
    verify = False

    def post(self, *args, **kwargs):
        raise requests.exceptions.RetryError(
            "HTTPSConnectionPool(host='zabbix.cit.insea.io', port=443): "
            "Max retries exceeded with url: /api_jsonrpc.php "
            "(Caused by ResponseError('too many 502 error responses'))"
        )


class ZabbixDataPullToolTest(unittest.TestCase):
    def test_api_call_wraps_retry_failure_with_method_context(self):
        with self.assertRaises(zabbix_tool.ZabbixToolError) as raised:
            zabbix_tool._api_call(
                FailingSession(),
                "https://zabbix.cit.insea.io/api_jsonrpc.php",
                "token",
                "hostgroup.get",
                {"output": ["groupid", "name"]},
                100,
                30,
            )

        message = str(raised.exception)
        self.assertIn("hostgroup.get", message)
        self.assertIn("too many 502 error responses", message)
        self.assertIn("increase retry_total", message)

    def test_main_returns_structured_error_for_missing_token(self):
        with patch.dict(os.environ, {"ZABBIX_TOKEN": ""}, clear=False):
            with patch.object(zabbix_tool, "DEFAULT_API_TOKEN", ""):
                result = zabbix_tool.main(api_token="", payload={})

        self.assertFalse(result["ok"])
        self.assertEqual(result["error"], "zabbix_tool_error")
        self.assertIn("Missing api_token", result["error_message"])
        self.assertEqual(result["rows"], [])


if __name__ == "__main__":
    unittest.main()
