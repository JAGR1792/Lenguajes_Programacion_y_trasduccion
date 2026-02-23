import sys
import os


# Estos son los tipos de símbolo que usamos pa simplificar el alfabeto.
# En vez de guardar cada char posible, lo metemos en una categoría.
SIMBOLOS = ("UPPER", "LOWER", "DIGIT", "PLUS", "OTHER")

# M = (Q, Σ, δ, q0, F)
# Q: conjunto de estados del AFD.
Q = (
    "q_inicial",
    "q_id_aceptado",
    "q_id_espera_digito",
    "q_suma",
    "q_incremento",
    "q_entero",
    "q_rechazo",
)
# Σ: alfabeto (acá representado por categorías de símbolo).
SIGMA = set(SIMBOLOS)
# q0: estado inicial.
Q0 = "q_inicial"
# F: estados de aceptación (si termino aquí, la cadena se acepta).
F = {"q_id_aceptado", "q_suma", "q_incremento", "q_entero"}

# δ: función de transición.
# Esta tabla dice: "si estoy en tal estado y leo tal símbolo, me voy a tal estado.
DELTA = {
    "q_inicial": {
        "UPPER": "q_id_aceptado",
        "LOWER": "q_id_aceptado",
        "DIGIT": "q_entero",
        "PLUS": "q_suma",
        "OTHER": "q_rechazo",
    },
    "q_id_aceptado": {
        "UPPER": "q_rechazo",
        "LOWER": "q_id_espera_digito",
        "DIGIT": "q_rechazo",
        "PLUS": "q_rechazo",
        "OTHER": "q_rechazo",
    },
    "q_id_espera_digito": {
        "UPPER": "q_rechazo",
        "LOWER": "q_rechazo",
        "DIGIT": "q_id_aceptado",
        "PLUS": "q_rechazo",
        "OTHER": "q_rechazo",
    },
    "q_suma": {
        "UPPER": "q_rechazo",
        "LOWER": "q_rechazo",
        "DIGIT": "q_rechazo",
        "PLUS": "q_incremento",
        "OTHER": "q_rechazo",
    },
    "q_incremento": {
        "UPPER": "q_rechazo",
        "LOWER": "q_rechazo",
        "DIGIT": "q_rechazo",
        "PLUS": "q_rechazo",
        "OTHER": "q_rechazo",
    },
    "q_entero": {
        "UPPER": "q_rechazo",
        "LOWER": "q_rechazo",
        "DIGIT": "q_rechazo",
        "PLUS": "q_rechazo",
        "OTHER": "q_rechazo",
    },
    "q_rechazo": {
        "UPPER": "q_rechazo",
        "LOWER": "q_rechazo",
        "DIGIT": "q_rechazo",
        "PLUS": "q_rechazo",
        "OTHER": "q_rechazo",
    },
}


def clasificar(caracter: str) -> str:
    # Esta función traduce un char real a una categoría del alfabeto.
    # O sea, esto es pa que el AFD no dependa de chars sueltos sino de clases.
    if "A" <= caracter <= "Z":
        return "UPPER"
    if "a" <= caracter <= "z":
        return "LOWER"
    if "0" <= caracter <= "9":
        return "DIGIT"
    if caracter == "+":
        return "PLUS"
    return "OTHER"


def acepta(cadena: str) -> bool:
    # Arrancamos siempre en q0 (estado inicial).
    estado = Q0
    # Recorremos la cadena char por char, aplicando δ cada vez.
    for caracter in cadena:
        simbolo = clasificar(caracter)
        estado = DELTA[estado][simbolo]
    # Si al final quedé en un estado final, acepta; si no, rechaza.
    return estado in F


def main() -> None:
    # Si me pasan ruta por consola, la uso; si no, uso archivo.txt por defecto.
    ruta = sys.argv[1] if len(sys.argv) > 1 else "archivo.txt"
    # Esto es pa no romperse si me pasan un nombre que no existe.
    if not os.path.exists(ruta):
        ruta = "archivo.txt"

    try:
        # Leemos TODO el archivo, línea por línea.
        with open(ruta, "r", encoding="utf-8") as archivo:
            hay_lineas = False
            for linea in archivo:
                hay_lineas = True
                # Solo quitamos salto de línea, no tocamos el contenido interno.
                cadena = linea.rstrip("\r\n")
                # Para cada línea imprimimos exactamente lo pedido.
                print("Acepta" if acepta(cadena) else "No Acepta")
    except OSError:
        # Si no se puede abrir el archivo, lo tomamos como no aceptado.
        print("No Acepta")
        return

    # Si el archivo está vacío, también reportamos no aceptación. por q no quiro hacer un try catch para eso, y es más fácil hacer esto que manejar el error de EOF.
    if not hay_lineas:
        print("No Acepta")


if __name__ == "__main__":
    main()
