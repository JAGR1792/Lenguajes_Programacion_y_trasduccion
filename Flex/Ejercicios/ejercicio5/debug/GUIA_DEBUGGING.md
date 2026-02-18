# Guía de Debugging: Flex vs Handwritten C

## 1. Debugging en C Handwritten

### Técnicas básicas:

#### A) **Compilación condicional con `-DDEBUG`**

```c
#ifdef DEBUG
fprintf(stderr, "Debug info: valor=%d\n", valor);
#endif
```

**Compilar:**
```bash
# Versión normal (sin debug)
cc -o programa programa.c

# Versión con debug
cc -DDEBUG -o programa_debug programa.c
```

#### B) **Printf debugging**

El método más simple y efectivo:

```c
printf("DEBUG: Entrando a función X\n");
printf("DEBUG: Variable i=%d, j=%d\n", i, j);
printf("DEBUG: Carácter recibido: '%c' (ASCII %d)\n", c, c);
```

#### C) **GDB (GNU Debugger)**

```bash
# Compilar con símbolos de debug
cc -g -o programa programa.c

# Iniciar GDB
gdb ./programa

# Comandos útiles:
(gdb) break main          # Punto de interrupción
(gdb) run                 # Ejecutar
(gdb) step                # Avanzar línea por línea
(gdb) print variable      # Ver valor de variable
(gdb) continue            # Continuar ejecución
```

#### D) **Valgrind (para memory leaks)**

```bash
valgrind --leak-check=full ./programa
```

### Ventajas del debugging en C handwritten:

✅ **Control total**: Ves exactamente cada línea ejecutada
✅ **Simple**: Solo 32 líneas de código
✅ **Rápido**: Compilación directa, sin pasos intermedios
✅ **Comprensible**: Lógica lineal fácil de seguir

### Desventajas:

❌ Tienes que agregar debug code manualmente
❌ Más propenso a bugs lógicos (olvidar resetear variables)

---

## 2. Debugging en Flex

### Técnicas básicas:

#### A) **Debug interno de Flex**

```c
%{
#ifdef DEBUG
extern int yy_flex_debug;  // Variable global de Flex
#endif
%}

%%
/* ... reglas ... */
%%

int main() {
    #ifdef DEBUG
    yy_flex_debug = 1;  // Activa modo verbose
    #endif
    yylex();
}
```

**Compilar:**
```bash
flex -o scanner.c scanner.l
cc -DDEBUG -o scanner scanner.c -lfl
```

#### B) **Debugging de reglas**

Agregar prints en las acciones:

```flex
[a-zA-Z]+  { 
    #ifdef DEBUG
    fprintf(stderr, "[MATCH] WORD: '%s'\n", yytext);
    #endif
    words++; 
}
```

#### C) **Opción -d de Flex**

Genera código con debug habilitado:

```bash
flex -d -o scanner.c scanner.l
cc -o scanner scanner.c -lfl
```

Output muestra cada transición del autómata.

#### D) **Ver el código generado**

```bash
# Generar y examinar el código C
flex -o scanner.c scanner.l
less scanner.c  # Ver las ~45,000 líneas generadas
```

Busca funciones como:
- `yylex()` - El scanner principal
- `yy_get_next_buffer()` - Manejo de buffer
- `yy_try_NUL_trans()` - Transiciones

#### E) **Flex con GDB**

```bash
flex -o scanner.c scanner.l
cc -g -o scanner scanner.c -lfl
gdb ./scanner

# Breakpoint útiles:
(gdb) break yylex
(gdb) break yy_get_next_buffer
```

### Ventajas del debugging en Flex:

✅ **Modo verbose integrado**: `yy_flex_debug = 1`
✅ **Menos código que debuggear**: Solo escribes las reglas
✅ **Herramientas específicas**: Flex tiene opciones de debug built-in

### Desventajas:

❌ **Código generado complejo**: 45,000 líneas incomprensibles
❌ **Difícil seguir el flujo**: El autómata no es intuitivo
❌ **Más layers de abstracción**: No sabes exactamente qué hace internamente

---

## 3. Comparación de Técnicas

| Aspecto | Handwritten C | Flex |
|---------|--------------|------|
| **Tiempo de setup** | Inmediato | Requiere compilar .l → .c |
| **Comprensibilidad** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Control fino** | Total | Limitado |
| **Herramientas** | printf, GDB, Valgrind | yy_flex_debug, GDB |
| **Curva aprendizaje** | Baja | Media-Alta |

---

## 4. Ejemplo Práctico: Debugging de un Bug

### Problema: ¿Por qué no cuenta "123" como palabra?

#### En Handwritten C:

```bash
echo "hello 123 world" | ./wc_handwritten_debug 2>&1
```

Output:
```
Char[7]: '1' (ASCII 49)
Char[8]: '2' (ASCII 50)
Char[9]: '3' (ASCII 51)
```

**Diagnóstico inmediato**: `isalpha('1')` es `false`, así que no entra en el bloque de palabras.

#### En Flex:

```bash
echo "hello 123 world" | ./wc_flex_debug 2>&1
```

Output:
```
[TOKEN] WORD: 'hello'
[TOKEN] CHAR: ' '
[TOKEN] CHAR: '1'
[TOKEN] CHAR: '2'
[TOKEN] CHAR: '3'
```

**Diagnóstico**: La regla `[a-zA-Z]+` no matchea dígitos.

### Solución en ambos:

**Handwritten**: Cambiar `isalpha(c)` → `isalnum(c)`

**Flex**: Cambiar `[a-zA-Z]+` → `[a-zA-Z0-9]+`

---

## 5. Herramientas Avanzadas

### Para C (ambos):
- **AddressSanitizer**: `cc -fsanitize=address`
- **UndefinedBehaviorSanitizer**: `cc -fsanitize=undefined`
- **strace**: Ver syscalls
- **ltrace**: Ver llamadas a biblioteca

### Para Flex específicamente:
- **Graphviz**: Visualizar el autómata generado
- **flex --debug**: Información de construcción
- **flex --verbose**: Estadísticas del scanner

---

## 6. Conclusiones

### Para debugging de programas simples:
👍 **Handwritten C gana** - más fácil, más rápido, más intuitivo

### Para gramáticas complejas:
👍 **Flex gana** - las herramientas integradas y el modo verbose compensan la complejidad

### Recomendación:
- Usa **handwritten C** para scanners simples (< 100 líneas)
- Usa **Flex** para gramáticas complejas donde el debugging del autómata sería imposible manualmente
