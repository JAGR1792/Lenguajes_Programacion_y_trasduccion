#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Estados del AFD (Q). Los nombres son los que explicas en la exposición.
typedef enum {
    ESTADO_INICIAL,
    ESTADO_ID_ACEPTADO,
    ESTADO_ID_ESPERA_DIGITO,
    ESTADO_SUMA,
    ESTADO_INCREMENTO,
    ESTADO_ENTERO,
    ESTADO_RECHAZO,
    CANTIDAD_ESTADOS
} Estado;

// Símbolos del alfabeto Σ (en categorías, no char por char).
typedef enum {
    S_UPPER,
    S_LOWER,
    S_DIGIT,
    S_PLUS,
    S_OTHER,
    S_COUNT
} Simbolo;

// δ (delta): función de transición del AFD.
// DELTA[estado_actual][simbolo] = estado_siguiente
static const Estado DELTA[CANTIDAD_ESTADOS][S_COUNT] = {
    [ESTADO_INICIAL] = {
        [S_UPPER] = ESTADO_ID_ACEPTADO,
        [S_LOWER] = ESTADO_ID_ACEPTADO,
        [S_DIGIT] = ESTADO_ENTERO,
        [S_PLUS] = ESTADO_SUMA,
        [S_OTHER] = ESTADO_RECHAZO
    },
    [ESTADO_ID_ACEPTADO] = {
        [S_UPPER] = ESTADO_RECHAZO,
        [S_LOWER] = ESTADO_ID_ESPERA_DIGITO,
        [S_DIGIT] = ESTADO_RECHAZO,
        [S_PLUS] = ESTADO_RECHAZO,
        [S_OTHER] = ESTADO_RECHAZO
    },
    [ESTADO_ID_ESPERA_DIGITO] = {
        [S_UPPER] = ESTADO_RECHAZO,
        [S_LOWER] = ESTADO_RECHAZO,
        [S_DIGIT] = ESTADO_ID_ACEPTADO,
        [S_PLUS] = ESTADO_RECHAZO,
        [S_OTHER] = ESTADO_RECHAZO
    },
    [ESTADO_SUMA] = {
        [S_UPPER] = ESTADO_RECHAZO,
        [S_LOWER] = ESTADO_RECHAZO,
        [S_DIGIT] = ESTADO_RECHAZO,
        [S_PLUS] = ESTADO_INCREMENTO,
        [S_OTHER] = ESTADO_RECHAZO
    },
    [ESTADO_INCREMENTO] = {
        [S_UPPER] = ESTADO_RECHAZO,
        [S_LOWER] = ESTADO_RECHAZO,
        [S_DIGIT] = ESTADO_RECHAZO,
        [S_PLUS] = ESTADO_RECHAZO,
        [S_OTHER] = ESTADO_RECHAZO
    },
    [ESTADO_ENTERO] = {
        [S_UPPER] = ESTADO_RECHAZO,
        [S_LOWER] = ESTADO_RECHAZO,
        [S_DIGIT] = ESTADO_RECHAZO,
        [S_PLUS] = ESTADO_RECHAZO,
        [S_OTHER] = ESTADO_RECHAZO
    },
    [ESTADO_RECHAZO] = {
        [S_UPPER] = ESTADO_RECHAZO,
        [S_LOWER] = ESTADO_RECHAZO,
        [S_DIGIT] = ESTADO_RECHAZO,
        [S_PLUS] = ESTADO_RECHAZO,
        [S_OTHER] = ESTADO_RECHAZO
    }
};

// F: estados finales. Si termino en uno de estos, la cadena se acepta.
static int es_estado_final(Estado estado) {
    return estado == ESTADO_ID_ACEPTADO || estado == ESTADO_SUMA || estado == ESTADO_INCREMENTO || estado == ESTADO_ENTERO;
}

// Esta función clasifica un char real en una categoría del alfabeto.
// O sea, esto es pa que el autómata trabaje por clases de símbolo.
static Simbolo clasificar(unsigned char c) {
    if (c >= 'A' && c <= 'Z') {
        return S_UPPER;
    }
    if (c >= 'a' && c <= 'z') {
        return S_LOWER;
    }
    if (c >= '0' && c <= '9') {
        return S_DIGIT;
    }
    if (c == '+') {
        return S_PLUS;
    }
    return S_OTHER;
}

// Corre el AFD completo sobre una cadena.
int acepta(const char *cadena) {
    // Arrancamos en q0.
    Estado estado = ESTADO_INICIAL;
    // Recorremos la cadena símbolo por símbolo aplicando δ.
    for (size_t i = 0; cadena[i] != '\0'; i++) {
        Simbolo simbolo = clasificar((unsigned char)cadena[i]);
        estado = DELTA[estado][simbolo];
    }
    // Si el último estado es final, acepta.
    return es_estado_final(estado);
}

int main(int argc, char *argv[]) {
    // Ruta por argumento o archivo.txt por defecto.
    const char *ruta = (argc > 1) ? argv[1] : "archivo.txt";
    FILE *archivo = fopen(ruta, "r");
    char cadena[1024];
    // Bandera pa saber si el archivo traía al menos una línea.
    int hay_lineas = 0;

    if (archivo == NULL) {
        // Si no abre, devolvemos lo que pide el enunciado.
        printf("No Acepta\n");
        return 0;
    }

    // Recorremos TODO el archivo línea por línea.
    while (fgets(cadena, sizeof(cadena), archivo) != NULL) {
        hay_lineas = 1;
        // Quitamos solo salto de línea final.
        cadena[strcspn(cadena, "\r\n")] = '\0';
        if (acepta(cadena)) {
            printf("Acepta\n");
        } else {
            printf("No Acepta\n");
        }
    }

    fclose(archivo);

    // Archivo vacío => no hay nada aceptable.
    if (!hay_lineas) {
        printf("No Acepta\n");
    }

    return 0;
}
