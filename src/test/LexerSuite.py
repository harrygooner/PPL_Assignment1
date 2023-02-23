import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_string_identifier(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("\"This is a string, containing tab \t\"", "This is a string, containing tab \t,<EOF>", 101))

    def test_lowercase_identifier(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 102))
    def test_float(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("132424_1", "1324241,<EOF>", 103))
    def test_array(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("{\"Kangxi\", \"Yongzheng\", \"Qianlong\"}", "{\"Kangxi\", \"Yongzheng\", \"Qianlong\"},<EOF>", 104))
    def test_comment(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("\"hello \n \"", "hello \n,<EOF>", 105))
    
