import json
import unittest
from json_flattxt import traverse


class TestTraverse(unittest.TestCase):

    def setUp(self):
        with open("sample1.json", "r") as file:
            self.data = json.load(file)

    def test_traverse(self):
        expected_output = []
        traverse(self.data, "", expected_output)
        expected_output = "\n".join(expected_output)

        result = []
        traverse(self.data, "", result)
        result = "\n".join(result)

        with open("result.txt", "w") as file:
            file.write(result)

        self.assertEqual(result, expected_output)

    def test_traverse_single_key_dict(self):
        data = {"key": "value"}

        expected_output = '"key"."value",'

        result = []
        traverse(data, "", result)
        result = "\n".join(result)

        self.assertEqual(result, expected_output)

    def test_traverse_list(self):
        data = ["a", "b", "c"]
        expected_output = ['."a",', '."b",', '."c",']
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))

    def test_traverse_empty_dict(self):
        data = {}
        expected_output = []
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))

    def test_traverse_empty_list(self):
        data = []
        expected_output = []
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))

    def test_traverse_nested_list(self):
        data = ["a", ["b", "c"], "d"]
        expected_output = ['."a",', '."b",', '."c",', '."d",']
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))

    def test_traverse_mixed_data_structure(self):
        data = {"a": ["b", {"c": "value"}, "d"]}
        expected_output = ['"a"."b",', '"a"."c"."value",', '"a"."d",']
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))

    def test_traverse_complex_data_structure(self):
        data = {"a": [{"b": [{"c": "value1"}, {"d": "value2"}]}, {"e": [{"f": "value3"}, {"g": "value4"}]}]}
        expected_output = ['"a"."b"."c"."value1",', '"a"."b"."d"."value2",', '"a"."e"."f"."value3",', '"a"."e"."g"."value4",']
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))

    def test_traverse_multi_nested_dict(self):
        data = {"a": {"b": {"c": {"d": {"e": "value"}}}}}
        expected_output = ['"a"."b"."c"."d"."e"."value",']
        result = []
        traverse(data, "", result)
        self.assertEqual("\n".join(result), "\n".join(expected_output))


if __name__ == '__main__':
    unittest.main()

