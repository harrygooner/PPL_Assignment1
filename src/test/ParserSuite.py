import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """a,b,c: string = expr,expr,expr;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main:function void(){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """\"q\"::\"h\""""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """false&&true"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """!(!op&&op)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """foo(a,b)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))    