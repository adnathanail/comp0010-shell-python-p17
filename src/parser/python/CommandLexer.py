# Generated from Command.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("B\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\6\6 \n\6\r\6\16\6!\3\6\3\6\3\7\3\7\6\7(\n\7")
        buf.write("\r\7\16\7)\3\7\3\7\3\b\3\b\3\b\6\b\61\n\b\r\b\16\b\62")
        buf.write("\7\b\65\n\b\f\b\16\b8\13\b\3\b\3\b\3\t\6\t=\n\t\r\t\16")
        buf.write("\t>\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\3\2\7\4\2\f\f))\4\2\f\fbb\5\2\f\f$$bb\7\2\13\f")
        buf.write("\"\"=>@@~~\4\2\13\13\"\"\2G\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2")
        buf.write("\2\2\7\31\3\2\2\2\t\33\3\2\2\2\13\35\3\2\2\2\r%\3\2\2")
        buf.write("\2\17-\3\2\2\2\21<\3\2\2\2\23@\3\2\2\2\25\26\7=\2\2\26")
        buf.write("\4\3\2\2\2\27\30\7~\2\2\30\6\3\2\2\2\31\32\7>\2\2\32\b")
        buf.write("\3\2\2\2\33\34\7@\2\2\34\n\3\2\2\2\35\37\7)\2\2\36 \n")
        buf.write("\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2")
        buf.write("\"#\3\2\2\2#$\7)\2\2$\f\3\2\2\2%\'\7b\2\2&(\n\3\2\2\'")
        buf.write("&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\7")
        buf.write("b\2\2,\16\3\2\2\2-\66\7$\2\2.\65\5\r\7\2/\61\n\4\2\2\60")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\65\3\2\2\2\64.\3\2\2\2\64\60\3\2\2\2\658\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29:\7$\2")
        buf.write("\2:\20\3\2\2\2;=\n\5\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2")
        buf.write(">?\3\2\2\2?\22\3\2\2\2@A\t\6\2\2A\24\3\2\2\2\t\2!)\62")
        buf.write("\64\66>\2")
        return buf.getvalue()


class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SINGLE_QUOTED = 5
    BACKQUOTED = 6
    DOUBLE_QUOTED = 7
    UNQUOTED_CONTENT = 8
    WHITESPACE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'|'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_QUOTED", "BACKQUOTED", "DOUBLE_QUOTED", "UNQUOTED_CONTENT", 
            "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SINGLE_QUOTED", "BACKQUOTED", 
                  "DOUBLE_QUOTED", "UNQUOTED_CONTENT", "WHITESPACE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


