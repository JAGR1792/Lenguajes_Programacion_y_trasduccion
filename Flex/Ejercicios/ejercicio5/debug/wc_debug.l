/* Flex word count con debugging */
%{
int chars = 0;
int words = 0;
int lines = 0;

/* Función para debug */
void debug_token(const char* token_name, const char* text) {
    #ifdef DEBUG
    fprintf(stderr, "[TOKEN] %s: '%s'\n", token_name, text);
    #endif
}
%}

%%

[a-zA-Z]+    { 
    words++; 
    chars += strlen(yytext); 
    debug_token("WORD", yytext);
}

\n           { 
    chars++; 
    lines++; 
    debug_token("NEWLINE", "\\n");
}

.            { 
    chars++; 
    debug_token("CHAR", yytext);
}

%%

int main(int argc, char **argv)
{
    #ifdef DEBUG
    fprintf(stderr, "=== MODO DEBUG ACTIVADO (FLEX) ===\n");
    yy_flex_debug = 1;  /* Activa debug interno de Flex */
    #endif
    
    yylex();
    
    #ifdef DEBUG
    fprintf(stderr, "\n=== RESUMEN FINAL ===\n");
    fprintf(stderr, "Líneas: %d\n", lines);
    fprintf(stderr, "Palabras: %d\n", words);
    fprintf(stderr, "Caracteres: %d\n", chars);
    #endif
    
    printf("%8d%8d%8d\n", lines, words, chars);
    return 0;
}
