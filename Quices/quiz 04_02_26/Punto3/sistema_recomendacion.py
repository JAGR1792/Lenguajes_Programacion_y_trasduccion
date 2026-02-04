"""
Sistema de Recomendación de Productos
Basado en compras colaborativas: "usuarios que compraron X también compraron Y"
"""

from collections import defaultdict


class SistemaRecomendacion:
    """Sistema simple de recomendación basado en compras de usuarios similares"""
    
    def __init__(self):
        # compras[usuario] = set de productos que compró
        self.compras = defaultdict(set)
        # compradores[producto] = set de usuarios que lo compraron
        self.compradores = defaultdict(set)
    
    def addPurchase(self, usuario, producto):
        """
        Registra una compra de un usuario
        
        Complejidad: O(1)
        """
        self.compras[usuario].add(producto)
        self.compradores[producto].add(usuario)
    
    def getRecommendations(self, usuario, n=5):
        """
        Retorna productos recomendados para el usuario
        
        Algoritmo:
        1. Obtener productos del usuario
        2. Para cada producto, encontrar otros usuarios que lo compraron
        3. Recopilar productos de esos usuarios
        4. Excluir productos ya comprados
        5. Ordenar por frecuencia
        
        Complejidad: O(p * u * q) donde:
            p = productos del usuario
            u = usuarios por producto
            q = productos por usuario
        
        Args:
            usuario: ID del usuario
            n: cantidad de recomendaciones a retornar
            
        Returns:
            lista de productos recomendados
        """
        productos_usuario = self.compras[usuario]
        recomendaciones = defaultdict(int)
        
        # Para cada producto que compró el usuario
        for producto in productos_usuario:
            # Encontrar usuarios que también lo compraron
            for otro_usuario in self.compradores[producto]:
                if otro_usuario != usuario:
                    # Agregar productos de ese usuario
                    for otro_producto in self.compras[otro_usuario]:
                        if otro_producto not in productos_usuario:
                            recomendaciones[otro_producto] += 1
        
        # Ordenar por frecuencia (más comprado = más recomendado)
        return sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)[:n]


# ============================================================================
# DEMOSTRACIÓN
# ============================================================================

if __name__ == "__main__":
    sistema = SistemaRecomendacion()
    
    print("="*70)
    print("SISTEMA DE RECOMENDACIÓN DE PRODUCTOS")
    print("="*70)
    
    # Registrar compras
    print("\n1. Registrando compras:")
    compras = [
        ("Juan", "Laptop"),
        ("Juan", "Mouse"),
        ("Juan", "Teclado"),
        ("Maria", "Laptop"),
        ("Maria", "Monitor"),
        ("Maria", "Teclado"),
        ("Pedro", "Mouse"),
        ("Pedro", "Teclado"),
        ("Pedro", "Auriculares"),
        ("Ana", "Laptop"),
        ("Ana", "Mouse"),
        ("Ana", "Monitor"),
        ("Luis", "Monitor"),
        ("Luis", "Auriculares"),
        ("Luis", "Webcam"),
    ]
    
    for usuario, producto in compras:
        sistema.addPurchase(usuario, producto)
        print(f"   {usuario} compró {producto}")
    
    # Mostrar compras de cada usuario
    print("\n2. Compras por usuario:")
    for usuario in ["Juan", "Maria", "Pedro", "Ana", "Luis"]:
        productos = sistema.compras[usuario]
        print(f"   {usuario}: {sorted(productos)}")
    
    # Generar recomendaciones
    print("\n3. Recomendaciones:")
    for usuario in ["Juan", "Maria", "Pedro"]:
        recomendaciones = sistema.getRecommendations(usuario, n=3)
        print(f"\n   Para {usuario}:")
        print(f"   Compró: {sorted(sistema.compras[usuario])}")
        if recomendaciones:
            print(f"   Recomendaciones:")
            for producto, score in recomendaciones:
                print(f"     - {producto} (score: {score})")
        else:
            print(f"   Sin recomendaciones")
    
    print("\n" + "="*70)
