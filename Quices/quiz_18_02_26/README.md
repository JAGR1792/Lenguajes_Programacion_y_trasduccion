# Analizador de Números Complejos en Lex

## Descripción
Este programa utiliza **Lex** (Flex) para crear un analizador léxico que reconoce y valida números complejos en la forma `a+bi` o `a-bi`.

## Características
- **Acepta números reales** como parte real e imaginaria (con o sin decimales)
- **Soporta signos** positivos y negativos
- **Unidades imaginarias múltiples**: i, I, J, j
- **Formatos válidos**:
  - `3+2i` (enteros)
  - `3.5+2.5i` (decimales)
  - `3.5+2i` (mixtos)
  - `2i` (imaginario puro)
  - `3 + 2i` (con espacios)
  - `3.5 + 2.i` (decimal con punto antes de i)
  - `-3+2i` (con signo negativo)

## Definiciones
### Número
```
[0-9]+([.][0-9]+)? // No pude identificarlos con un identificador unico
```
- Uno o más dígitos
- Opcionalmente seguidos de punto decimal y más dígitos

### Unidad Imaginaria (i's)
```
[iIjJ]
```
- Cualquiera de: i, I, J, j

## Compilación
```bash
flex Quiz_complejos.l
gcc -o lex.yy.c -lfl
```

## Uso
```bash
./a.out archivo.txt
```

Donde `archivo.txt` contiene números complejos, uno por línea.

## Salida
Por cada línea procesa:
- **Acepta** - si es un número complejo válido
- **No Acepta** - si no es un número complejo válido

## Ejemplos de Entrada/Salida

**archivo.txt:**
```
3.5+2i
3.5 + 2.i
5-3I
-2.5+4j
1+1J
10+20i
3.5+2
abc
2i
-5
7.5+4.2i
```

**Salida:**
```
Acepta
Acepta
Acepta
Acepta
Acepta
Acepta
No Acepta
No Acepta
Acepta
No Acepta
Acepta
```
