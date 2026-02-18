/* Handwritten word count con debugging */
#include <stdio.h>
#include <ctype.h>

int main(int argc, char **argv)
{
    int chars = 0;
    int words = 0;
    int lines = 0;
    int in_word = 0;
    int c;
    
    // DEBUG: Activar con -DDEBUG en compilación
    #ifdef DEBUG
    fprintf(stderr, "=== MODO DEBUG ACTIVADO ===\n");
    #endif
    
    while((c = getchar()) != EOF) {
        chars++;
        
        #ifdef DEBUG
        // Mostrar cada carácter procesado
        if(isprint(c)) {
            fprintf(stderr, "Char[%d]: '%c' (ASCII %d)\n", chars, c, c);
        } else {
            fprintf(stderr, "Char[%d]: [control] (ASCII %d)\n", chars, c);
        }
        #endif
        
        if(c == '\n') {
            lines++;
            in_word = 0;
            
            #ifdef DEBUG
            fprintf(stderr, "  -> Nueva línea detectada (total: %d)\n", lines);
            #endif
        }
        else if(isalpha(c)) {
            if(!in_word) {
                words++;
                in_word = 1;
                
                #ifdef DEBUG
                fprintf(stderr, "  -> Nueva palabra #%d iniciada\n", words);
                #endif
            }
        }
        else {
            if(in_word) {
                #ifdef DEBUG
                fprintf(stderr, "  -> Palabra finalizada\n");
                #endif
            }
            in_word = 0;
        }
    }
    
    #ifdef DEBUG
    fprintf(stderr, "\n=== RESUMEN FINAL ===\n");
    fprintf(stderr, "Líneas: %d\n", lines);
    fprintf(stderr, "Palabras: %d\n", words);
    fprintf(stderr, "Caracteres: %d\n", chars);
    #endif
    
    printf("%8d%8d%8d\n", lines, words, chars);
    return 0;
}
