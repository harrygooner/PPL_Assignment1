grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

COMMENT: '/*' .*? '*/' {self.text = 'COMMENT'} | '//' .*? {self.text = 'COMMENT'};

BOOLEAN: 'false' | 'true';

KEYWORD:
	'auto'
	| 'integer'
	| 'void'
	| 'array'
	| 'break'
	| 'float'
	| 'return'
	| 'out'
	| 'boolean'
	| 'string'
	| 'for'
	| 'continue'
	| 'do'
	| 'function'
	| 'of'
	| 'else'
	| 'if'
	| 'while'
	| 'inherit' {self.text = 'KEYWORD'};

//SEP
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LEFT_CURBRACK: '{';
RIGHT_CURBRACK: '}';
ASSIG_OP: '=';
LEFT_SQUAREBRACK: '[';
RIGHT_SQUAREBRACK: ']';
DOT: '.';

//OPERATORS
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
LOG_NOT_OP: '!';
LOG_AND_OP: '&&';
LOG_OR_OP: '||';
EQUAL_TO_OP: '==';
NOT_EQUAL_TO_OP: '!=';
LESS_OP: '<';
EQ_LESS_OP: '<=';
GREATER_OP: '>';
GREATER_THAN_OP: '>=';
STRING_OP: '::' {self.text = 'OPERATORS'};

IDENTIFIERS: ([a-z] [a-z0-9]+);

//LITERALS
INT_LIT: ([1-9] DIGIT*? [_])+ (DIGIT DIGIT? DIGIT?) {self.text = "".join(self.text.split("_"))
		}
	| '0'
	| [1-9] DIGIT*;
fragment DIGIT: [0-9];

STRINGLIT: '"' (~'"' | '\\"')* '"' {self.text = self.text[1:-1]};

FLOAT_LIT:
	INT_LIT DECPART {self.text = "".join(self.text.split("_"))}
	| INT_LIT DECPART EXPPART {self.text = "".join(self.text.split("_"))
											};
fragment DECPART: '.' [0-9]+;
fragment EXPPART: [eE] '-'? [0-9]+;

ARRAY: [{] ([ ]? ELEMENT ',')* ([ ]? ELEMENT)? [}];
fragment ELEMENT: ( INT_LIT | STRINGLIT | FLOAT_LIT);

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;