# ====================
# Clase Trie y Nodo
# ====================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserta una palabra en el Trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Verifica si una palabra existe en el Trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    
    def _buscar_palabras_desde_nodo(self, node, prefix, suggestions):
        """Recorrido DFS para recolectar palabras completas desde un nodo"""
        if node.is_end_of_word:
            suggestions.append(prefix)
        for char, child in node.children.items():
            self._buscar_palabras_desde_nodo(child, prefix + char, suggestions)
    
    def autocomplete(self, prefix: str):
        """
        Retorna todas las palabras que comienzan con el prefijo dado
        
        Args:
            prefix: el prefijo a buscar
            
        Returns:
            lista de palabras que comienzan con el prefijo
        """
        node = self.root
        suggestions = []
        
        # Navegar hasta el final del prefijo
        for char in prefix:
            if char not in node.children:
                return suggestions  # Prefijo no existe
            node = node.children[char]
        
        # Buscar todas las palabras desde este nodo
        self._buscar_palabras_desde_nodo(node, prefix, suggestions)
        return sorted(suggestions)