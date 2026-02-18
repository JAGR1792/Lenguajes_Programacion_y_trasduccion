# Ejercicio 5: Word Count - Flex vs C Handwritten

## 📁 Estructura

```
ejercicio5/
├── wc.l                    # Código fuente Flex
├── wc_handwritten.c        # Código fuente C handwritten
├── wc_flex                 # Ejecutable Flex
├── wc_handwritten          # Ejecutable C
├── benchmark.sh            # Script de medición
├── test_large.txt          # Archivo de prueba (100K líneas)
├── COMPARACION.md          # Análisis de resultados
└── debug/                  # Versiones con debugging
    ├── GUIA_DEBUGGING.md   # Guía completa de debugging
    └── ...                 # Código y ejecutables de debug
```

## 🚀 Uso Rápido

### Ejecutar benchmark
```bash
./benchmark.sh
```

### Compilar desde cero
```bash
# Flex
flex -o debug/wc.c wc.l
cc -o wc_flex debug/wc.c -lfl

# Handwritten
cc -o wc_handwritten wc_handwritten.c
```

### Probar manualmente
```bash
echo "hello world" | ./wc_flex
echo "hello world" | ./wc_handwritten
```

## 📊 Resultados

- **Handwritten C**: 44ms (⚡ 77% más rápido)
- **Flex**: 78ms

Ver `COMPARACION.md` para análisis completo.

## 🐛 Debugging

Ver `debug/GUIA_DEBUGGING.md` para técnicas detalladas.
