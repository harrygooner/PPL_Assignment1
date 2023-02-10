grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

IDENTIFIERS: [a-z][a-z0-9]+;
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;