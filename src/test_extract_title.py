import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extra_title_from_single_line(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_extra_title_from_multi_line_and_spaces(self):
        result = extract_title(
            """ stuff
                               
                               # Hello
                               
                               some other stuff
                               """
        )
        self.assertEqual(result, "Hello")

    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("hey")


if __name__ == "__main__":
    unittest.main()
