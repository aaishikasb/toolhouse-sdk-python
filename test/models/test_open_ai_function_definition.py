# This file was generated by liblab | https://liblab.com/

import unittest
from src.toolhouse.models.OpenAiFunctionDefinition import OpenAiFunctionDefinition


class TestOpenAiFunctionDefinitionModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_open_ai_function_definition(self):
        # Create OpenAiFunctionDefinition class instance
        test_model = OpenAiFunctionDefinition(
            name="deserunt", description="reprehenderit", parameters={"ea": 8}
        )
        self.assertEqual(test_model.name, "deserunt")
        self.assertEqual(test_model.description, "reprehenderit")
        self.assertEqual(test_model.parameters, {"ea": 8})

    def test_open_ai_function_definition_required_fields_missing(self):
        # Assert OpenAiFunctionDefinition class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = OpenAiFunctionDefinition()


if __name__ == "__main__":
    unittest.main()