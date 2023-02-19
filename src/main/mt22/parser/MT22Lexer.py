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
<<<<<<< HEAD
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\30\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\r\n\2")
        buf.write("\r\2\16\2\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\2\2\6\3\3")
        buf.write("\5\4\7\5\t\6\3\2\3\5\2\13\f\17\17\"\"\2\30\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\f\3\2\2\2\5\22")
        buf.write("\3\2\2\2\7\24\3\2\2\2\t\26\3\2\2\2\13\r\t\2\2\2\f\13\3")
        buf.write("\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\20\3")
        buf.write("\2\2\2\20\21\b\2\2\2\21\4\3\2\2\2\22\23\13\2\2\2\23\6")
        buf.write("\3\2\2\2\24\25\13\2\2\2\25\b\3\2\2\2\26\27\13\2\2\2\27")
        buf.write("\n\3\2\2\2\4\2\16\3\b\2\2")
=======
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u018d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\2")
        buf.write("\7\2\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2i\n\2\f\2\16\2l\13\2\3\2\5\2o\n\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3z\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00db\n\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\6\37\u011c\n\37\r\37\16\37\u011d")
        buf.write("\3 \3 \7 \u0122\n \f \16 \u0125\13 \3 \6 \u0128\n \r ")
        buf.write("\16 \u0129\3 \3 \5 \u012e\n \3 \5 \u0131\n \3 \3 \3 \3")
        buf.write(" \3 \7 \u0138\n \f \16 \u013b\13 \5 \u013d\n \3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u0145\n\"\f\"\16\"\u0148\13\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0156\n#\3$\3$\6")
        buf.write("$\u015a\n$\r$\16$\u015b\3%\3%\5%\u0160\n%\3%\6%\u0163")
        buf.write("\n%\r%\16%\u0164\3&\3&\5&\u0169\n&\3&\3&\3&\7&\u016e\n")
        buf.write("&\f&\16&\u0171\13&\3&\5&\u0174\n&\3&\5&\u0177\n&\3&\3")
        buf.write("&\3\'\3\'\3\'\5\'\u017e\n\'\3(\6(\u0181\n(\r(\16(\u0182")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\3+\3+\5]j\u0123\2,\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\2C\"E#G\2I\2K$M\2O%Q&S\'U(\3\2")
        buf.write("\r\3\2c|\4\2\62;c|\3\2\63;\3\2aa\3\2\62;\3\2$$\4\2GGg")
        buf.write("g\3\2}}\3\2\"\"\3\2\177\177\5\2\13\f\17\17\"\"\2\u01b3")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2")
        buf.write("\2S\3\2\2\2\2U\3\2\2\2\3n\3\2\2\2\5y\3\2\2\2\7\u00da\3")
        buf.write("\2\2\2\t\u00dc\3\2\2\2\13\u00de\3\2\2\2\r\u00e0\3\2\2")
        buf.write("\2\17\u00e2\3\2\2\2\21\u00e4\3\2\2\2\23\u00e6\3\2\2\2")
        buf.write("\25\u00e8\3\2\2\2\27\u00ea\3\2\2\2\31\u00ec\3\2\2\2\33")
        buf.write("\u00ee\3\2\2\2\35\u00f0\3\2\2\2\37\u00f2\3\2\2\2!\u00f4")
        buf.write("\3\2\2\2#\u00f6\3\2\2\2%\u00f8\3\2\2\2\'\u00fa\3\2\2\2")
        buf.write(")\u00fc\3\2\2\2+\u00fe\3\2\2\2-\u0101\3\2\2\2/\u0104\3")
        buf.write("\2\2\2\61\u0107\3\2\2\2\63\u010a\3\2\2\2\65\u010c\3\2")
        buf.write("\2\2\67\u010f\3\2\2\29\u0111\3\2\2\2;\u0114\3\2\2\2=\u0119")
        buf.write("\3\2\2\2?\u013c\3\2\2\2A\u013e\3\2\2\2C\u0140\3\2\2\2")
        buf.write("E\u0155\3\2\2\2G\u0157\3\2\2\2I\u015d\3\2\2\2K\u0166\3")
        buf.write("\2\2\2M\u017d\3\2\2\2O\u0180\3\2\2\2Q\u0186\3\2\2\2S\u0189")
        buf.write("\3\2\2\2U\u018b\3\2\2\2WX\7\61\2\2XY\7,\2\2Y]\3\2\2\2")
        buf.write("Z\\\13\2\2\2[Z\3\2\2\2\\_\3\2\2\2]^\3\2\2\2][\3\2\2\2")
        buf.write("^`\3\2\2\2_]\3\2\2\2`a\7,\2\2ab\7\61\2\2bc\3\2\2\2co\b")
        buf.write("\2\2\2de\7\61\2\2ef\7\61\2\2fj\3\2\2\2gi\13\2\2\2hg\3")
        buf.write("\2\2\2il\3\2\2\2jk\3\2\2\2jh\3\2\2\2km\3\2\2\2lj\3\2\2")
        buf.write("\2mo\b\2\3\2nW\3\2\2\2nd\3\2\2\2o\4\3\2\2\2pq\7h\2\2q")
        buf.write("r\7c\2\2rs\7n\2\2st\7u\2\2tz\7g\2\2uv\7v\2\2vw\7t\2\2")
        buf.write("wx\7w\2\2xz\7g\2\2yp\3\2\2\2yu\3\2\2\2z\6\3\2\2\2{|\7")
        buf.write("c\2\2|}\7w\2\2}~\7v\2\2~\u00db\7q\2\2\177\u0080\7k\2\2")
        buf.write("\u0080\u0081\7p\2\2\u0081\u0082\7v\2\2\u0082\u0083\7g")
        buf.write("\2\2\u0083\u0084\7i\2\2\u0084\u0085\7g\2\2\u0085\u00db")
        buf.write("\7t\2\2\u0086\u0087\7x\2\2\u0087\u0088\7q\2\2\u0088\u0089")
        buf.write("\7k\2\2\u0089\u00db\7f\2\2\u008a\u008b\7c\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\u008d\7t\2\2\u008d\u008e\7c\2\2\u008e\u00db")
        buf.write("\7{\2\2\u008f\u0090\7d\2\2\u0090\u0091\7t\2\2\u0091\u0092")
        buf.write("\7g\2\2\u0092\u0093\7c\2\2\u0093\u00db\7m\2\2\u0094\u0095")
        buf.write("\7h\2\2\u0095\u0096\7n\2\2\u0096\u0097\7q\2\2\u0097\u0098")
        buf.write("\7c\2\2\u0098\u00db\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7v\2\2\u009c\u009d\7w\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\u00db\7p\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1")
        buf.write("\7w\2\2\u00a1\u00db\7v\2\2\u00a2\u00a3\7d\2\2\u00a3\u00a4")
        buf.write("\7q\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\u00a8\7c\2\2\u00a8\u00db\7p\2\2\u00a9\u00aa")
        buf.write("\7u\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00db\7i\2\2\u00af\u00b0")
        buf.write("\7h\2\2\u00b0\u00b1\7q\2\2\u00b1\u00db\7t\2\2\u00b2\u00b3")
        buf.write("\7e\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7w\2\2\u00b9\u00db\7g\2\2\u00ba\u00bb\7f\2\2\u00bb\u00db")
        buf.write("\7q\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be\7w\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7q\2\2\u00c3\u00db\7p\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00db\7h\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00db\7g\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00db\7h\2\2\u00cc\u00cd\7y\2\2\u00cd\u00ce")
        buf.write("\7j\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7n\2\2\u00d0\u00db")
        buf.write("\7g\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7j\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db")
        buf.write("\b\4\4\2\u00da{\3\2\2\2\u00da\177\3\2\2\2\u00da\u0086")
        buf.write("\3\2\2\2\u00da\u008a\3\2\2\2\u00da\u008f\3\2\2\2\u00da")
        buf.write("\u0094\3\2\2\2\u00da\u0099\3\2\2\2\u00da\u009f\3\2\2\2")
        buf.write("\u00da\u00a2\3\2\2\2\u00da\u00a9\3\2\2\2\u00da\u00af\3")
        buf.write("\2\2\2\u00da\u00b2\3\2\2\2\u00da\u00ba\3\2\2\2\u00da\u00bc")
        buf.write("\3\2\2\2\u00da\u00c4\3\2\2\2\u00da\u00c6\3\2\2\2\u00da")
        buf.write("\u00ca\3\2\2\2\u00da\u00cc\3\2\2\2\u00da\u00d1\3\2\2\2")
        buf.write("\u00db\b\3\2\2\2\u00dc\u00dd\7*\2\2\u00dd\n\3\2\2\2\u00de")
        buf.write("\u00df\7+\2\2\u00df\f\3\2\2\2\u00e0\u00e1\7.\2\2\u00e1")
        buf.write("\16\3\2\2\2\u00e2\u00e3\7=\2\2\u00e3\20\3\2\2\2\u00e4")
        buf.write("\u00e5\7<\2\2\u00e5\22\3\2\2\2\u00e6\u00e7\7}\2\2\u00e7")
        buf.write("\24\3\2\2\2\u00e8\u00e9\7\177\2\2\u00e9\26\3\2\2\2\u00ea")
        buf.write("\u00eb\7?\2\2\u00eb\30\3\2\2\2\u00ec\u00ed\7]\2\2\u00ed")
        buf.write("\32\3\2\2\2\u00ee\u00ef\7_\2\2\u00ef\34\3\2\2\2\u00f0")
        buf.write("\u00f1\7\60\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7-\2\2\u00f3")
        buf.write(" \3\2\2\2\u00f4\u00f5\7/\2\2\u00f5\"\3\2\2\2\u00f6\u00f7")
        buf.write("\7,\2\2\u00f7$\3\2\2\2\u00f8\u00f9\7\61\2\2\u00f9&\3\2")
        buf.write("\2\2\u00fa\u00fb\7\'\2\2\u00fb(\3\2\2\2\u00fc\u00fd\7")
        buf.write("#\2\2\u00fd*\3\2\2\2\u00fe\u00ff\7(\2\2\u00ff\u0100\7")
        buf.write("(\2\2\u0100,\3\2\2\2\u0101\u0102\7~\2\2\u0102\u0103\7")
        buf.write("~\2\2\u0103.\3\2\2\2\u0104\u0105\7?\2\2\u0105\u0106\7")
        buf.write("?\2\2\u0106\60\3\2\2\2\u0107\u0108\7#\2\2\u0108\u0109")
        buf.write("\7?\2\2\u0109\62\3\2\2\2\u010a\u010b\7>\2\2\u010b\64\3")
        buf.write("\2\2\2\u010c\u010d\7>\2\2\u010d\u010e\7?\2\2\u010e\66")
        buf.write("\3\2\2\2\u010f\u0110\7@\2\2\u01108\3\2\2\2\u0111\u0112")
        buf.write("\7@\2\2\u0112\u0113\7?\2\2\u0113:\3\2\2\2\u0114\u0115")
        buf.write("\7<\2\2\u0115\u0116\7<\2\2\u0116\u0117\3\2\2\2\u0117\u0118")
        buf.write("\b\36\5\2\u0118<\3\2\2\2\u0119\u011b\t\2\2\2\u011a\u011c")
        buf.write("\t\3\2\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e>\3\2\2\2\u011f")
        buf.write("\u0123\t\4\2\2\u0120\u0122\5A!\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\u0125\3\2\2\2\u0123\u0124\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0128\t")
        buf.write("\5\2\2\u0127\u011f\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012d\5A!\2\u012c\u012e\5A!\2\u012d\u012c\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0131\5A!\2\u0130")
        buf.write("\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0133\b \6\2\u0133\u013d\3\2\2\2\u0134\u013d\7")
        buf.write("\62\2\2\u0135\u0139\t\4\2\2\u0136\u0138\5A!\2\u0137\u0136")
        buf.write("\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013c\u0127\3\2\2\2\u013c\u0134\3\2\2\2\u013c\u0135\3")
        buf.write("\2\2\2\u013d@\3\2\2\2\u013e\u013f\t\6\2\2\u013fB\3\2\2")
        buf.write("\2\u0140\u0146\7$\2\2\u0141\u0145\n\7\2\2\u0142\u0143")
        buf.write("\7^\2\2\u0143\u0145\7$\2\2\u0144\u0141\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0149\u014a\7$\2\2\u014a\u014b\b\"\7\2\u014bD\3\2\2\2")
        buf.write("\u014c\u014d\5? \2\u014d\u014e\5G$\2\u014e\u014f\b#\b")
        buf.write("\2\u014f\u0156\3\2\2\2\u0150\u0151\5? \2\u0151\u0152\5")
        buf.write("G$\2\u0152\u0153\5I%\2\u0153\u0154\b#\t\2\u0154\u0156")
        buf.write("\3\2\2\2\u0155\u014c\3\2\2\2\u0155\u0150\3\2\2\2\u0156")
        buf.write("F\3\2\2\2\u0157\u0159\7\60\2\2\u0158\u015a\t\6\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015cH\3\2\2\2\u015d\u015f\t\b\2")
        buf.write("\2\u015e\u0160\7/\2\2\u015f\u015e\3\2\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u0163\t\6\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165J\3\2\2\2\u0166\u016f\t\t\2")
        buf.write("\2\u0167\u0169\t\n\2\2\u0168\u0167\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\5M\'\2\u016b")
        buf.write("\u016c\7.\2\2\u016c\u016e\3\2\2\2\u016d\u0168\3\2\2\2")
        buf.write("\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170\u0176\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174")
        buf.write("\t\n\2\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0177\5M\'\2\u0176\u0173\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\t")
        buf.write("\13\2\2\u0179L\3\2\2\2\u017a\u017e\5? \2\u017b\u017e\5")
        buf.write("C\"\2\u017c\u017e\5E#\2\u017d\u017a\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017eN\3\2\2\2\u017f\u0181")
        buf.write("\t\f\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0185\b(\n\2\u0185P\3\2\2\2\u0186\u0187\13\2\2")
        buf.write("\2\u0187\u0188\b)\13\2\u0188R\3\2\2\2\u0189\u018a\13\2")
        buf.write("\2\2\u018aT\3\2\2\2\u018b\u018c\13\2\2\2\u018cV\3\2\2")
        buf.write("\2\33\2]jny\u00da\u011d\u0123\u0129\u012d\u0130\u0139")
        buf.write("\u013c\u0144\u0146\u0155\u015b\u015f\u0164\u0168\u016f")
        buf.write("\u0173\u0176\u017d\u0182\f\3\2\2\3\2\3\3\4\4\3\36\5\3")
        buf.write(" \6\3\"\7\3#\b\3#\t\b\2\2\3)\n")
>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

<<<<<<< HEAD
    WS = 1
    ERROR_CHAR = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4
=======
    COMMENT = 1
    BOOLEAN = 2
    KEYWORD = 3
    LEFT_PAREN = 4
    RIGHT_PAREN = 5
    COMMA = 6
    SEMICOLON = 7
    COLON = 8
    LEFT_CURBRACK = 9
    RIGHT_CURBRACK = 10
    ASSIG_OP = 11
    LEFT_SQUAREBRACK = 12
    RIGHT_SQUAREBRACK = 13
    DOT = 14
    ADD_OP = 15
    SUB_OP = 16
    MUL_OP = 17
    DIV_OP = 18
    MOD_OP = 19
    LOG_NOT_OP = 20
    LOG_AND_OP = 21
    LOG_OR_OP = 22
    EQUAL_TO_OP = 23
    NOT_EQUAL_TO_OP = 24
    LESS_OP = 25
    EQ_LESS_OP = 26
    GREATER_OP = 27
    GREATER_THAN_OP = 28
    STRING_OP = 29
    IDENTIFIERS = 30
    INT_LIT = 31
    STRINGLIT = 32
    FLOAT_LIT = 33
    ARRAY = 34
    WS = 35
    ERROR_CHAR = 36
    UNCLOSE_STRING = 37
    ILLEGAL_ESCAPE = 38
>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
<<<<<<< HEAD
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]
=======
            "'('", "')'", "','", "';'", "':'", "'{'", "'}'", "'='", "'['", 
            "']'", "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BOOLEAN", "KEYWORD", "LEFT_PAREN", "RIGHT_PAREN", 
            "COMMA", "SEMICOLON", "COLON", "LEFT_CURBRACK", "RIGHT_CURBRACK", 
            "ASSIG_OP", "LEFT_SQUAREBRACK", "RIGHT_SQUAREBRACK", "DOT", 
            "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "LOG_NOT_OP", 
            "LOG_AND_OP", "LOG_OR_OP", "EQUAL_TO_OP", "NOT_EQUAL_TO_OP", 
            "LESS_OP", "EQ_LESS_OP", "GREATER_OP", "GREATER_THAN_OP", "STRING_OP", 
            "IDENTIFIERS", "INT_LIT", "STRINGLIT", "FLOAT_LIT", "ARRAY", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "BOOLEAN", "KEYWORD", "LEFT_PAREN", "RIGHT_PAREN", 
                  "COMMA", "SEMICOLON", "COLON", "LEFT_CURBRACK", "RIGHT_CURBRACK", 
                  "ASSIG_OP", "LEFT_SQUAREBRACK", "RIGHT_SQUAREBRACK", "DOT", 
                  "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "LOG_NOT_OP", 
                  "LOG_AND_OP", "LOG_OR_OP", "EQUAL_TO_OP", "NOT_EQUAL_TO_OP", 
                  "LESS_OP", "EQ_LESS_OP", "GREATER_OP", "GREATER_THAN_OP", 
                  "STRING_OP", "IDENTIFIERS", "INT_LIT", "DIGIT", "STRINGLIT", 
                  "FLOAT_LIT", "DECPART", "EXPPART", "ARRAY", "ELEMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]
>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


<<<<<<< HEAD
=======
    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.COMMENT_action 
            actions[2] = self.KEYWORD_action 
            actions[28] = self.STRING_OP_action 
            actions[30] = self.INT_LIT_action 
            actions[32] = self.STRINGLIT_action 
            actions[33] = self.FLOAT_LIT_action 
            actions[39] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = 'COMMENT'
     

        if actionIndex == 1:
            self.text = 'COMMENT'
     

    def KEYWORD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = 'KEYWORD'
     

    def STRING_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = 'OPERATORS'
     

    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = "".join(self.text.split("_"))
            		
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:-1]
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = "".join(self.text.split("_"))
     

        if actionIndex == 7:
            self.text = "".join(self.text.split("_"))
            											
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise ErrorToken(self.text)
     


>>>>>>> c2b4f5816e0aed3022b279e531c0c423b3053e20
