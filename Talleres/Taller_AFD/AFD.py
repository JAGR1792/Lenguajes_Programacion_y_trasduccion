import sys

def AFD(cadena):

    estados = {'q1', 'q2', 'q3'} 
    alfabeto = ('0', '1')
    
    F_transiciones = {
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q2', '1': 'q2'},
        'q3': {'0': 'q3', '1': 'q3'}
    }
    
    estado_inicial = 'q1'
    estados_finales = {'q2'} # el q3 no nos sirve pa nada, es un estado de rechazo

    

    #Recorremos caracter por caracter
    estado_actual = estado_inicial
    for simbolo in cadena:
        
        estado_actual = F_transiciones[estado_actual][simbolo]

    # Verificar si el estado final es de aceptación, ternarios porque tengo que demostrar que represento a la U en competencias de programación
    return "aceptado" if estado_actual in estados_finales else "No aceptado"
   

if __name__ == "__main__":
    if len(sys.argv) != 2: # En geeksforgeeks dice que es porque acepta 2 elementos, lo que seria el AFD.py y el archivo de texto de entrada.
        sys.exit(1)

    archivo_entrada = sys.argv[1] # Esta línea de código toma el segundo argumento que se pasó al ejecutar el script desde la terminal y lo guarda en la variable archivo_entrada

    try:
        with open(archivo_entrada, 'r') as f:
            for linea in f:
                cadena = linea.strip()
                if cadena:
                    resultado = AFD(cadena)
                    print(f"Cadena '{cadena}': {resultado}")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
        sys.exit(1)