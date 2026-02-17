/* English -> American */

%%
"colour"        { printf("color"); }
"flavour"       { printf("sabor"); }

"clever"        { printf("inteligente"); }
"smart"         { printf("elegante"); }
"conservative"  { printf("liberal"); }

\n              { printf("\n"); }
.               { printf("%s", yytext); }
%%

main(int argc, char **argv)
{
    yylex();
}

