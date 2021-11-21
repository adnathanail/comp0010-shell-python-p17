grammar Command;

/*
 * Lexer Rules
 */

SINGLE_QUOTED : '\'' (~[\n'])+ '\'' ;

BACKQUOTED : '`' (~[\n`])+ '`' ;

DOUBLE_QUOTED : '"' (BACKQUOTED | (~[\n`"])+)* '"';

UNQUOTED_CONTENT : (~[ \t\n;|<>])+ ;

WHITESPACE          : ' ' | '\t' ;

/*
 * Parser Rules
 */

command : ((call callPipe?) commandSeq?) EOF ;
commandSeq : ';' (call callPipe?) commandSeq? ;
callPipe : '|' call callPipe?;

call : WHITESPACE* (redirection WHITESPACE*)* argument (WHITESPACE* atom)* WHITESPACE* ;
atom : redirection | argument ;
argument : ( quoted | UNQUOTED_CONTENT )+ ;
redirection : ('<' WHITESPACE* argument) | '>' WHITESPACE* argument ;

quoted : SINGLE_QUOTED | DOUBLE_QUOTED | BACKQUOTED   ;