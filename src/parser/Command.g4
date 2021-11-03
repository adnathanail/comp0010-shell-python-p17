grammar Command;

/*
 * Lexer Rules
 */

UNQUOTED_CONTENT : (~[ \t])+ ;

SINGLE_QUOTED : '\'' (~[\n'])+ '\'' ;

BACKQUOTED : '`' (~[\n`])+ '`' ;

// DOUBLE_QUOTED_CONTENT : (~[\n`"])+ ;

WHITESPACE          : (' ' | '\t') ;

/*
 * Parser Rules
 */

command                : call EOF ;

call                : (argument)+ ;

argument : WHITESPACE* (UNQUOTED_CONTENT | quoted) WHITESPACE*;

quoted : SINGLE_QUOTED | BACKQUOTED ;// | double_quoted  ;

// double_quoted : '"""' (BACKQUOTED | DOUBLE_QUOTED_CONTENT)* '"""' ;