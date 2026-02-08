"""Interfaz de usuario y conversiones de entrada/salida."""

from operaciones_bits import restar_4_bits_complemento_a_dos, sumar_4_bits


def leer_bits(texto):
	"""Convierte una cadena binaria de 4 bits en lista de enteros 0/1."""
	if len(texto) != 4 or any(ch not in "01" for ch in texto):
		raise ValueError("Ingrese un numero binario de 4 bits (ej: 0101).")
	return [1 if ch == "1" else 0 for ch in texto]


def bits_a_texto(bits):
	"""Convierte una lista de bits en cadena binaria de 4 caracteres."""
	return "".join("1" if b else "0" for b in bits)


def bits_a_decimal(bits):
	"""Convierte una lista de bits a decimal usando base 2."""
	return int(bits_a_texto(bits), 2)


def formato_bin_decimal(bits):
	"""Devuelve una cadena con binario y decimal en un mismo formato."""
	return f"{bits_a_texto(bits)} ({bits_a_decimal(bits)})"


def decimal_a_entero(texto):
	"""Convierte una cadena decimal a entero usando int(). necesito el manejo así porque el programa es interactivo y no puedo asumir que el usuario siempre ingresará un número válido."""
	try:
		valor = int(texto)
	except ValueError as exc:
		raise ValueError("Ingrese un numero decimal valido (0 a 15).") from exc
	if valor < 0 or valor > 15:
		raise ValueError("El numero debe estar entre 0 y 15.")
	return valor


def decimal_a_bits(valor):
	"""Convierte un entero 0..15 a lista de 4 bits."""
	bits = [0, 0, 0, 0]
	for i in range(3, -1, -1):
		bits[i] = valor % 2
		valor //= 2
	return bits


def leer_entrada(formato, texto):
	"""Lee entrada en formato binario o decimal y devuelve lista de bits."""
	if formato == "B":
		return leer_bits(texto)
	valor = decimal_a_entero(texto)
	return decimal_a_bits(valor)


def mostrar_ejemplos():
	"""Ejecuta casos de prueba para ilustrar suma y resta."""
	ejemplos = [
		("S", "0011", "0101"),
		("S", "1111", "0001"),
		("R", "1000", "0011"),
		("R", "0010", "0100"),
	]
	print("Ejemplos automaticos:")
	for operacion, a_txt, b_txt in ejemplos:
		a_bits = leer_bits(a_txt)
		b_bits = leer_bits(b_txt)
		if operacion == "S":
			resultado, acarreo = sumar_4_bits(a_bits, b_bits)
			print(
				f"  {a_txt} + {b_txt} = {bits_a_texto(resultado)} "
				f"({bits_a_decimal(resultado)}) (carry={acarreo})"
			)
		else:
			resultado, acarreo = restar_4_bits_complemento_a_dos(a_bits, b_bits)
			print(
				f"  {a_txt} - {b_txt} = {bits_a_texto(resultado)} "
				f"({bits_a_decimal(resultado)}) (prestamo={acarreo})"
			)


def ejecutar_interactivo():
	"""Solicita datos al usuario y muestra el resultado."""
	opcion = input("Operacion (S=suma, R=resta): ").strip().upper()
	if opcion not in ("S", "R"):
		print("Operacion invalida.")
		return

	formato = input("Formato (B=binario, D=decimal): ").strip().upper()
	if formato not in ("B", "D"):
		print("Formato invalido.")
		return

	try:
		if formato == "B":
			a_texto = input("A (4 bits): ").strip()
			b_texto = input("B (4 bits): ").strip()
		else:
			a_texto = input("A (0 a 15): ").strip()
			b_texto = input("B (0 a 15): ").strip()
		a_bits = leer_entrada(formato, a_texto)
		b_bits = leer_entrada(formato, b_texto)
		if formato == "D":
			a_valor = decimal_a_entero(a_texto)
			b_valor = decimal_a_entero(b_texto)
			print("A en binario:", bin(a_valor)[2:].zfill(4))
			print("B en binario:", bin(b_valor)[2:].zfill(4))
	except ValueError as exc:
		print(exc)
		return

	if opcion == "S":
		resultado, acarreo = sumar_4_bits(a_bits, b_bits)
		print("A:", formato_bin_decimal(a_bits))
		print("B:", formato_bin_decimal(b_bits))
		print("Resultado:", formato_bin_decimal(resultado))
		print("Carry:", acarreo)
	else:
		resultado, acarreo = restar_4_bits_complemento_a_dos(a_bits, b_bits)
		print("A:", formato_bin_decimal(a_bits))
		print("B:", formato_bin_decimal(b_bits))
		print("Resultado:", formato_bin_decimal(resultado))
		print("Prestamo (0=negativo):", acarreo)


def ejecutar_programa():
	"""Punto de inicio: imprime encabezado, ejemplos y modo interactivo."""
	print("Sumador y restador de 4 bits")
	
	mostrar_ejemplos()
	print("Ahora puedes probar con tus propios valores.")
	ejecutar_interactivo()
