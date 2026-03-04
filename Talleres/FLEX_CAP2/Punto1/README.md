# Punto 1

## Compilar

### Original
```bash
flex Ex2_4.l
cc lex.yy.c -lfl
```

### Versión línea
```bash
flex Ex2_4_linea.l
cc lex.yy.c -lfl
```

### Versión bloques
```bash
flex Ex2_4_bloques.l
cc lex.yy.c -lfl
```

## Ejecutar

### Original
```bash
./a.out entrada_cmp.txt
```

### Versión línea
```bash
./a.out entrada_cmp.txt
```

### Versión bloques
```bash
./a.out entrada_cmp.txt
```

## Comparar las 3 formas

Compila cada versión y guarda su binario:

```bash
flex Ex2_4.l
cc lex.yy.c -lfl
mv a.out ex_original

flex Ex2_4_linea.l
cc lex.yy.c -lfl
mv a.out ex_linea

flex Ex2_4_bloques.l
cc lex.yy.c -lfl
mv a.out ex_bloques
```

Luego compara en 3 columnas:

```bash
paste -d '|' <({ echo 'ORIGINAL'; ./ex_original entrada_cmp.txt; }) <({ echo 'LINEA'; ./ex_linea entrada_cmp.txt; }) <({ echo 'BLOQUES'; ./ex_bloques entrada_cmp.txt; })
```
