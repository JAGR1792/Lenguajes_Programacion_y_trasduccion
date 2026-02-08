"""Operaciones aritmeticas de 4 bits construidas con compuertas logicas."""

from compuertas import compuerta_and, compuerta_not, compuerta_or, compuerta_xor


def sumador_completo(a, b, acarreo_entrada):
	"""Suma tres bits y devuelve (bit_suma, acarreo_salida)."""
	suma_1 = compuerta_xor(a, b)
	bit_suma = compuerta_xor(suma_1, acarreo_entrada)
	acarreo_salida = compuerta_or(
		compuerta_and(a, b), compuerta_and(acarreo_entrada, suma_1)
	)
	return bit_suma, acarreo_salida


def sumar_4_bits(a_bits, b_bits, acarreo_entrada=0):
	"""Suma dos arreglos de 4 bits con acarreo de entrada opcional."""
	resultado = [0, 0, 0, 0]
	acarreo = acarreo_entrada
	
	for i in range(3, -1, -1):
		resultado[i], acarreo = sumador_completo(a_bits[i], b_bits[i], acarreo)
	return resultado, acarreo


def complemento_a_uno(bits):
	"""Calcula el complemento a uno aplicando NOT a cada bit."""
	return [compuerta_not(b) for b in bits]


def restar_4_bits_complemento_a_dos(a_bits, b_bits):
	"""Resta A - B usando el complemento a dos de B."""
	b_complemento_uno = complemento_a_uno(b_bits)
	resultado, acarreo = sumar_4_bits(a_bits, b_complemento_uno, acarreo_entrada=1)
	return resultado, acarreo
