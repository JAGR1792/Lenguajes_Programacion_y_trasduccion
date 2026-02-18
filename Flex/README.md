# Flex

Este directorio contiene ejemplos y ejercicios de Flex (y algunos con Bison).
Los binarios pueden venir precompilados, pero en otro sistema operativo o CPU
se recomienda recompilar.

## Estructura

- Ejemplos/    ejemplos basicos
- Ejercicios/  ejercicios y entregas

## Requisitos

- flex
- bison (cuando haya .y)
- gcc o clang

En Debian/Ubuntu:

  sudo apt install flex bison gcc

## Ejecutar

Si el binario ya existe y funciona en tu arquitectura:

  ./nombre_del_ejecutable

Ejemplo:

  ./ejemplo5

## Compilar (Flex solo)

Si solo hay .l:

  flex -o lex.yy.c archivo.l
  cc -o salida lex.yy.c -lfl

## Compilar (Flex + Bison)

Si hay .l y .y:

  bison -d archivo.y
  flex -o lex.yy.c archivo.l
  cc -o salida archivo.tab.c lex.yy.c -lfl

## Notas

- Siempre recompilar si cambiaste los .l o .y.
- En algunos ejercicios hay scripts o README especificos dentro de cada carpeta.
