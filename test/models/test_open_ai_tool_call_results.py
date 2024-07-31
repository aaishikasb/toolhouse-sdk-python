# This file was generated by liblab | https://liblab.com/
# pylint: disable=C0116, C0115

import unittest
from src.toolhouse.models.OpenAiToolCallResults import OpenAiToolCallResults


class TestOpenAiToolCallResultsModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)  # pylint: disable=W1503

    def test_open_ai_tool_call_results(self):
        # Create OpenAiToolCallResults class instance
        test_model = OpenAiToolCallResults(
            content="veniam", name="officiis", tool_call_id="alias", role="tool"
        )
        self.assertEqual(test_model.content, "veniam")
        self.assertEqual(test_model.name, "officiis")
        self.assertEqual(test_model.tool_call_id, "alias")
        self.assertEqual(test_model.role, "tool")

    def test_open_ai_tool_call_results_required_fields_missing(self):
        # Assert OpenAiToolCallResults class generation fails without required fields
        with self.assertRaises(TypeError):
            # pylint: disable=E1120, W0612
            test_model = OpenAiToolCallResults()  # noqa: F841


if __name__ == "__main__":
    unittest.main()