
%option noyywrap nodefault yylineno case-insensitive
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct ref {
    struct ref *next;
    char *filename;
    int flags;
    int lineno;
};

struct symbol {
    char *name;
    struct ref *reflist;
};

#define NHASH 9997
static struct symbol symtab[NHASH];
static char *curfilename;

unsigned symhash(const char *sym);
struct symbol *lookup(const char *sym);
void addref(int lineno, char *filename, char *word, int flags);
void printrefs(void);

static int symcmp(const void *a, const void *b) {
    const struct symbol *sa = *(const struct symbol **)a;
    const struct symbol *sb = *(const struct symbol **)b;
    return strcasecmp(sa->name, sb->name);
}

unsigned symhash(const char *sym)
{
    unsigned int hash = 0;
    while (*sym) {
        hash = hash * 31u + (unsigned char)tolower((unsigned char)*sym);
        sym++;
    }
    return hash % NHASH;
}

struct symbol *lookup(const char *sym)
{
    unsigned int h = symhash(sym);
    unsigned int start = h;

    while (symtab[h].name) {
        if (strcasecmp(symtab[h].name, sym) == 0) {
            return &symtab[h];
        }
        h = (h + 1) % NHASH;
        if (h == start) {
            fprintf(stderr, "tabla de simbolos llena\n");
            exit(1);
        }
    }

    symtab[h].name = strdup(sym);
    if (!symtab[h].name) {
        perror("strdup");
        exit(1);
    }
    symtab[h].reflist = NULL;
    return &symtab[h];
}

void addref(int lineno, char *filename, char *word, int flags)
{
    struct symbol *sp = lookup(word);
    struct ref *r = malloc(sizeof(struct ref));
    if (!r) {
        perror("malloc");
        exit(1);
    }
    r->filename = filename;
    r->flags = flags;
    r->lineno = lineno;
    r->next = sp->reflist;
    sp->reflist = r;
}

void printrefs(void)
{
    struct symbol **used = malloc(sizeof(struct symbol *) * NHASH);
    int i;
    int nused = 0;

    if (!used) {
        perror("malloc");
        exit(1);
    }

    for (i = 0; i < NHASH; i++) {
        if (symtab[i].name) {
            used[nused++] = &symtab[i];
        }
    }

    qsort(used, nused, sizeof(struct symbol *), symcmp);

    for (i = 0; i < nused; i++) {
        struct symbol *sp = used[i];
        struct ref *r;
        printf("%s:\n", sp->name);
        for (r = sp->reflist; r; r = r->next) {
            printf("  %s:%d\n", r->filename, r->lineno);
        }
    }

    free(used);
}
%}
%%
^(a|an|and|are|as|at|be|but|for|in|is|it|of|on|or|that|the|this|to)$ ;
(a|an|and|are|as|at|be|but|for|in|is|it|of|on|or|that|the|this|to)    ;

[a-z]+(\'(s|t))? { addref(yylineno, curfilename, yytext, 0); }
.|\n               ;
%%
int main(int argc, char **argv)
{
    int i;

    if (argc < 2) {
        curfilename = "(stdin)";
        yylineno = 1;
        yylex();
    } else {
        for (i = 1; i < argc; i++) {
            FILE *f = fopen(argv[i], "r");
            if (!f) {
                perror(argv[i]);
                return 1;
            }
            curfilename = argv[i];
            yyrestart(f);
            yylineno = 1;
            yylex();
            fclose(f);
        }
    }

    printrefs();
    return 0;
}
