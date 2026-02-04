class navegadorWeb:
    def __init__(self) -> None:
        self.pila_atras = []
        self.pila_adelante = []
        self.actual = None

    def loadPage(self, url: str) -> None:
        if not url:
            raise ValueError("url no puede estar vacío")
        if self.actual is not None:
            self.pila_atras.append(self.actual)
        self.actual = url
        self.pila_adelante.clear()

    def goBack(self):
        if not self.pila_atras:
            return None
        if self.actual is not None:
            self.pila_adelante.append(self.actual)
        self.actual = self.pila_atras.pop()
        return self.actual

    def goForward(self):
        if not self.pila_adelante:
            return None
        if self.actual is not None:
            self.pila_atras.append(self.actual)
        self.actual = self.pila_adelante.pop()
        return self.actual

    def VentanaActual(self):
        return self.actual


if __name__ == "__main__":
    navegador = navegadorWeb()
    navegador.loadPage("https://ejemplo.com")
    navegador.loadPage("https://ejemplo.com/sobre")
    navegador.loadPage("https://ejemplo.com/contacto")
    print("Actual:", navegador.VentanaActual())
    navegador.goBack()
    print("Atrás:", navegador.VentanaActual())
    navegador.goForward()
    print("Adelante:", navegador.VentanaActual())
