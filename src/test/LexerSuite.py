import unittest
from TestUtils import TestLexer


# class LexerSuite(unittest.TestCase):

#     def test_lowercase_identifier(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
#     def test_string_identifier(self):
#         """test keywords"""
#         self.assertTrue(TestLexer.test("\"This is a string, containing tab \t\"", "This is a string, containing tab \t,<EOF>", 101))

#     def test_lowercase_identifier(self):
#         """test keywords"""
#         self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 102))
#     def test_float(self):
#         """test keywords"""
#         self.assertTrue(TestLexer.test("1231241_1_123", "12312411123,<EOF>", 103))
#     def test_array(self):
#         """test keywords"""
#         self.assertTrue(TestLexer.test("//a\na", ",<EOF>", 104))
#     def test_comment(self):
#         """test keywords"""
#         self.assertTrue(TestLexer.test("\"hello \n \"", "hello \n,<EOF>", 105))
#     def test_float(self):
#         """test keywords"""
#         self.assertTrue(TestLexer.test(".5E1", ".5E1,<EOF>", 106))
class LexerSuite(unittest.TestCase):
    # Integers
    def test1(self):
        input = """012_3"""
        target = "0,123,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 101))

    def test2(self):
        input = "1231241_1_123"
        target = "12312411123,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 102))

    def test3(self):
        input = "-256_23_45"
        target = "-,2562345,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 103))

    def test4(self):
        input = "123901249_0"
        target = "1239012490,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 104))

    def test5(self):
        input = "-1_234_567"
        target = "-,1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 105))

    def test6(self):
        input = "-0175"
        target = "-,0,175,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 106))

    def test7(self):
        input = "-5680"
        target = "-,5680,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 107))

    def test8(self):
        input = "12345__6789"
        target = "12345,__6789,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 108))

    def test9(self):
        input = "-123456789"
        target = "-,123456789,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 109))

    def test10(self):
        input = "-0_123"
        target = "-,0,_123,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 110))
    # FLOAT
    def test11(self):
        input = ".E-12"
        target = ".E-12,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 111))

    def test12(self):
        input = "12e-12"
        target = "12e-12,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 112))

    def test13(self):
        input = "2.3e+4"
        target = "2.3e+4,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 113))

    def test14(self):
        input = "78E-9"
        target = "78E-9,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 114))

    def test15(self):
        input = "123_123.456e-7"
        target = "123123.456e-7,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 115))

    def test16(self):
        input = "-20_23_1508.001e+100"
        target = "-,20231508.001e+100,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 116))

    def test17(self):
        input = "12_34_56_78.99e00"
        target = "12345678.99e00,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 117))

    def test18(self):
        input = ".1230e12"
        target = ".1230e12,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 118))

    def test19(self):
        input = "_23_1508.001e+100"
        target = "_23_1508,.001e+100,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 119))

    def test20(self):
        input = "_23_1508.00111e"
        target = "_23_1508,.,0,0,111,e,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 120))

    # Boolean
    def test21(self):
        input = "false false"
        target = "false,false,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 121))

    def test22(self):
        input = "true"
        target = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 122))

    def test23(self):
        input = "true false true"
        target = "true,false,true,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 123))

    def test24(self):
        input = "false"
        target = "false,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 124))

    def test25(self):
        input = "false true"
        target = "false,true,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 125))

    def test26(self):
        input = "false true false"
        target = "false,true,false,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 126))

    def test27(self):
        input = "true auto"
        target = "true,auto,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 127))

    def test28(self):
        input = "void"
        target = "void,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 128))
    
    def test29(self):
        input = "true integer false"
        target = "true,integer,false,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 129))

    def test30(self):
        input = "true float string array"
        target = "true,float,string,array,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 130))

    # Comments
    def test31(self):
        input = "// Ok bro"
        target = "<EOF>"
        self.assertTrue(TestLexer.test(input, target, 131))

    def test32(self):
        input = "/* No problem */"
        target = "<EOF>"
        self.assertTrue(TestLexer.test(input, target, 132))

    def test33(self):
        input = "abc // It's variable"
        target = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 133))

    def test34(self):
        input = "PPL /*Ok*/ HCMUT"
        target = "PPL,HCMUT,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 134))

    def test35(self):
        input = "/* Error */ */"
        target = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 135))

    def test36(self):
        input = "// abcxyz //"
        target = "<EOF>"
        self.assertTrue(TestLexer.test(input, target, 136))

    def test37(self):
        input = "//a\na"
        target = "a,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 137))

    def test38(self):
        input = "/*/* Oops */*/"
        target = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 138))

    def test39(self):
        input = "/*/* Greedy? */"
        target = "<EOF>"
        self.assertTrue(TestLexer.test(input, target, 139))

    def test40(self):
        input = "/* //// Qua mon PPL */"
        target = "<EOF>"
        self.assertTrue(TestLexer.test(input, target, 140))

    # Identifiers
    def test41(self):
        input = "_123"
        target = "_123,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 141))

    def test42(self):
        input = "Abc123"
        target = "Abc123,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 142))

    def test43(self):
        input = "_ttt __56_a7"
        target = "_ttt,__56_a7,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 143))

    def test44(self):
        input = "_____a"
        target = "_____a,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 144))

    def test45(self):
        input = "abc"
        target = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 145))

    def test46(self):
        input = "hasagi"
        target = "hasagi,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 146))

    def test47(self):
        input = "_NamHung_"
        target = "_NamHung_,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 147))

    def test48(self):
        input = "Mothai34"
        target = "Mothai34,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 148))

    def test49(self):
        input = "aA_1240"
        target = "aA_1240,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 149))

    def test50(self):
        input = "Monnaykhoqua"
        target = "Monnaykhoqua,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 150))

    # Keywords
    def test51(self):
        input = "auto"
        target = "auto,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 151))

    def test52(self):
        input = "break continue"
        target = "break,continue,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 152))

    def test53(self):
        input = "function"
        target = "function,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 153))

    def test54(self):
        input = "while do"
        target = "while,do,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 154))

    def test55(self):
        input = "string integer float boolean"
        target = "string,integer,float,boolean,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 155))

    def test56(self):
        input = "if else else"
        target = "if,else,else,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 156))

    def test57(self):
        input = "dowhile void arrayfor"
        target = "dowhile,void,arrayfor,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 157))

    def test58(self):
        input = "return float integer inherit out"
        target = "return,float,integer,inherit,out,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 158))

    def test59(self):
        input = "do do do function float"
        target = "do,do,do,function,float,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 159))

    def test60(self):
        input = "if while do while else else"
        target = "if,while,do,while,else,else,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 160))

    #Operators
    def test61(self):
        input = "+ - * /"
        target = "+,-,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 161))

    def test62(self):
        input = "!= == <= >= < >"
        target = "!=,==,<=,>=,<,>,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 162))

    def test63(self):
        input = ":: + - * /"
        target = "::,+,-,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 163))

    def test64(self):
        input = "& && || !"
        target = "Error Token &"
        self.assertTrue(TestLexer.test(input, target, 164))

    def test65(self):
        input = "% / || &&"
        target = "%,/,||,&&,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 165))

    def test66(self):
        input = "**"
        target = "*,*,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 166))

    def test67(self):
        input = "|||"
        target = "||,Error Token |"
        self.assertTrue(TestLexer.test(input, target, 167))

    def test68(self):
        input = "!=!="
        target = "!=,!=,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 168))

    def test69(self):
        input = ">=<===><"
        target = ">=,<=,==,>,<,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 169))

    def test70(self):
        input = ">>><<<"
        target = ">,>,>,<,<,<,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 170))

    # String, sep
    def test71(self):
        input = "()"
        target = "(,),<EOF>"
        self.assertTrue(TestLexer.test(input, target, 171))

    def test72(self):
        input = "[]"
        target = "[,],<EOF>"
        self.assertTrue(TestLexer.test(input, target, 172))

    def test73(self):
        input = "{}"
        target = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, target, 173))

    def test74(self):
        input = ". ,"
        target = ".,,,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 174))

    def test75(self):
        self.assertTrue(TestLexer.test("abc_a", "abc_a,<EOF>", 175))

    def test76(self):
        self.assertTrue(TestLexer.test("123_4_56", "123456,<EOF>", 176))

    def test77(self):
        self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 177))

    def test78(self):
        self.assertTrue(TestLexer.test(
            "\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 178))

    def test79(self):
        self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 179))

    def test80(self):
        self.assertTrue(TestLexer.test(
            "\"This is a string containing tab \t\"", "This is a string containing tab 	,<EOF>", 180))

    def test81(self):
        self.assertTrue(TestLexer.test('inherit', 'inherit,<EOF>', 181))

    def test82(self):
        self.assertTrue(TestLexer.test("0_123", "0,_123,<EOF>", 182))

    def test83(self):
        self.assertTrue(TestLexer.test("\"hello \n hii \"",
                        "Unclosed String: hello ", 183))

    def test84(self):
        self.assertTrue(TestLexer.test(".E12", ".E12,<EOF>", 184))

    def test85(self):
        self.assertTrue(TestLexer.test("?", "Error Token ?", 185))

    def test86(self):
        self.assertTrue(TestLexer.test("{1,2,3}", "{,1,,,2,,,3,},<EOF>", 186))

    def test87(self):
        self.assertTrue(TestLexer.test(
            "\"UncloseStringExample", "Unclosed String: UncloseStringExample", 187))

    def test88(self):
        self.assertTrue(TestLexer.test("123.4_56", "123.4,_56,<EOF>", 188))

    def test89(self):
        self.assertTrue(TestLexer.test("12e+6", "12e+6,<EOF>", 189))

    def test90(self):
        self.assertTrue(TestLexer.test(
            "\" Illegal escape \g\"", "Illegal Escape In String:  Illegal escape \g", 190))

    def test91(self):
        input = "xyz\b"
        target = "xyz,Error Token \b"
        self.assertTrue(TestLexer.test(input, target, 191))

    def test92(self):
        input = "namhung\r"
        target = "namhung,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 192))

    def test93(self):
        input = """\"HCMUT\'BK\""""
        target = "HCMUT'BK,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 193))

    def test94(self):
        input = """\"Welcome to\n the VietNam\i\""""
        target = "Unclosed String: Welcome to"
        self.assertTrue(TestLexer.test(input, target, 194))

    def test95(self):
        input = """\"VietNam\'s Football team\""""
        target = "VietNam's Football team,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 195))

    def test96(self):
        input = """\"Haha\\'Hehe\""""
        target = "Illegal Escape In String: Haha\\'"
        self.assertTrue(TestLexer.test(input, target, 196))

    def test97(self):
        input = """\"With backslash\\\""""
        target = "Unclosed String: With backslash\\"
        self.assertTrue(TestLexer.test(input, target, 197))

    def test98(self):
        input = """\"No\\" idea\""""
        target = """No\\\" idea,<EOF>"""
        self.assertTrue(TestLexer.test(input, target, 198))

    def test99(self):
        input = "\"Helloo Everybody\""
        target = "Helloo Everybody,<EOF>"
        self.assertTrue(TestLexer.test(input, target, 199))

    def test100(self):
        input = "\"Don\'t feel so good"
        target = "Unclosed String: Don't feel so good"
        self.assertTrue(TestLexer.test(input, target, 200))


