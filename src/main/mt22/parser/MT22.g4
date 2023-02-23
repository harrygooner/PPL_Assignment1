grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: arr|vardecl|funcdecl|concat_expr|funcall_expr EOF;

//arr lexer
arr: LEFT_CURBRACK arrayList RIGHT_CURBRACK;
arrayList: non_null_arrayList |;
non_null_arrayList: arrayEle COMMA non_null_arrayList | arrayEle;
arrayEle: INT_LIT|FLOAT_LIT|STRING_LIT;

//Variable declaration
vardecl: initVardecl|noninitVardecl;
noninitVardecl: idlist COLON typ SEMICOLON;
initVardecl: IDENTIFIER initVardeclEle expr SEMICOLON;
initVardeclEle: (COMMA IDENTIFIER initVardeclEle expr COMMA) |COMMA IDENTIFIER COLON typ ASSIG_OP expr COMMA; 
idlist: IDENTIFIER COMMA idlist|IDENTIFIER;
typ: BOOLEAN|INT|FLOAT|ARRAY_TYP|STRING|VOID;
exprlist: non_null_exprlist|;
non_null_exprlist: expr COMMA exprlist|expr;
expr: 'expr';

//Parameter declaration
paradecl: OUT? IDENTIFIER COLON typ;

//Function declaration
funcdecl: IDENTIFIER COLON FUNCTION typ paramlist (INHERIT IDENTIFIER)? body;
paramlist: LEFT_PAREN params RIGHT_PAREN;
params: non_null_params|;
non_null_params: paradecl COMMA non_null_params|paradecl;
body: LEFT_CURBRACK RIGHT_CURBRACK;
//body: LEFT_CURBRACK bodyelements RIGHT_CURBRACK;

//EXPRESSIONS
concat_expr: concat_operand CONCAT_OP concat_operand | relational_expr;
concat_operand:STRING_LIT | IDENTIFIER;
relational_expr: relational_EQ_expr|relational_noEQ_expr | logical_expr;
relational_EQ_expr: relational_EQ_operand relational_EQ_op relational_EQ_operand;
relational_noEQ_expr:relational_noEQ_operand relational_noEQ_op relational_noEQ_operand;
relational_EQ_operand: BOOL_LIT|INT_LIT|IDENTIFIER;
relational_EQ_op:EQUAL_TO_OP|NOT_EQUAL_TO_OP;
relational_noEQ_op: LESS_OP|EQ_LESS_OP|GREATER_OP|EQ_GREATER_OP;
relational_noEQ_operand:FLOAT_LIT|INT_LIT|IDENTIFIER;
logical_expr: logical_expr logical_op add_expr|add_expr;
logical_op:CONJ_OP|DISJ_OP;
add_expr: add_expr (ADD_OP|SUB_OP) mul_expr|mul_expr;
mul_expr: mul_expr mul_op nega_expr|nega_expr;
mul_op: MUL_OP|DIV_OP|MOD_OP;
nega_expr: NEGA_OP nega_expr|sign_expr;
sign_expr: SUB_OP sign_expr|index_expr;
index_expr: IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK| subexpr ;
index_list:  INT_LIT COMMA index_list|INT_LIT ;
subexpr:IDENTIFIER |BOOL_LIT| INT_LIT | FLOAT_LIT | LEFT_PAREN concat_expr RIGHT_PAREN;
funcall_expr: IDENTIFIER LEFT_PAREN argulist RIGHT_PAREN;
argulist: IDENTIFIER COMMA argulist|IDENTIFIER;
COMMENT: '/*' .*? '*/' | ('//' (~[\r\n]*)?) ;

BOOL_LIT: 'false' | 'true';

//KEYWORD
AUTO:'auto';
INT: 'integer';
VOID: 'void';
ARRAY_TYP: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
STRING: 'string';
FOR: 'for';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit' {self.text = 'KEYWORD'};

//OPERATORS
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
NEGA_OP: '!';
CONJ_OP: '&&';
DISJ_OP: '||';
EQUAL_TO_OP: '==';
NOT_EQUAL_TO_OP: '!=';
LESS_OP: '<';
EQ_LESS_OP: '<=';
GREATER_OP: '>';
EQ_GREATER_OP: '>=';
CONCAT_OP: '::' {self.text = 'OPERATORS'};



//SEP
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
COMMA: ',';
SEMICOLON: ';';
COLON: ':.?';
LEFT_CURBRACK: '{';
RIGHT_CURBRACK: '}';
ASSIG_OP: '=';
LEFT_SQUAREBRACK: '[';
RIGHT_SQUAREBRACK: ']';
DOT: '.';



IDENTIFIER: ([a-z_] [a-z0-9]*);


//LITERALS
INT_LIT: ([1-9] DIGIT*? [_])+ (DIGIT DIGIT? DIGIT?) {self.text = "".join(self.text.split("_"))
		}
	| '0\n'
	| [1-9] DIGIT*;
fragment DIGIT: [0-9];
INDEX:([0-9]|[1-9][0-9]+);
STRING_LIT: '"' (~["\n] | '\\"')* '"' {self.text = self.text[1:-1]} | '"' (~'"' | '\\"')*  '\n' (~'"' | '\\"')*  '"' {raise IllegalEscape(self.text)};

FLOAT_LIT:
	INT_LIT DECPART {self.text = "".join(self.text.split("_"))}
	| INT_LIT DECPART EXPPART {self.text = "".join(self.text.split("_"))
											};
fragment DECPART: '.' [0-9]+;
fragment EXPPART: [eE] '-'? [0-9]+;

//ARRAY: [{] ([ ]? ELEMENT ',')* ([ ]? ELEMENT)? [}];
//fragment ELEMENT: ( INT_LIT | STRING_LIT| FLOAT_LIT);

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;