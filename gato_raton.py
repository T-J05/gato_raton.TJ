import random
import time

# Tamaño del tablero
tamanho_tablero = 6

# Creación de la tabla
tablero = [["." for _ in range(tamanho_tablero)] for _ in range(tamanho_tablero)]

# Posiciones iniciles del gato y el ratón y salida
posicion_gato1 = (5, 5)
posicion_raton1 = (0 , 0)
random_nrgato = random.randint(1,5)
random_nrraton = random.randint(1,5)




# Función para pasar la tabla "en limpio"
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función para actualizar el tablero
def actualizar_tablero( posicion_raton1, posicion_gato1):
    tablero = [["." for _ in range(tamanho_tablero)]for _ in range(tamanho_tablero)]

    # Ubicamos al gato y al ratón del tablero #accedemos a las filas y a las columnas de ambos
    tablero[posicion_raton1[0]] [posicion_raton1 [1]] = "R"  
    tablero[posicion_gato1[0]][posicion_gato1[1]] = "G"
    

    # Llamamos a la función que limpia e imprime el tablero
    imprimir_tablero(tablero)



    # Hacemos un print de linea para que sea vea mas pulcro
    print()

# Función para obtener las posiciones
def obtener_posibles_movimientos(tamanho_tablero ,posicion):
    x , y =posicion
    movimientos = []

    if x > 0:  #mayor a cero
        movimientos.append((x - 1 , y)) # arriba

    if x < tamanho_tablero - 1: #menor a
        movimientos.append((x + 1 , y)) # abajo

    if y > 0: #mayor a cero 
        movimientos.append((x , y - 1)) # izquierda

    if y < tamanho_tablero - 1: #menor a 
        movimientos.append((x , y + 1)) # derecha

    return movimientos

    


cont = 0 #contador para saber las cantidades de turnos 
def evaluacion (posicion_gato,posicion_raton):
    #calculamos las distancias Manhattan
    distancia_entre_gyr = abs(posicion_gato[0]- posicion_raton [0]) + abs(posicion_gato [1] - posicion_raton[1]) 
    
    return distancia_entre_gyr 



def minimax(posicion_gato, posicion_raton, profundidad, turno ):
    if profundidad == 0 or posicion_raton == posicion_gato :
        return evaluacion(posicion_gato, posicion_raton )

    if turno == 'Gato':
        mejor_valor = float('inf')
        for movimiento in obtener_posibles_movimientos(tamanho_tablero, posicion_gato):
            valor = minimax(movimiento, posicion_raton, profundidad - 1, 'Raton' )
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

    if turno == 'Raton':
        mejor_valor = float('-inf')
        for movimiento in obtener_posibles_movimientos(tamanho_tablero, posicion_raton):
            valor = minimax(posicion_gato, movimiento, profundidad - 1, 'Gato' )
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor

def movimiento_gato(tamanho_tablero, posicion_gato, posicion_raton):
    if posicion_raton[0] == posicion_gato[0] or posicion_raton[1] == posicion_gato[1]:
        # Si el ratón y el gato están en la misma fila o columna, el gato se mueve hacia el ratón
        if posicion_raton[0] == posicion_gato[0]:
            # Mismo fila, mover en la columna
            if posicion_raton[1] > posicion_gato[1]:
                return (posicion_gato[0], posicion_gato[1] + 1)

            else:
                return (posicion_gato[0], posicion_gato[1] - 1)
        else:
            # Mismo columna, mover en la fila
            if posicion_raton[0] > posicion_gato[0]:
                return (posicion_gato[0] + 1, posicion_gato[1])
            else:
                return (posicion_gato[0] - 1, posicion_gato[1])
    else:
        # Si no están en la misma fila o columna, aplicamos el algoritmo minimax
        mjr_mov = None 
        mjr_valor = float("inf")
        for movimiento in obtener_posibles_movimientos(tamanho_tablero, posicion_gato):
            valor = minimax(movimiento, posicion_raton, random_nrgato, 'Gato')
            if valor < mjr_valor:
                mjr_valor = valor
                mjr_mov = movimiento
        return mjr_mov

def movimiento_raton(tamanho_tablero, posicion_gato, posicion_raton):
    mjr_mov = None 
    mjr_valor = float("-inf")
    for movimiento in obtener_posibles_movimientos(tamanho_tablero, posicion_raton):
        valor = minimax(posicion_gato, movimiento, random_nrraton, 'Raton')
        if valor > mjr_valor:
            mjr_valor = valor
            mjr_mov = movimiento
    return mjr_mov



posicion_gato = posicion_gato1
posicion_raton = posicion_raton1
actualizar_tablero (posicion_raton,posicion_gato)
tiempo = 1
# Bucle para el juego principal 
while True:
    posicion_gato = movimiento_gato (tamanho_tablero,posicion_gato,posicion_raton)
    actualizar_tablero(posicion_raton, posicion_gato)
    if posicion_gato == posicion_raton:
        print ('el gato a atrapado al raton')
        break 
     # Verificar si el gato está adyacente al ratón
    if abs(posicion_gato[0] - posicion_raton[0]) <= 1 and abs(posicion_gato[1] - posicion_raton[1]) <= 1:
        print("¡El gato ha acorralado al ratón!")
        break  # Terminar el juego
    actualizar_tablero(posicion_raton , posicion_gato)
    
    time.sleep (tiempo)

    posicion_raton = movimiento_raton (tamanho_tablero,posicion_gato,posicion_raton)
    actualizar_tablero (posicion_raton,posicion_gato)

    if posicion_gato == posicion_raton:
        print ('el gato a atrapado al raton')
        break 
   
    actualizar_tablero(posicion_raton , posicion_gato)
    
    time.sleep (tiempo)


    cont +=1
    if cont == 10:
        print('el raton escapo')
        break
    
    