%{
# include "Ejercicio1.tab.h"
# include <stdlib.h>
# include <stdio.h>
%}

%%
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"|" { return ABS; }
"(" { return OP; }
")" { return CP; }
"//".*\n { /* ignore comments with newline */ }
[0-9]+ { yylval.ival = atoi(yytext); return NUMBER; }
\n { return EOL; }
[ \t] { /* ignore whitespace */ }
. { printf("Mystery character %c\n", *yytext); }
%%

