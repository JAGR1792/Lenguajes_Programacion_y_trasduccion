# Diagrama de Flujo - Sistema de Navegación Web

## Método: loadPage(url)

```
INICIO
  │
  ├─ ¿url está vacío?
  │   │
  │   ├─ SÍ → Lanzar error "url no puede estar vacío"
  │   │
  │   └─ NO → Continuar
  │
  ├─ ¿Existe página actual?
  │   │
  │   ├─ SÍ → Agregar actual a pila_atras
  │   │
  │   └─ NO → Continuar
  │
  ├─ Establecer actual = url
  │
  ├─ Limpiar pila_adelante
  │
FIN
```

## Método: goBack()

```
INICIO
  │
  ├─ ¿pila_atras está vacía?
  │   │
  │   ├─ SÍ → Retornar None (no hay páginas anteriores)
  │   │
  │   └─ NO → Continuar
  │
  ├─ ¿Existe página actual?
  │   │
  │   ├─ SÍ → Agregar actual a pila_adelante
  │   │
  │   └─ NO → Continuar
  │
  ├─ Sacar última página de pila_atras
  │
  ├─ Establecer esa página como actual
  │
  ├─ Retornar actual
  │
FIN
```

## Método: goForward()

```
INICIO
  │
  ├─ ¿pila_adelante está vacía?
  │   │
  │   ├─ SÍ → Retornar None (no hay páginas siguientes)
  │   │
  │   └─ NO → Continuar
  │
  ├─ ¿Existe página actual?
  │   │
  │   ├─ SÍ → Agregar actual a pila_atras
  │   │
  │   └─ NO → Continuar
  │
  ├─ Sacar última página de pila_adelante
  │
  ├─ Establecer esa página como actual
  │
  ├─ Retornar actual
  │
FIN
```

## Diagrama de Estados del Sistema

```
Estado Inicial: actual = None, pila_atras = [], pila_adelante = []

[loadPage("A")]
→ Estado: actual = "A", pila_atras = [], pila_adelante = []

[loadPage("B")]
→ Estado: actual = "B", pila_atras = ["A"], pila_adelante = []

[loadPage("C")]
→ Estado: actual = "C", pila_atras = ["A", "B"], pila_adelante = []

[goBack()]
→ Estado: actual = "B", pila_atras = ["A"], pila_adelante = ["C"]

[goBack()]
→ Estado: actual = "A", pila_atras = [], pila_adelante = ["B", "C"]

[goForward()]
→ Estado: actual = "B", pila_atras = ["A"], pila_adelante = ["C"]

[loadPage("D")]
→ Estado: actual = "D", pila_atras = ["A", "B"], pila_adelante = []
   (Nota: pila_adelante se limpia al cargar nueva página)
```
