def inicia_emulacion():
    """
        Emulación de un marcador de tenis.
    """
    print("-------------------------------------------------")
    print("Hola, este es un emulador de un marcador de tenis")
    print("-------------------------------------------------")
    print("Inserta el nombre de los jugadores")    
    msjError = "La entrada no es válida, vuelve a intentarlo"

    jugador1 = __obten_entrada_valida(__verifica_entrada, "Jugador 1: ", msjError)

    jugador2 = __obten_entrada_valida(__verifica_entrada, "Jugador 2: ", msjError)

    print("Los jugadores a competir son: ", jugador1, " y ", jugador2)

    print("< ------------------------------------------------- >")
    print("Inicio del juego")
    jugador_saque = __obtener_saqueA(jugador1, jugador2)
    print("El jugador que inicia el saque será: ", jugador_saque)
    sets_jugador1 = 0
    sets_jugador2 = 0
    sets = 1
    resultados = []
    while sets <= 3:
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("Set ", sets)
        pointset_jugador1 = 0
        pointset_jugador2 = 0

        while (pointset_jugador1 < 6 and pointset_jugador2 < 6) or abs(pointset_jugador1 - pointset_jugador2) < 2:
            puntaje_jugador1 = 0
            puntaje_jugador2 = 0
            deuce = False
            cambiosaque = False
            while puntaje_jugador1 < 5 and puntaje_jugador2 < 5 and not cambiosaque:
                print("\tJugador ", jugador_saque, " saca")

                jugadorG = __obten_entrada_valida((lambda x: x.replace(" ", "") == "" or not(x.isdigit()) or (int(x) > 2 or int(x) < 0)),
                                                  "Punto para el jugador (1 ó 2): ", msjError)

                if jugadorG == "1":
                    puntaje_jugador1 += 1
                else:
                    puntaje_jugador2 += 1

                if puntaje_jugador1 == 4 and puntaje_jugador2 == 4 and deuce:
                    puntaje_jugador1 = 3
                    puntaje_jugador2 = 3
                elif puntaje_jugador1 > 4 or puntaje_jugador2 > 4:
                    deuce = False

                if (puntaje_jugador1 >= 4 or puntaje_jugador2 >= 4) and not(deuce):
                    cambiosaque = True
                else:
                    print("Puntaje: ", jugador1, " ", __interpreta_puntaje(puntaje_jugador1), " - ",
                          __interpreta_puntaje(puntaje_jugador2), " ", jugador2)

                if puntaje_jugador1 == 3 and puntaje_jugador2 == 3:
                    deuce = True
            
            if puntaje_jugador1 > puntaje_jugador2:
                pointset_jugador1 += 1
            else:
                pointset_jugador2 += 1

            print("Puntaje actual del set", sets, ": ", jugador1, " ", pointset_jugador1, " - ",
                  pointset_jugador2, " ", jugador2)
            jugador_saque = (jugador2 if jugador_saque == jugador1 else jugador1)
            print("\tCambio de saque")

            if (pointset_jugador1 + pointset_jugador2) % 2 == 1:
                print("Cambio de cancha")

        # Agregamos las estadísticas del set
        resultados.append([pointset_jugador1, pointset_jugador2])

        if pointset_jugador1 > pointset_jugador2:
            sets_jugador1 += 1
        else:
            sets_jugador2 += 1
        
        print("Fin del set ", sets)

        if sets_jugador1 == 2 or sets_jugador2 == 2:
            break        

        sets += 1

    print("El ganador es: ", jugador1 if sets_jugador1 > sets_jugador2 else jugador2)

    print("Resumen del juego")
    for i in range(len(resultados)):
        print("Set ", i + 1, ": ", jugador1, " ", resultados[i][0], " - ", resultados[i][1], " ", jugador2)
        
    print("Fin del juego")
    print("< ------------------------------------------------- >")
        

def __obten_entrada_valida(funcion, msjEntrada ,msjError):
    """
        Abre la entrada en terminal y a partir de una función evalúa su validez. Si el formato de entrada no es válido, se pide de
        nuevo escribir algo.

        Args:
            funcion (function)
            msjEntrada (str)
            msjError (str)

        Returns:
            str : entrada
    """
    entrada = ""
    evaluando = True
    while evaluando:
        try:
            entrada = input(msjEntrada)
            if funcion(entrada):
                raise Exception(msjError)
        except Exception as e:
            print(e)
        else:
            evaluando = False
    return entrada

def __interpreta_puntaje(puntaje):
    """
        Interpreta el puntaje del jugador.

        Args:
            puntaje (int)

        Returns:
            str : "0", "15", "30", "40" o "AD"
    """
    if puntaje == 0:
        return "0"
    elif puntaje == 1:
        return "15"
    elif puntaje == 2:
        return "30"
    elif puntaje == 3:
        return "40"
    else:
        return "AD"

def __obtener_saqueA(jugador1, jugador2):
    """
        Obtiene el jugador que inicia el saque

        Args:
            jugador1 (str)
            jugador2 (str)

        Returns:
            str : jugador1 o jugador2
    """
    import random
    return random.choice([jugador1, jugador2])

def __verifica_entrada(entrada):
    """
        Verifica que la entrada sea correcta, siendo que no puede ser un entero o una cadena vacía (enter o espacio).

        Args:
            entrada (str)
    """
    if entrada.replace(" ", "").isdigit() or entrada.replace(" ", "") == "":
        return True
    else:
        return False

if __name__ == "__main__":
    inicia_emulacion()