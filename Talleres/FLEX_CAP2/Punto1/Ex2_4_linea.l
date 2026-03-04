%option noyywrap yylineno
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct bufstack {
    struct bufstack *prev;
    YY_BUFFER_STATE bs;
    int lineno;
    char *filename;
    FILE *f;
} *curbs = 0;

char *curfilename;

int newfile(char *fn);
int popfile(void);

static int parse_include_filename(const char *line, char *out, size_t out_size) {
    const char *start = strchr(line, '"');
    char endc = '"';
    if (!start) {
        start = strchr(line, '<');
        endc = '>';
    }
    if (!start) return 0;
    start++;
    const char *end = strchr(start, endc);
    if (!end || end <= start) return 0;

    size_t len = (size_t)(end - start);
    if (len + 1 > out_size) return 0;
    memcpy(out, start, len);
    out[len] = '\0';
    return 1;
}
%}
%%
^[ \t]*#include[ \t]*[\"<][^\"\n>]+[\">][^\n]*\n {
    char fname[1024];
    if (!parse_include_filename(yytext, fname, sizeof(fname))) {
        fprintf(stderr, "%4d include mal formado\n", yylineno);
        yyterminate();
    }
    if (!newfile(fname)) yyterminate();
}
^[^\n]*\n { fprintf(yyout, "%4d %s", yylineno++, yytext); }
[^\n]+ { fprintf(yyout, "%4d %s", yylineno, yytext); }
<<EOF>> { if(!popfile()) yyterminate(); }
%%
int main(int argc, char **argv)
{
    if (argc < 2) {
        fprintf(stderr, "need filename\n");
        return 1;
    }
    if (newfile(argv[1])) yylex();
    return 0;
}

int newfile(char *fn)
{
    FILE *f = fopen(fn, "r");
    struct bufstack *bs = malloc(sizeof(struct bufstack));
    if (!f) { perror(fn); return 0; }
    if (!bs) { perror("malloc"); exit(1); }

    if (curbs) curbs->lineno = yylineno;
    bs->prev = curbs;
    bs->bs = yy_create_buffer(f, YY_BUF_SIZE);
    bs->f = f;
    bs->filename = fn;
    yy_switch_to_buffer(bs->bs);

    curbs = bs;
    yylineno = 1;
    curfilename = fn;
    return 1;
}

int popfile(void)
{
    struct bufstack *bs = curbs;
    struct bufstack *prevbs;
    if (!bs) return 0;

    fclose(bs->f);
    yy_delete_buffer(bs->bs);

    prevbs = bs->prev;
    free(bs);
    if (!prevbs) return 0;

    yy_switch_to_buffer(prevbs->bs);
    curbs = prevbs;
    yylineno = curbs->lineno;
    curfilename = curbs->filename;
    return 1;
}
