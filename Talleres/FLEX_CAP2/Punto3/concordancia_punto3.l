/* Punto 3: tabla de simbolos dinamica por rehashing */
%option noyywrap nodefault yylineno case-insensitive
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

static struct symbol *symtab = NULL;
static size_t nhash = 0;
static size_t nused = 0;
static char *curfilename;

#define INITIAL_NHASH 1021
#define LOAD_NUM 7
#define LOAD_DEN 10

static unsigned symhash(const char *sym);
static void symtab_init(size_t size);
static void symtab_rehash(size_t new_size);
static struct symbol *lookup(const char *sym);
static void addref(int lineno, char *filename, char *word, int flags);
static void printrefs(void);

static unsigned
symhash(const char *sym)
{
    unsigned int hash = 0;
    unsigned char c;

    while ((c = (unsigned char)*sym++)) {
        hash = hash * 9u ^ c;
    }
    return hash;
}

static void
symtab_init(size_t size)
{
    symtab = calloc(size, sizeof(struct symbol));
    if (!symtab) {
        fputs("out of space\n", stderr);
        exit(1);
    }
    nhash = size;
    nused = 0;
}

static void
symtab_rehash(size_t new_size)
{
    struct symbol *oldtab = symtab;
    size_t oldsize = nhash;
    size_t i;

    symtab = calloc(new_size, sizeof(struct symbol));
    if (!symtab) {
        fputs("out of space\n", stderr);
        exit(1);
    }

    nhash = new_size;
    nused = 0;

    for (i = 0; i < oldsize; i++) {
        if (oldtab[i].name) {
            unsigned h = symhash(oldtab[i].name) % nhash;
            while (symtab[h].name) {
                h = (h + 1) % nhash;
            }
            symtab[h] = oldtab[i];
            nused++;
        }
    }

    free(oldtab);
}

static struct symbol *
lookup(const char *sym)
{
    size_t probes;
    unsigned h;

    if (!symtab) {
        symtab_init(INITIAL_NHASH);
    }

    if ((nused + 1) * LOAD_DEN >= nhash * LOAD_NUM) {
        symtab_rehash(nhash * 2 + 1);
    }

    h = symhash(sym) % nhash;
    probes = nhash;

    while (probes--) {
        if (symtab[h].name) {
            if (strcmp(symtab[h].name, sym) == 0) {
                return &symtab[h];
            }
        } else {
            symtab[h].name = strdup(sym);
            if (!symtab[h].name) {
                fputs("out of space\n", stderr);
                exit(1);
            }
            symtab[h].reflist = NULL;
            nused++;
            return &symtab[h];
        }
        h = (h + 1) % nhash;
    }

    fputs("unexpected lookup failure\n", stderr);
    exit(1);
}

static void
addref(int lineno, char *filename, char *word, int flags)
{
    struct ref *r;
    struct symbol *sp = lookup(word);

    if (sp->reflist &&
        sp->reflist->lineno == lineno &&
        sp->reflist->filename == filename) {
        return;
    }

    r = malloc(sizeof(struct ref));
    if (!r) {
        fputs("out of space\n", stderr);
        exit(1);
    }

    r->next = sp->reflist;
    r->filename = filename;
    r->lineno = lineno;
    r->flags = flags;
    sp->reflist = r;
}

static int
symcompare(const void *xa, const void *xb)
{
    const struct symbol *a = *(const struct symbol * const *)xa;
    const struct symbol *b = *(const struct symbol * const *)xb;
    return strcmp(a->name, b->name);
}

static void
printrefs(void)
{
    struct symbol **used;
    size_t i, j = 0;

    if (!symtab || nused == 0) {
        return;
    }

    used = malloc(nused * sizeof(struct symbol *));
    if (!used) {
        fputs("out of space\n", stderr);
        exit(1);
    }

    for (i = 0; i < nhash; i++) {
        if (symtab[i].name) {
            used[j++] = &symtab[i];
        }
    }

    qsort(used, nused, sizeof(struct symbol *), symcompare);

    for (i = 0; i < nused; i++) {
        struct symbol *sp = used[i];
        char *prevfn = NULL;
        struct ref *rp = sp->reflist;
        struct ref *rpp = NULL;
        struct ref *rpn;

        while (rp) {
            rpn = rp->next;
            rp->next = rpp;
            rpp = rp;
            rp = rpn;
        }

        printf("%10s", sp->name);
        for (rp = rpp; rp; rp = rp->next) {
            if (rp->filename == prevfn) {
                printf(" %d", rp->lineno);
            } else {
                printf(" %s:%d", rp->filename, rp->lineno);
                prevfn = rp->filename;
            }
        }
        printf("\n");
    }

    free(used);
}
%}
%%
(a|an|and|are|as|at|be|but|for|in|is|it|of|on|or|that|the|this|to) ;

[a-z]+(\'(s|t))? { addref(yylineno, curfilename, yytext, 0); }
.|\n               ;
%%
int
main(int argc, char **argv)
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
