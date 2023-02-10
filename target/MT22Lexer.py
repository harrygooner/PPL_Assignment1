# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(" \b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2")
        buf.write("\17\n\2\r\2\16\2\20\3\2\3\2\3\3\3\3\6\3\27\n\3\r\3\16")
        buf.write("\3\30\3\4\3\4\3\5\3\5\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13")
        buf.write("\7\3\2\5\5\2\13\f\17\17\"\"\3\2c|\4\2\62;c|\2!\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\3\16\3\2\2\2\5\24\3\2\2\2\7\32\3\2\2\2\t\34\3\2\2\2\13")
        buf.write("\36\3\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20")
        buf.write("\16\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\23\b\2\2\2")
        buf.write("\23\4\3\2\2\2\24\26\t\3\2\2\25\27\t\4\2\2\26\25\3\2\2")
        buf.write("\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\6\3\2")
        buf.write("\2\2\32\33\13\2\2\2\33\b\3\2\2\2\34\35\13\2\2\2\35\n\3")
        buf.write("\2\2\2\36\37\13\2\2\2\37\f\3\2\2\2\5\2\20\30\3\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    IDENTIFIERS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "IDENTIFIERS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "IDENTIFIERS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


