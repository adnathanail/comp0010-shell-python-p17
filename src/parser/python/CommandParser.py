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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\3\3\3\7\3\32")
        buf.write("\n\3\f\3\16\3\35\13\3\7\3\37\n\3\f\3\16\3\"\13\3\3\3\3")
        buf.write("\3\7\3&\n\3\f\3\16\3)\13\3\3\3\7\3,\n\3\f\3\16\3/\13\3")
        buf.write("\3\3\7\3\62\n\3\f\3\16\3\65\13\3\3\4\3\4\5\49\n\4\3\5")
        buf.write("\3\5\6\5=\n\5\r\5\16\5>\3\6\3\6\7\6C\n\6\f\6\16\6F\13")
        buf.write("\6\3\6\3\6\3\6\7\6K\n\6\f\6\16\6N\13\6\3\6\5\6Q\n\6\3")
        buf.write("\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\6\7\2Z\2\16\3\2\2")
        buf.write("\2\4\24\3\2\2\2\68\3\2\2\2\b<\3\2\2\2\nP\3\2\2\2\fR\3")
        buf.write("\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\23")
        buf.write("\7\b\2\2\22\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25 \3\2\2\2\26\24\3\2\2\2\27\33\5\n\6\2\30")
        buf.write("\32\7\b\2\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\36\27\3\2\2")
        buf.write("\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2")
        buf.write("\2\2#-\5\b\5\2$&\7\b\2\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2")
        buf.write("\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2*,\5\6\4\2+\'\3\2\2")
        buf.write("\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\63\3\2\2\2/-\3\2\2\2")
        buf.write("\60\62\7\b\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\5\3\2\2\2\65\63\3\2\2\2\669\5\n\6")
        buf.write("\2\679\5\b\5\28\66\3\2\2\28\67\3\2\2\29\7\3\2\2\2:=\5")
        buf.write("\f\7\2;=\7\5\2\2<:\3\2\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2")
        buf.write("\2>?\3\2\2\2?\t\3\2\2\2@D\7\3\2\2AC\7\b\2\2BA\3\2\2\2")
        buf.write("CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GQ\5")
        buf.write("\b\5\2HL\7\4\2\2IK\7\b\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2")
        buf.write("\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2OQ\5\b\5\2P@\3\2\2\2P")
        buf.write("H\3\2\2\2Q\13\3\2\2\2RS\t\2\2\2S\r\3\2\2\2\16\24\33 \'")
        buf.write("-\638<>DLP")
        return buf.getvalue()


class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "UNQUOTED_CONTENT", 
                      "SINGLE_QUOTED", "BACKQUOTED", "WHITESPACE" ]

    RULE_command = 0
    RULE_call = 1
    RULE_atom = 2
    RULE_argument = 3
    RULE_redirection = 4
    RULE_quoted = 5

    ruleNames =  [ "command", "call", "atom", "argument", "redirection", 
                   "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    UNQUOTED_CONTENT=3
    SINGLE_QUOTED=4
    BACKQUOTED=5
    WHITESPACE=6

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.call()
            self.state = 13
            self.match(CommandParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 15
                self.match(CommandParser.WHITESPACE)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.T__0 or _la==CommandParser.T__1:
                self.state = 21
                self.redirection()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 22
                    self.match(CommandParser.WHITESPACE)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.argument()
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CommandParser.WHITESPACE:
                        self.state = 34
                        self.match(CommandParser.WHITESPACE)
                        self.state = 39
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 40
                    self.atom() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 46
                self.match(CommandParser.WHITESPACE)
                self.state = 51
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
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.T__0, CommandParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.redirection()
                pass
            elif token in [CommandParser.UNQUOTED_CONTENT, CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
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
        self.enterRule(localctx, 6, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 58
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                        self.state = 56
                        self.quoted()
                        pass
                    elif token in [CommandParser.UNQUOTED_CONTENT]:
                        self.state = 57
                        self.match(CommandParser.UNQUOTED_CONTENT)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 60 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(CommandParser.T__0)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 63
                    self.match(CommandParser.WHITESPACE)
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                self.argument()
                pass
            elif token in [CommandParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(CommandParser.T__1)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CommandParser.WHITESPACE:
                    self.state = 71
                    self.match(CommandParser.WHITESPACE)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 77
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
        self.enterRule(localctx, 10, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
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





