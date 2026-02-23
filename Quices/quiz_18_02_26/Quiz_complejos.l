%{
#include <stdio.h>
%}

%%

([-]?[0-9]+[.][0-9]+|[-]?[0-9]+)[ \t]*([+]|[-])[ \t]*([-]?[0-9]+[.][0-9]+|[-]?[0-9]+)[iIjJ] { printf("Acepta\n"); }
([-]?[0-9]+[.][0-9]+|[-]?[0-9]+)[iIjJ] { printf("Acepta\n"); }

[ \t]+ { }
\n     { }
.      { printf("No Acepta\n"); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("Error al abrir archivo");
            return 1;
        }
    }
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}


