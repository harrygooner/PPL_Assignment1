# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
<<<<<<< HEAD
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
=======
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

<<<<<<< HEAD
    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]
=======
    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "','", "';'", "':'", "'{'", "'}'", "'='", 
                     "'['", "']'", "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BOOLEAN", "KEYWORD", "LEFT_PAREN", 
                      "RIGHT_PAREN", "COMMA", "SEMICOLON", "COLON", "LEFT_CURBRACK", 
                      "RIGHT_CURBRACK", "ASSIG_OP", "LEFT_SQUAREBRACK", 
                      "RIGHT_SQUAREBRACK", "DOT", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "MOD_OP", "LOG_NOT_OP", "LOG_AND_OP", "LOG_OR_OP", 
                      "EQUAL_TO_OP", "NOT_EQUAL_TO_OP", "LESS_OP", "EQ_LESS_OP", 
                      "GREATER_OP", "GREATER_THAN_OP", "STRING_OP", "IDENTIFIERS", 
                      "INT_LIT", "STRINGLIT", "FLOAT_LIT", "ARRAY", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]
>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
<<<<<<< HEAD
    WS=1
    ERROR_CHAR=2
    UNCLOSE_STRING=3
    ILLEGAL_ESCAPE=4
=======
    COMMENT=1
    BOOLEAN=2
    KEYWORD=3
    LEFT_PAREN=4
    RIGHT_PAREN=5
    COMMA=6
    SEMICOLON=7
    COLON=8
    LEFT_CURBRACK=9
    RIGHT_CURBRACK=10
    ASSIG_OP=11
    LEFT_SQUAREBRACK=12
    RIGHT_SQUAREBRACK=13
    DOT=14
    ADD_OP=15
    SUB_OP=16
    MUL_OP=17
    DIV_OP=18
    MOD_OP=19
    LOG_NOT_OP=20
    LOG_AND_OP=21
    LOG_OR_OP=22
    EQUAL_TO_OP=23
    NOT_EQUAL_TO_OP=24
    LESS_OP=25
    EQ_LESS_OP=26
    GREATER_OP=27
    GREATER_THAN_OP=28
    STRING_OP=29
    IDENTIFIERS=30
    INT_LIT=31
    STRINGLIT=32
    FLOAT_LIT=33
    ARRAY=34
    WS=35
    ERROR_CHAR=36
    UNCLOSE_STRING=37
    ILLEGAL_ESCAPE=38
>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





