# Comparación de rendimiento: Flex vs Handwritten C

## Archivos

### Raíz (ejercicio5/)
- `wc.l` - Código fuente Flex
- `wc_handwritten.c` - Código fuente C handwritten
- `wc_flex` - Ejecutable Flex
- `wc_handwritten` - Ejecutable C
- `test_large.txt` - Archivo de prueba (100,000 líneas, 6.9 MB)
- `benchmark.sh` - Script para medir rendimiento
- `COMPARACION.md` - Este archivo

### debug/
- Versiones con debugging habilitado
- Guía completa de debugging: `debug/GUIA_DEBUGGING.md`

---

## Cómo ejecutar el benchmark

```bash
# Método rápido (todo automatizado)
./benchmark.sh

# Método manual
time ./wc_flex < test_large.txt
time ./wc_handwritten < test_large.txt
```

---

## Resultados (100,000 líneas)

| Versión | Tiempo Real | Rendimiento |
|---------|-------------|-------------|
| **Handwritten C** | **0.044s** | ⚡ **77% más rápido** |
| Flex | 0.078s | Baseline |
| System wc | 0.024s | Referencia |

---

## Análisis

### ¿Es notablemente más rápida la versión C?

**SÍ - casi el doble de rápida** (44ms vs 78ms)

### ¿Por qué?

1. **Menos overhead**: Código optimizado para una tarea específica
2. **Lógica simple**: Solo trackea `in_word` vs state machine de Flex
3. **Menos capas**: `getchar()` directo vs buffers/backtracking de Flex

### ¿Debugging?

**Handwritten C fue MÁS FÁCIL:**
- 32 líneas vs 45,000 generadas por Flex
- Lógica clara y visible
- Printf debugging simple y efectivo

Ver `debug/GUIA_DEBUGGING.md` para técnicas detalladas.

---

## Conclusión

**Para word count (tarea simple):**
- ✅ Handwritten C: más rápido, más simple, más fácil de debuggear

**Para compiladores (gramáticas complejas):**
- ✅ Flex: menos errores, más mantenible, patrones declarativos
