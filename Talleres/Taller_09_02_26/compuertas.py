"""Compuertas logicas basicas para bits 0/1."""


def compuerta_and(a, b):
	"""Devuelve 1 si ambos bits son 1; en otro caso 0."""
	return 1 if (a and b) else 0


def compuerta_or(a, b):
	"""Devuelve 1 si al menos un bit es 1; en otro caso 0."""
	return 1 if (a or b) else 0


def compuerta_not(a):
	"""Invierte el bit: 1->0, 0->1."""
	return 0 if a else 1


def compuerta_xor(a, b):
	"""Construye XOR usando solo AND, OR y NOT."""
	return compuerta_and(compuerta_or(a, b), compuerta_not(compuerta_and(a, b)))

