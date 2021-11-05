# Generated from Command.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\5\2\25\n\2\3\2\5\2\30\n\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\5\3\37\n\3\3\4\3\4\3\4\5\4$\n\4\3\5\7\5\'")
        buf.write("\n\5\f\5\16\5*\13\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5")
        buf.write("\7\5\63\n\5\f\5\16\5\66\13\5\3\5\3\5\7\5:\n\5\f\5\16\5")
        buf.write("=\13\5\3\5\7\5@\n\5\f\5\16\5C\13\5\3\5\7\5F\n\5\f\5\16")
        buf.write("\5I\13\5\3\6\3\6\5\6M\n\6\3\7\3\7\6\7Q\n\7\r\7\16\7R\3")
        buf.write("\b\3\b\7\bW\n\b\f\b\16\bZ\13\b\3\b\3\b\3\b\7\b_\n\b\f")
        buf.write("\b\16\bb\13\b\3\b\5\be\n\b\3\t\3\t\3\t\2\2\n\2\4\6\b\n")
        buf.write("\f\16\20\2\3\3\2\b\t\2p\2\22\3\2\2\2\4\33\3\2\2\2\6 \3")
        buf.write("\2\2\2\b(\3\2\2\2\nL\3\2\2\2\fP\3\2\2\2\16d\3\2\2\2\20")
        buf.write("f\3\2\2\2\22\24\5\b\5\2\23\25\5\6\4\2\24\23\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\27\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2")
        buf.write("\2\33\34\7\3\2\2\34\36\5\2\2\2\35\37\5\4\3\2\36\35\3\2")
        buf.write("\2\2\36\37\3\2\2\2\37\5\3\2\2\2 !\7\4\2\2!#\5\b\5\2\"")
        buf.write("$\5\6\4\2#\"\3\2\2\2#$\3\2\2\2$\7\3\2\2\2%\'\7\n\2\2&")
        buf.write("%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\64\3\2\2\2*")
        buf.write("(\3\2\2\2+/\5\16\b\2,.\7\n\2\2-,\3\2\2\2.\61\3\2\2\2/")
        buf.write("-\3\2\2\2/\60\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\62+\3")
        buf.write("\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\67")
        buf.write("\3\2\2\2\66\64\3\2\2\2\67A\5\f\7\28:\7\n\2\298\3\2\2\2")
        buf.write(":=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>@\5")
        buf.write("\n\6\2?;\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BG\3\2\2")
        buf.write("\2CA\3\2\2\2DF\7\n\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2G")
        buf.write("H\3\2\2\2H\t\3\2\2\2IG\3\2\2\2JM\5\16\b\2KM\5\f\7\2LJ")
        buf.write("\3\2\2\2LK\3\2\2\2M\13\3\2\2\2NQ\5\20\t\2OQ\7\7\2\2PN")
        buf.write("\3\2\2\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\r\3")
        buf.write("\2\2\2TX\7\5\2\2UW\7\n\2\2VU\3\2\2\2WZ\3\2\2\2XV\3\2\2")
        buf.write("\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2[e\5\f\7\2\\`\7\6\2\2")
        buf.write("]_\7\n\2\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3")
        buf.write("\2\2\2b`\3\2\2\2ce\5\f\7\2dT\3\2\2\2d\\\3\2\2\2e\17\3")
        buf.write("\2\2\2fg\t\2\2\2g\21\3\2\2\2\22\24\27\36#(/\64;AGLPRX")
        buf.write("`d")
        return buf.getvalue()


class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'|'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "UNQUOTED_CONTENT", "SINGLE_QUOTED", 
                      "BACKQUOTED", "WHITESPACE" ]

    RULE_command = 0
    RULE_commandSeq = 1
    RULE_callPipe = 2
    RULE_call = 3
    RULE_atom = 4
    RULE_argument = 5
    RULE_redirection = 6
    RULE_quoted = 7

    ruleNames =  [ "command", "commandSeq", "callPipe", "call", "atom", 
                   "argument", "redirection", "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    UNQUOTED_CONTENT=5
    SINGLE_QUOTED=6
    BACKQUOTED=7
    WHITESPACE=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandParser.EOF, 0)

        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def commandSeq(self):
            return self.getTypedRuleContext(CommandParser.CommandSeqContext,0)


        def callPipe(self):
            return self.getTypedRuleContext(CommandParser.CallPipeContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.call()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CommandParser.T__1:
                self.state = 17
                self.callPipe()


            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CommandParser.T__0:
                self.state = 20
                self.commandSeq()


            self.state = 23
            self.match(CommandParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandSeqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(CommandParser.CommandContext,0)


        def commandSeq(self):
            return self.getTypedRuleContext(CommandParser.CommandSeqContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_commandSeq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandSeq" ):
                listener.enterCommandSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandSeq" ):
                listener.exitCommandSeq(self)




    def commandSeq(self):

        localctx = CommandParser.CommandSeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commandSeq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(CommandParser.T__0)
            self.state = 26
            self.command()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CommandParser.T__0:
                self.state = 27
                self.commandSeq()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallPipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def callPipe(self):
            return self.getTypedRuleContext(CommandParser.CallPipeContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_callPipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallPipe" ):
                listener.enterCallPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallPipe" ):
                listener.exitCallPipe(self)




    def callPipe(self):

        localctx = CommandParser.CallPipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_callPipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(CommandParser.T__1)
            self.state = 31
            self.call()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CommandParser.T__1:
                self.state = 32
                self.callPipe()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.WHITESPACE)
            else:
                return self.getToken(CommandParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.AtomContext)
            else:
                return self.getTypedRuleContext(CommandParser.AtomContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = CommandParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 35
                self.match(CommandParser.WHITESPACE)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.T__2 or _la==CommandParser.T__3:
                self.state = 41
                self.redirection()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 42
                    self.match(CommandParser.WHITESPACE)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.argument()
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CommandParser.WHITESPACE:
                        self.state = 54
                        self.match(CommandParser.WHITESPACE)
                        self.state = 59
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 60
                    self.atom() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 66
                self.match(CommandParser.WHITESPACE)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(CommandParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = CommandParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.T__2, CommandParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.redirection()
                pass
            elif token in [CommandParser.UNQUOTED_CONTENT, CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.QuotedContext)
            else:
                return self.getTypedRuleContext(CommandParser.QuotedContext,i)


        def UNQUOTED_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.UNQUOTED_CONTENT)
            else:
                return self.getToken(CommandParser.UNQUOTED_CONTENT, i)

        def getRuleIndex(self):
            return CommandParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CommandParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 78
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                        self.state = 76
                        self.quoted()
                        pass
                    elif token in [CommandParser.UNQUOTED_CONTENT]:
                        self.state = 77
                        self.match(CommandParser.UNQUOTED_CONTENT)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 80 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.WHITESPACE)
            else:
                return self.getToken(CommandParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)




    def redirection(self):

        localctx = CommandParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(CommandParser.T__2)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 83
                    self.match(CommandParser.WHITESPACE)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 89
                self.argument()
                pass
            elif token in [CommandParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(CommandParser.T__3)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 91
                    self.match(CommandParser.WHITESPACE)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED(self):
            return self.getToken(CommandParser.SINGLE_QUOTED, 0)

        def BACKQUOTED(self):
            return self.getToken(CommandParser.BACKQUOTED, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = CommandParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==CommandParser.SINGLE_QUOTED or _la==CommandParser.BACKQUOTED):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





