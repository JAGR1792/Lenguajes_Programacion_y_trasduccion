import os
from trie import Trie

# Cargar diccionario
trie = Trie()

script_dir = os.path.dirname(os.path.abspath(__file__))
diccionario_path = os.path.join(script_dir, 'diccionario.txt')

with open(diccionario_path, 'r', encoding='utf-8') as f:
    palabras = [linea.strip().lower() for linea in f if linea.strip()]

for palabra in palabras:
    trie.insert(palabra)

print("AUTOCOMPLETADO - MOTOR DE BUSQUEDA")
print("-" * 40)

# Prefijos predefinidos
prefijos_test = ["es", "ti", "mu", "p", "v", "a"]
print("Pruebas predefinidas:\n")
for prefijo in prefijos_test:
    resultados = trie.autocomplete(prefijo)[:10]
    print(f"Prefijo '{prefijo}': {resultados}")

# Entrada del usuario
print("\n" + "-" * 40)
print("Ingresa prefijos (escribe 'salir' para terminar):\n")
while True:
    prefijo = input("Prefijo: ").strip().lower()
    if prefijo == "salir":
        break
    if prefijo:
        resultados = trie.autocomplete(prefijo)
        print(f"Resultados para '{prefijo}': {resultados[:20]}")
        if len(resultados) > 20:
            print(f"(Total: {len(resultados)} palabras)\n")
        else:
            print()
