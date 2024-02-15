from typing import Tuple

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.izquierda = None
        self.derecha = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_aux(valor, self.raiz)

    def _insertar_aux(self, valor, nodo_actual):
        if valor <= nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
                nodo_actual.izquierda.padre = nodo_actual
            else:
                self._insertar_aux(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
                nodo_actual.derecha.padre = nodo_actual
            else:
                self._insertar_aux(valor, nodo_actual.derecha)

    def buscar(self, valor):
        return self._buscar_aux(valor, self.raiz)

    def _buscar_aux(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar_aux(valor, nodo_actual.izquierda)
        return self._buscar_aux(valor, nodo_actual.derecha)

    def preorden(self):
        return self._preorden_aux(self.raiz, "")
    
    def _preorden_aux(self, nodo_actual, transversal):
        if nodo_actual is not None:
            transversal += str(nodo_actual.valor) + ", "
            transversal = self._preorden_aux(nodo_actual.izquierda, transversal)
            transversal = self._preorden_aux(nodo_actual.derecha, transversal)
        return transversal
    
    def inorden(self):
        return self._inorden_aux(self.raiz, "")
    
    def _inorden_aux(self, nodo_actual, transversal):
        if nodo_actual is not None:
            transversal = self._inorden_aux(nodo_actual.izquierda, transversal)
            transversal += str(nodo_actual.valor) + ", "
            transversal = self._inorden_aux(nodo_actual.derecha, transversal)
        return transversal

    def postorden(self):
        return self._postorden_aux(self.raiz, "")
    
    def _postorden_aux(self, nodo_actual, transversal):
        if nodo_actual is not None:
            transversal = self._postorden_aux(nodo_actual.izquierda, transversal)
            transversal = self._postorden_aux(nodo_actual.derecha, transversal)
            transversal += str(nodo_actual.valor) + ", "
        return transversal
    
def funcion_cuentamontvalles(recorrido: str) -> Tuple[int, int]:
    """
        Función que cuenta la cantidad de montañas y valles en una cadena.
        Estos son 'U' (up) y 'D' (down). Además suponemos que comenzamos sobre el nivel del mar.

        Args:
            recorrido (str)

        Returns:
            Tuple[int, int] : montañas, valles
    """
    nivel = 0
    montanias = 0
    valles = 0
    for paso in recorrido:
        if paso == "U":
            nivel += 1
        else:
            nivel -= 1
        if nivel == 0 and paso == "U":
            valles += 1
        if nivel == 0 and paso == "D":
            montanias += 1
    return montanias, valles
    
if __name__ == "__main__":

    print("--------------------------------------------------------------------------")
    print("\t\t  Ejercicio 1. Cuenta Montañas y Valles")
    print("--------------------------------------------------------------------------")
    recorrido = "UDDDUDUUUDUUD"
    print("Recorrido:", recorrido)
    cuenta = funcion_cuentamontvalles(recorrido)
    print("Montañas:", cuenta[0])
    print("Valles:", cuenta[1])

    print("--------------------------------------------------------------------------")
    print("\t\t   Ejercicio 2. Arbol Binario Ordenado")
    print("--------------------------------------------------------------------------")
    arbol1 = ArbolBinarioOrdenado()

    # Insertamos valores al árbol recibiendo una lista.

    valores = [5, 3, 7, 2, 4, 6, 8]
    print("Valores a insertar en el árbol uno:", valores)
    for valor in valores:
       arbol1.insertar(valor)
    print("Preorden:", arbol1.preorden())
    print("Inorden:", arbol1.inorden())
    print("Postorden:", arbol1.postorden())

    print("Buscando el valor 3:", arbol1.buscar(3).valor if arbol1.buscar(3) else "No se encontró el valor 3")
    print("Buscando el valor 8:", arbol1.buscar(8).valor if arbol1.buscar(8) else "No se encontró el valor 8")
    print("Buscando el valor 10:", arbol1.buscar(10).valor if arbol1.buscar(10) else "No se encontró el valor 10")
    print("Buscando el valor 1:", arbol1.buscar(1).valor if arbol1.buscar(1) else "No se encontró el valor 1")


    arbol2 = ArbolBinarioOrdenado()
    valores = [10, 5, 16, 2, 8, 19, 18, 9]
    print("\nValores a insertar en el árbol dos:", valores)
    for valor in valores:
       arbol2.insertar(valor)
    print("Preorden:", arbol2.preorden())
    print("Inorden:", arbol2.inorden())
    print("Postorden:", arbol2.postorden())

    print("Buscando el valor 3:", arbol2.buscar(3).valor if arbol2.buscar(3) else "No se encontró el valor 3")
    print("Buscando el valor 8:", arbol2.buscar(8).valor if arbol2.buscar(8) else "No se encontró el valor 8")
    print("Buscando el valor 10:", arbol2.buscar(10).valor if arbol2.buscar(10) else "No se encontró el valor 10")
    print("Buscando el valor 19:", arbol2.buscar(19).valor if arbol2.buscar(19) else "No se encontró el valor 19")