import os
from trie import Trie

# Leer el diccionario
print("="*70)
print("INSTANCIANDO TRIE CON DICCIONARIO")
print("="*70)

trie = Trie()

# Obtener la ruta del directorio donde está el script
script_dir = os.path.dirname(os.path.abspath(__file__))
diccionario_path = os.path.join(script_dir, 'diccionario.txt')

# Cargar palabras del diccionario
with open(diccionario_path, 'r', encoding='utf-8') as f:
    palabras = [linea.strip().lower() for linea in f if linea.strip()]

print(f"\n✓ Diccionario cargado: {len(palabras)} palabras")

# Insertar todas las palabras
for palabra in palabras:
    trie.insert(palabra)

print(f"✓ Trie poblado exitosamente")

# Pruebas de búsqueda exacta
print("\n" + "="*70)
print("PRUEBAS DE BÚSQUEDA EXACTA (search)")
print("="*70)

palabras_test_search = ["de", "la", "python", "gato", "mundo"]
for palabra in palabras_test_search:
    existe = trie.search(palabra)
    print(f"  search('{palabra}'): {existe}")

# Pruebas de autocompletado
print("\n" + "="*70)
print("PRUEBAS DE AUTOCOMPLETADO (autocomplete)")
print("="*70)

prefijos_test = ["es", "ti", "mu", "p", "v", "a"]
for prefijo in prefijos_test:
    resultados = trie.autocomplete(prefijo)[:10]  # Mostrar solo los primeros 10
    
    print(f"\n  Prefijo '{prefijo}':")
    if resultados:
        print(f"    {resultados}")
    else:
        print(f"    Sin resultados")

print("\n" + "="*70)
