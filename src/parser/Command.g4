grammar Command;

/*
 * Lexer Rules
 */

UNQUOTED_CONTENT : (~[ \t\n;|<>])+ ;

SINGLE_QUOTED : '\'' (~[\n'])+ '\'' ;

BACKQUOTED : '`' (~[\n`])+ '`' ;

// DOUBLE_QUOTED_CONTENT : (~[\n`"])+ ;

WHITESPACE          : ' ' | '\t' ;

/*
 * Parser Rules
 */

command : ((call callPipe?) commandSeq?) EOF ;
commandSeq : ';' command commandSeq? ;
callPipe : '|' call callPipe?;

call : WHITESPACE* (redirection WHITESPACE*)* argument (WHITESPACE* atom)* WHITESPACE* ;
atom : redirection | argument ;
argument : ( quoted | UNQUOTED_CONTENT )+ ;
redirection : ('<' WHITESPACE* argument) | '>' WHITESPACE* argument ;

quoted : SINGLE_QUOTED | BACKQUOTED ;// | double_quoted  ;

// double_quoted : '"""' (BACKQUOTED | DOUBLE_QUOTED_CONTENT)* '"""' ;