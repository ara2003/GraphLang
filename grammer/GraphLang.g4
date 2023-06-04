
grammar GraphLang;

program
    : func_def_stmt* code EOF
    ;

code_block
 : '{' code '}'
 ;

code
 : code_stmt*
 ;

code_stmt
 : code_block
 | stmt ';'
 ;

stmt
    : init_var_stmt
    | assign_stmt
    | funcCall
    | while_stmt
    | if_stmt
    | return_stmt
    ;

assign_stmt
 : ID '=' expr
 ;

expr
 : unary_expr (OPERATION unary_expr)*
 ;

unary_expr
 : 'not'? pre_inc* atom_expr post_inc*
 ;

pre_inc
 : INCREMENT
 ;
 
post_inc
 : INCREMENT
 ;
 
atom_expr
 : variable_expr
 | INT
 | BOOL
 | graph
 | arc
 | type_cast_expr
 ;

variable_expr
 : ID
 ;

gl_type
 : GRAPHTYPE
 | NODETYPE
 | ARCTYPE
 ;

init_var_stmt
    : 'var' ID ('=' expr)?
    ;

return_stmt
 : 'return' expr
 ;
    
graph : '{' nodes ';' arcs '}';

nodes
 : expr (',' expr)*
 ;

arcs
 : expr (',' expr)*
 ;

arc : '{' ID ',' ID ',' expr '}';

func : 'function' ID '(' (expr (',' expr)*)? ')' ;

func_def_stmt : 'function' ID '(' (parametr (',' parametr)*)? ')' '{' code '}';

parametr
 : ID
 ;

funcCall : ID '(' (expr (',' expr)* )? ')' ;

if_stmt : 'if' '(' expr ')' code_stmt ('else' code_stmt)?  ;

while_stmt : 'while' '(' expr ')' code_stmt ;

type_cast_expr : '(' gl_type ')' expr ;


INCREMENT : '++'|'--' ;
OPERATION : '*'|'/'|'+'|'-'|'=='|'!='|'>'|'<'|'>='|'<='|'or'|'and' ;
GRAPHTYPE : 'graph' ;
NODETYPE : 'node' ;
ARCTYPE : 'arc' ;
INT : [0-9]+ ;
BOOL : 'True' | 'False' ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;