#!/bin/bash
# Script para medir rendimiento de forma consistente

echo "======================================"
echo "  Benchmark: Flex vs Handwritten C"
echo "======================================"
echo

# Verificar que los ejecutables existen
if [ ! -f wc_flex ] || [ ! -f wc_handwritten ]; then
    echo "Error: Ejecutables no encontrados"
    echo "Compilando..."
    flex -o debug/wc.c wc.l
    cc -o wc_flex debug/wc.c -lfl
    cc -o wc_handwritten wc_handwritten.c
fi

# Verificar archivo de prueba
if [ ! -f test_large.txt ]; then
    echo "Generando archivo de prueba (100,000 líneas)..."
    for i in {1..100000}; do 
        echo "The quick brown fox jumps over the lazy dog multiple times in this line"
    done > test_large.txt
fi

FILE_SIZE=$(du -h test_large.txt | cut -f1)
echo "Archivo de prueba: test_large.txt ($FILE_SIZE)"
echo

# Ejecutar benchmarks
echo "=== Versión Flex ==="
time ./wc_flex < test_large.txt
echo

echo "=== Versión Handwritten C ==="
time ./wc_handwritten < test_large.txt
echo

echo "=== System wc (referencia) ==="
time wc test_large.txt
echo

echo "======================================"
echo "Benchmark completado"
echo "======================================"
