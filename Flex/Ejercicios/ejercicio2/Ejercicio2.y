%{
#include <stdio.h>
#include <stdlib.h>
%}

%union {
    int ival;
}

%token <ival> NUMBER
%token ADD SUB MUL DIV ABS
%token AND OR
%token EOL
%token OP CP
%type <ival> exp and_expr add_expr mul_expr unary atom

%left OR
%left AND
%left ADD SUB
%left MUL DIV
%right ABS

%%

calclist:
    /* empty */
  | calclist exp EOL { printf("= %d (0x%x)\n", $2, $2); }
  ;

exp:
    and_expr { $$ = $1; }
  | exp OR and_expr { $$ = $1 | $3; }
  ;

and_expr:
    add_expr { $$ = $1; }
  | and_expr AND add_expr { $$ = $1 & $3; }
  ;

add_expr:
    mul_expr { $$ = $1; }
  | add_expr ADD mul_expr { $$ = $1 + $3; }
  | add_expr SUB mul_expr { $$ = $1 - $3; }
  ;

mul_expr:
    unary { $$ = $1; }
  | mul_expr MUL unary { $$ = $1 * $3; }
  | mul_expr DIV unary { $$ = $1 / $3; }
  ;

unary:
    atom { $$ = $1; }
  | ABS unary { $$ = $2 >= 0 ? $2 : -$2; }
  | ABS exp ABS { $$ = $2 >= 0 ? $2 : -$2; }
  | SUB unary { $$ = -$2; }
  ;

atom:
    NUMBER { $$ = $1; }
  | OP exp CP { $$ = $2; }
  | atom ABS { $$ = $1 >= 0 ? $1 : -$1; }
  ;

%%

int main(int argc, char **argv)
{
    return yyparse();
}

int yyerror(char *s)
{
    fprintf(stderr, "error: %s\n", s);
    return 0;
}