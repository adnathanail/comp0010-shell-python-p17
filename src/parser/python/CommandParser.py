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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\5\2\23\n\2\3\2\3\2\3\3\3\3\3\3\5\3\32\n\3")
        buf.write("\3\4\7\4\35\n\4\f\4\16\4 \13\4\3\4\3\4\7\4$\n\4\f\4\16")
        buf.write("\4\'\13\4\7\4)\n\4\f\4\16\4,\13\4\3\4\3\4\7\4\60\n\4\f")
        buf.write("\4\16\4\63\13\4\3\4\7\4\66\n\4\f\4\16\49\13\4\3\4\7\4")
        buf.write("<\n\4\f\4\16\4?\13\4\3\5\3\5\5\5C\n\5\3\6\3\6\6\6G\n\6")
        buf.write("\r\6\16\6H\3\7\3\7\7\7M\n\7\f\7\16\7P\13\7\3\7\3\7\3\7")
        buf.write("\7\7U\n\7\f\7\16\7X\13\7\3\7\5\7[\n\7\3\b\3\b\3\b\2\2")
        buf.write("\t\2\4\6\b\n\f\16\2\3\3\2\7\b\2e\2\20\3\2\2\2\4\26\3\2")
        buf.write("\2\2\6\36\3\2\2\2\bB\3\2\2\2\nF\3\2\2\2\fZ\3\2\2\2\16")
        buf.write("\\\3\2\2\2\20\22\5\6\4\2\21\23\5\4\3\2\22\21\3\2\2\2\22")
        buf.write("\23\3\2\2\2\23\24\3\2\2\2\24\25\7\2\2\3\25\3\3\2\2\2\26")
        buf.write("\27\7\3\2\2\27\31\5\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\5\3\2\2\2\33\35\7\t\2\2\34\33\3\2\2")
        buf.write("\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37*\3\2\2\2")
        buf.write(" \36\3\2\2\2!%\5\f\7\2\"$\7\t\2\2#\"\3\2\2\2$\'\3\2\2")
        buf.write("\2%#\3\2\2\2%&\3\2\2\2&)\3\2\2\2\'%\3\2\2\2(!\3\2\2\2")
        buf.write("),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-\67")
        buf.write("\5\n\6\2.\60\7\t\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2")
        buf.write("\2\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\66\5\b")
        buf.write("\5\2\65\61\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2")
        buf.write("\28=\3\2\2\29\67\3\2\2\2:<\7\t\2\2;:\3\2\2\2<?\3\2\2\2")
        buf.write("=;\3\2\2\2=>\3\2\2\2>\7\3\2\2\2?=\3\2\2\2@C\5\f\7\2AC")
        buf.write("\5\n\6\2B@\3\2\2\2BA\3\2\2\2C\t\3\2\2\2DG\5\16\b\2EG\7")
        buf.write("\6\2\2FD\3\2\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2")
        buf.write("\2I\13\3\2\2\2JN\7\4\2\2KM\7\t\2\2LK\3\2\2\2MP\3\2\2\2")
        buf.write("NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2Q[\5\n\6\2RV\7")
        buf.write("\5\2\2SU\7\t\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2")
        buf.write("\2WY\3\2\2\2XV\3\2\2\2Y[\5\n\6\2ZJ\3\2\2\2ZR\3\2\2\2[")
        buf.write("\r\3\2\2\2\\]\t\2\2\2]\17\3\2\2\2\20\22\31\36%*\61\67")
        buf.write("=BFHNVZ")
        return buf.getvalue()


class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "UNQUOTED_CONTENT", "SINGLE_QUOTED", "BACKQUOTED", 
                      "WHITESPACE" ]

    RULE_command = 0
    RULE_commandSeq = 1
    RULE_call = 2
    RULE_atom = 3
    RULE_argument = 4
    RULE_redirection = 5
    RULE_quoted = 6

    ruleNames =  [ "command", "commandSeq", "call", "atom", "argument", 
                   "redirection", "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    UNQUOTED_CONTENT=4
    SINGLE_QUOTED=5
    BACKQUOTED=6
    WHITESPACE=7

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

        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def EOF(self):
            return self.getToken(CommandParser.EOF, 0)

        def commandSeq(self):
            return self.getTypedRuleContext(CommandParser.CommandSeqContext,0)


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
            self.state = 14
            self.call()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CommandParser.T__0:
                self.state = 15
                self.commandSeq()


            self.state = 18
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
            self.state = 20
            self.match(CommandParser.T__0)
            self.state = 21
            self.command()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CommandParser.T__0:
                self.state = 22
                self.commandSeq()


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
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 25
                self.match(CommandParser.WHITESPACE)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.T__1 or _la==CommandParser.T__2:
                self.state = 31
                self.redirection()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 32
                    self.match(CommandParser.WHITESPACE)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.argument()
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CommandParser.WHITESPACE:
                        self.state = 44
                        self.match(CommandParser.WHITESPACE)
                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 50
                    self.atom() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 56
                self.match(CommandParser.WHITESPACE)
                self.state = 61
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
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.T__1, CommandParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.redirection()
                pass
            elif token in [CommandParser.UNQUOTED_CONTENT, CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
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
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 68
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                        self.state = 66
                        self.quoted()
                        pass
                    elif token in [CommandParser.UNQUOTED_CONTENT]:
                        self.state = 67
                        self.match(CommandParser.UNQUOTED_CONTENT)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(CommandParser.T__1)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 73
                    self.match(CommandParser.WHITESPACE)
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.argument()
                pass
            elif token in [CommandParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(CommandParser.T__2)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 81
                    self.match(CommandParser.WHITESPACE)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
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
        self.enterRule(localctx, 12, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
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





