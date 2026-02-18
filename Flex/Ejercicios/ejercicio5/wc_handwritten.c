/* Handwritten word count program in C - equivalent to wc.l */
#include <stdio.h>
#include <ctype.h>

int main(int argc, char **argv)
{
    int chars = 0;
    int words = 0;
    int lines = 0;
    int in_word = 0;
    int c;
    
    while((c = getchar()) != EOF) {
        chars++;
        
        if(c == '\n') {
            lines++;
            in_word = 0;
        }
        else if(isalpha(c)) {
            if(!in_word) {
                words++;
                in_word = 1;
            }
        }
        else {
            in_word = 0;
        }
    }
    
    printf("%8d%8d%8d\n", lines, words, chars);
    return 0;
}
