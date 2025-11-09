from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
'''
Ejercicio 1. Veterinaria - Stock
En la veterinaria ”Exactas’s pets”, al finalizar cada d´ıa, el personal registra en papeles los nombres y la cantidad actual de
los productos cuyo stock ha cambiado. Para mejorar la gesti´on, desde la direcci´on de la veterinaria han pedido desarrollar una
soluci´on en Python que les permita analizar las fluctuaciones del stock. Se pide implementar una funci´on, que reciba una lista
de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La funci´on debe procesar esta lista
y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su m´ınimo y m´aximo stock
hist´orico registrado.
problema stock productos (in stock cambios : seq⟨str × Z⟩) : dict⟨ZxZ⟩ {
requiere: {Todos los elementos de stock cambios est´an formados por un str no vac´ıo y un entero ≥ 0.}
asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese
producto en stock cambios y como segundo valor el mayor.}
}
'''
def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[tuple[int, int]]:
    res: dict[tuple[int, int]] = {}

    for producto, stock in stock_cambios:
        if producto not in res:
            res[producto] = (stock, stock)
        
        else:
            minimo: int = res[producto][0]
            maximo: int = res[producto][1]

            if stock < minimo:
                minimo = stock
            elif stock > maximo:
                maximo = stock
            res[producto] = (minimo, maximo)
        
    return res

stock_cambios: list[tuple[str, int]] = [("A",2), ("B",4), ("C",3), ("A",5)]
print(stock_productos(stock_cambios))


'''
Ejercicio 2. Veterinaria - Filtrar c´odigos de barra
El hijo del due˜no de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos c´odigos de barras
terminan en n´umeros primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre
de esta idea, solicita una funci´on en Python que facilite esta gesti´on. Se pide implementar una funci´on que, dada una secuencia de
enteros, cada uno representando un c´odigo de barras de un producto, cree y devuelva una nueva lista que contenga ´unicamente
aquellos n´umeros de la lista original cuyos ´ultimos tres d´ıgitos formen un n´umero primo (por ejemplo, 101, 002 y 011).
Nota: Un n´umero primo es aquel que solo es divisible por s´ı mismo y por 1. Algunos ejemplos de n´umeros primos de hasta
tres d´ıgitos son: 2, 3, 5, 101, 103, 107, etc.
problema filtrar codigos primos (in codigos barra : seq⟨Z⟩) : seq⟨Z⟩ {
requiere: {Todos los enteros de codigos barra tienen, por lo menos, 3 d´ıgitos.}
requiere: {No hay elementos repetidos en codigos barra.}
asegura: {Los ´ultimos 3 d´ıgitos de cada uno de los elementos de res forman un n´umero primo.}
asegura: {Todos los elementos de codigos barra cuyos ´ultimos 3 d´ıgitos forman un n´umero primo est´an en res.}
asegura: {Todos los elementos de res est´an en codigos barra.}
}
'''
def es_primo(numero: int) -> bool:
    if numero % 2 == 0:
        return False
    return True

def ultimos_tres_digitos(numero: int) -> int:
    return numero % 1000

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []

    for numero in codigos_barra:
        if es_primo(ultimos_tres_digitos(numero)):
            res.append(numero)
    
    return res

verificar = filtrar_codigos_primos([101, 102, 103])
print(verificar)


'''
Ejercicio 3. Veterinaria - Flujo de pacientes
Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando
al local. Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una funci´on en
Python que encuentre la secuencia m´as larga de consultas consecutivas que solo contenga los tipos de mascota ”perro” o ”gato”.
Se pide implementar una funci´on que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el
´ındice donde comienza la subsecuencia m´as larga que cumpla con estas condiciones.
problema subsecuencia mas larga (in tipos pacientes atendidos : seq⟨str⟩) : Z {
requiere: {tipos pacientes atendidos tiene, por lo menos, un elemento ”perro” o ”gato”.}
asegura: {res es el ´ındice donde empieza la subsecuencia m´as larga de tipos pacientes atendidos que contenga solo
elementos ”perro” o ”gato”.}
asegura: {Si hay m´as de una subsecuencia de tama˜no m´aximo, res tiene el ´ındice de la primera.}
}
'''
def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    indice_actual: int = 0
    longitud_actual: int = 0
    indice_inicio_max: int = 0
    longitud_max: int = 0

    for i in range(len(tipos_pacientes_atendidos)):
        tipo: str = tipos_pacientes_atendidos[i]
        if tipo == "perro" or tipo == "gato":
            if longitud_actual == 0:
                indice_actual = i
            longitud_actual += 1
        
        else:
            if longitud_actual > longitud_max:
                longitud_max = longitud_actual
                indice_inicio_max = indice_actual
            longitud_actual = 0

    if longitud_actual > longitud_max:
        longitud_max = longitud_actual
        indice_inicio_max = indice_actual

    return indice_inicio_max

verificar = subsecuencia_mas_larga(["loro", "perro", "gato", "gato", "conejo", "perro", "gato", "gato", "perro", "conejo"])
print(verificar)


'''
Ejercicio 4. Veterinaria - Tabla turnos
Las personas responsables de los turnos est´an anotadas en una matriz donde las columnas representan los d´ıas, en orden de
lunes a domingo, y cada fila un rango de una hora. Hay cuatro filas para los turnos de la ma˜nana (9, 10, 11 y 12 hs) y otras
cuatro para la tarde (14, 15, 16 y 17).
Para hacer m´as eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables,
est´an asignadas de manera continuada en los turnos de cada d´ıa.
Para ello se pide desarrollar una funci´on en Python que, dada la matriz de turnos, devuelva una lista de tuplas de bool, una
por cada d´ıa. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los
turnos de la ma˜nana para ese d´ıa son iguales entre s´ı. El segundo elemento debe ser True si y solo si todos los valores de los
turnos de la tarde para ese d´ıa son iguales entre s´ı.
Siempre hay una persona responsable en cualquier horario de la veterinaria.
problema un responsable por turno (in grilla horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool × Bool⟩ {
requiere: {|grilla horaria| = 8.}
requiere: {Todos los elementos de grilla horaria tienen el mismo tama˜no (mayor a 0 y menor 8).}
requiere: {No hay cadenas vac´ıas en las listas de grilla horaria.}
asegura: {|res| = |grilla horaria[0]|.}
asegura: {El primer valor de la tupla en res [i], con i:Z, 0 res| es igual a True los primeros 4 valores de la columna i de
grilla horaria son iguales entre s´ı.}
asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 res| es igual a True los ´ultimos 4 valores de la columna i de
grilla horaria son iguales entre s´ı.}
}
'''
def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool, bool]]:
    res: list[tuple[bool, bool]] = []
    cantidad_columnas: int = len(grilla_horaria[0])

    for j in range(0, cantidad_columnas):
        persona_mañana: str = grilla_horaria[0][j]
        todas_iguales_mañana: bool = True
        for fila in range(1, 4):
            if persona_mañana != grilla_horaria[fila][j]:
                todas_iguales_mañana = False
        
        persona_tarde: str = grilla_horaria[4][j]
        todas_iguales_tarde: bool = True
        for fila in range(5, 8):
            if persona_tarde != grilla_horaria[fila][j]:
                todas_iguales_tarde = False

        res.append((todas_iguales_mañana, todas_iguales_tarde))

    return res
grilla_horaria: list[list[str]] = [["ANA", "ANA", "ANA"],
                                   ["ANA", "ANA", "ANA"],
                                   ["ANA", "PEDRO", "ANA"],
                                   ["ANA", "ANA", "ANA"],
                                   ["JUAN", "JUAN", "JUAN"],
                                   ["JUAN", "JUAN", "JUAN"],
                                   ["JUAN", "JUAN", "PEDRO"],
                                   ["JUAN", "JUAN", "JUAN"]]

print(un_responsable_por_turno(grilla_horaria))


'''
Ejercicio 5. Sala de Escape - Promedio de salidas
Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de
una habitaci´on resolviendo enigmas, llevan un registro meticuloso de todas las salas de escape que hay en Capital. Este registro
indica si han visitado una sala y si pudieron o no salir de ella. Un 0 significa que no fueron, un 61 que no lograron salir a tiempo,
y un n´umero entre 1 y 60 representa los minutos que les tom´o escapar exitosamente. Con estos datos, pueden comparar sus
logros y desaf´ıos en cada nueva aventura que emprenden juntos.
Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados
para cada sala de escape en Capital, escribir una funci´on en Python que devuelva un diccionario. En este nuevo diccionario,
las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la cantidad de salas de las que cada
persona logr´o salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir).
problema promedio de salidas (in registro: dict<str, seq⟨Z⟩>) : dict<str, <Z×R>> {
requiere: {registro tiene por lo menos un integrante.}
requiere: {Todos los integrantes de registro tiene por lo menos un tiempo.}
requiere: {Todos los valores de registro tiene la misma longitud.}
requiere: {Todos los tiempos de los valores de registro est´an entre 0 y 61 inclusive.}
asegura: {res tiene las mismas claves que registro.}
asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a
0 y menor estricto a 61 que figuran en sus valores de registro.}
asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que sali´o es mayor a
0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino
es 0.0.}
}
'''
def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int, float]] = {}

    for amigo in registro.keys():
        tiempos: list[int] = registro[amigo]
        cant_salidas: int = 0
        suma_tiempos: int = 0

        for tiempo in tiempos:
            if tiempo > 0 and tiempo < 61:
                cant_salidas += 1
                suma_tiempos += tiempo

        if cant_salidas > 0:
            promedio: float = suma_tiempos / cant_salidas
        else:
            res[amigo] = 0.0               
        
        res[amigo] = (cant_salidas, promedio)
    
    return res

registro = {
    "Ana": [30, 45, 0, 70],        # 2 salidas válidas: promedio 37.5
    "Beto": [15, 20, 25, 10, 5],   # 5 salidas válidas: promedio 15.0
    "Carla": [0, 0, 0],            # Ninguna salida válida
    "Damián": [59, 60, 61, 58]     # 3 válidas (61 no cuenta): promedio 59.0
}

resultado = promedio_de_salidas(registro)
print("Resultado:", resultado)


'''
Ejercicio 6. Sala de Escape - Tiempo m´as r´apido
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una funci´on en Python
que devuelva la posici´on (´ındice) en la cual se encuentra el tiempo m´as r´apido, excluyendo las salas en las que no haya salido (0
o mayor a 60).
problema tiempo mas rapido (in tiempos salas: seq⟨Z⟩) : Z {
requiere: {Hay por lo menos un elemento en tiempos salas entre 1 y 60 inclusive.}
requiere: {Todos los tiempos en tiempos salas est´an entre 0 y 61 inclusive.}
asegura: {res es la posici´on de la sala en tiempos salas de la que m´as r´apido se sali´o (en caso que haya m´as de una,
devolver la primera, osea la de menor ´ındice).}
}
'''
def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    res: int = 0
    tiempo_minimo: int = 61

    for i in range(len(tiempos_salas)):
        tiempo: int = tiempos_salas[i]
        if tiempo > 0 and tiempo < 61:
            if tiempo < tiempo_minimo:
                tiempo_minimo = tiempo
                res = i

    return res

tiempos_salas: list[int] = [4,83,23,53,22,1]
print(tiempo_mas_rapido(tiempos_salas))


'''
Ejercicio 7. Sala de Escape - Racha m´as larga
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una
funci´on en Python que devuelva una tupla con el ´ındice de inicio y el ´ındice de fin de la subsecuencia m´as larga de salidas
exitosas de salas de escape consecutivas.
problema racha mas larga (in tiempos: seq⟨Z⟩) : <Z×Z> {
requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive.}
requiere: {Todos los tiempos en tiempos est´an entre 0 y 61 inclusive.}
asegura: {En la primera posici´on de res est´a la posici´on (´ındice de la lista) de la sala que inicia la racha m´as larga.}
asegura: {En la segunda posici´on de res est´a la posici´on (´ındice de la lista) de la sala que finaliza la racha m´as larga.}
asegura: {El elemento de la primer posici´on de res en tiempos es mayor estricto 0 y menor estricto que 61.}
asegura: {El elemento de la segunda posici´on de res en tiempos es mayor estricto 0 y menor estricto que 61.}
asegura: {La primera posici´on de res es menor o igual a la segunda posici´on de res.}
asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posici´on de res y la segunda posici´on de res.}
asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que est´a entre la primer
posici´on de res y la segunda posici´on de res.}
asegura: {Si hay dos o m´as subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera
de ellas.}
}
'''
def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    indice_inicio_max: int = 0
    longitud_max: int = 0
    indice_actual: int = 0
    longitud_actual: int = 0
    indice_fin_max: int = -1

    for i in range(len(tiempos)):
        tiempo: int = tiempos[i]
        if tiempo > 0 and tiempo < 61:
            if longitud_actual == 0:
                indice_actual = i
            longitud_actual += 1
        
        else:
            if longitud_actual > longitud_max:
                longitud_max = longitud_actual
                indice_inicio_max = indice_actual
                indice_fin_max = i - 1
            longitud_actual = 0
        
    if longitud_actual > longitud_max:
        longitud_max = longitud_actual
        indice_inicio_max = indice_actual
        indice_fin_max = len(tiempo) - 1

    return (indice_inicio_max, indice_fin_max)

verificar = racha_mas_larga([0, 45, 30, 61, 25, 15, 10, 61, 5])
print(verificar)


'''
Ejercicio 8. Sala de Escape - Escape en solitario
Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los
tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un n´umero entre 1 y 60 si salieron), escribir
una funci´on en Python que devuelva los ´ındices de todas las filas (que representan las salas) en las cuales el primer, segundo y
cuarto amigo no fueron (0), pero el tercero s´ı fue independientemente de si sali´o o no).
problema escape en solitario (in amigos por salas: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
requiere: {Hay por lo menos una sala en amigos por salas.}
requiere: {Hay 4 amigos en amigos por salas.}
requiere: {Todos los tiempos en cada sala de amigos por salas est´an entre 0 y 61 inclusive.}
asegura: {La longitud de res es menor igual que la longitud de amigos por salas.}
asegura: {Por cada sala en amigos por salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de
0, la posici´on de dicha sala en amigos por salas debe aparecer res.}
asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos por salas[i] es 0, y
el tercer valor es distinto de 0.}
}
'''
def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res: list[int] = []
    salas: int = len(amigos_por_salas)

    for i in range(salas):
        sala: list[int] = amigos_por_salas[i]
        if sala[0] == 0 and sala[1] == 0 and sala[2] != 0 and sala[3] == 0:
            res.append(i)
    
    return res
amigos_por_salas: list[list[int]] = [
    [0, 0, 5, 0],   # ✅ Solo el amigo 3 participó → índice 0
    [1, 0, 0, 0],   # No cumple (amigo 1 fue)
    [0, 0, 0, 0],   # No cumple (nadie fue)
    [0, 0, 12, 0],  # ✅ Solo el amigo 3 participó → índice 3
    [0, 4, 9, 0],   # No cumple (también fue el amigo 2)
]

resultado = escape_en_solitario(amigos_por_salas)
print("Salas en las que el amigo 3 fue solo:", resultado)


'''
Ejercicio 9. Juego de la Gallina
El juego del gallina es una competici´on en la que dos participantes conducen un veh´ıculo en direcci´on al del contrario; si
alguno se desv´ıa de la trayectoria de choque pierde y es humillado por comportarse como un ”gallina”. Se hizo un torneo para
ver qui´en es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores juegan y
se chocan entre s´ı, entonces pierde cada uno 5 puntos por haberse da˜nado. Si ambos jugadores se desv´ıan, pierde cada uno 10
puntos por gallinas. Si uno no se desv´ıa y el otro s´ı, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos!
En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se dev´ıa, o nunca lo hace.
Se debe programar la funci´on ‘torneo de gallinas’ que recibe un diccionario (donde las claves representan los nombres de los
participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y devuelve un diccionario con los puntajes
obtendidos por cada jugador.
problema torneo de gallinas (in estrategias: dict<str, str>) : dict<str, Z> {
requiere: {estrategias tiene por lo menos 2 elementos (jugadores).}
requiere: {Las claves de estrategias tienen longitud mayor a 0.}
requiere: {Los valores de estrategias s´olo pueden ser los strs ”me desv´ıo siempre” ´o ”me la banco y no me desv´ıo”.}
asegura: {Las claves de res y las claves de estrategias son iguales.}
asegura: {Para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al
finalizar el torneo, dado que jug´o una vez contra cada otro jugador.}
}
'''
def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    """
    Devuelve un diccionario con los puntajes finales de cada jugador
    después de jugar todos contra todos en el torneo de la gallina.

    PRE:
        - estrategias tiene al menos 2 jugadores.
        - Las claves son strings no vacíos.
        - Los valores son "me desvÍo siempre" o "me la banco y no me desvÍo".
    POST:
        - Devuelve un diccionario con las mismas claves.
        - Los valores indican el puntaje total de cada jugador.
    """

    puntajes: dict[str, int] = {}
    jugadores: list[str] = list(estrategias.keys())

    # Inicializa los puntajes en 0
    for jugador in jugadores:
        puntajes[jugador] = 0

    # Recorremos todas las combinaciones posibles sin repetir
    for i in range(0, len(jugadores)):
        for j in range(i + 1, len(jugadores)):
            jugador1: str = jugadores[i]
            jugador2: str = jugadores[j]
            estrategia1: str = estrategias[jugador1]
            estrategia2: str = estrategias[jugador2]

            # Caso 1: ambos NO se desvían → choque
            if estrategia1 == "me la banco y no me desvÍo" and estrategia2 == "me la banco y no me desvÍo":
                puntajes[jugador1] = puntajes[jugador1] - 5
                puntajes[jugador2] = puntajes[jugador2] - 5

            # Caso 2: ambos se desvían → doble gallina
            elif estrategia1 == "me desvÍo siempre" and estrategia2 == "me desvÍo siempre":
                puntajes[jugador1] = puntajes[jugador1] - 10
                puntajes[jugador2] = puntajes[jugador2] - 10

            # Caso 3: jugador1 no se desvía y jugador2 sí → gana jugador1
            elif estrategia1 == "me la banco y no me desvÍo" and estrategia2 == "me desvÍo siempre":
                puntajes[jugador1] = puntajes[jugador1] + 10
                puntajes[jugador2] = puntajes[jugador2] - 15

            # Caso 4: jugador1 se desvía y jugador2 no → gana jugador2
            elif estrategia1 == "me desvÍo siempre" and estrategia2 == "me la banco y no me desvÍo":
                puntajes[jugador1] = puntajes[jugador1] - 15
                puntajes[jugador2] = puntajes[jugador2] + 10

    return puntajes

estrategias: dict[str, str] = {
    "Ana": "me la banco y no me desvÍo",
    "Beto": "me desvÍo siempre",
    "Carla": "me la banco y no me desvÍo",
    "Diego": "me desvÍo siempre"
}

resultado = torneo_de_gallinas(estrategias)
print("🏁 Resultados del torneo de gallinas 🐔")
for jugador in resultado.keys():
    print(f"{jugador}: {resultado[jugador]} puntos")


'''
Ejercicio 10. Cola en el Banco
En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por
las tuplas (nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser ”com´un” o ”vip”.
Se nos pide implementar una funci´on en python que dada una cola de clientes del banco, devuelva una nueva cola con los
mismos clientes pero en donde los clientes vip est´an primero que los clientes comunes manteniendo el orden original de los clientes
vips y los comunes entre s´ı.
problema reordenar cola priorizando vips (in filaClientes: Cola<str × str>) : Cola<str> {
requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0.}
requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son ”com´un” o ”vip”.}
requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre s´ı.}
asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes.}
asegura: {|res| = |filaCliente|.}
asegura: {res no tiene elementos repetidos.}
asegura: {No hay ning´un cliente ”com´un” antes que un ”vip” en res.}
asegura: {Para todo cliente c1 y cliente c2 de tipo ”com´un” pertenecientes a filaClientes si c1 aparece antes que c2 en
filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
asegura: {Para todo cliente c1 y cliente c2 de tipo ”vip” pertenecientes a filaClientes si c1 aparece antes que c2 en
filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
}
'''
def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str, str]]) -> Cola[str]:
    clientes1: Cola[str] = Cola()
    clientes2: Cola[str] = Cola()

    while not filaClientes.empty():
        descripcion = filaClientes.get()
        if descripcion[1] == "vip":
            clientes1.put(descripcion[0])
        else:
            clientes2.put(descripcion[0])
    
    while not clientes2.empty():
        clientes1.put(clientes2.get())
    
    return clientes1

c1 = Cola()
c1.put(("Martha", "vip"))
c1.put(("Tomas", "comun"))
c1.put(("Lorena", "vip"))
c1.put(("Andrea", "comun"))

print("Cola original:", list(c1.queue))
resultado = reordenar_cola_priorizando_vips(c1)
print("Cola reordenada:", list(resultado.queue))


'''
Ejercicio 11. Sufijos que son pal´ındromos
Decimos que una palabra es pal´ındromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide programar
en python la siguiente funci´on:
problema cuantos sufijos son palindromos (in texto: str) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de pal´ındromos que hay en el conjunto de sufijos de texto.}
}
Nota: un sufijo es una subsecuencia de texto que va desde una posici´on cualquiera hasta el al final de la palabra. Ej: ”Diego”,
el conjunto de sufijos es: ”Diego”, ”iego”,”ego”,”go”, ”o”. Para este ejercicio no consideraremos a ”” como sufijo de ning´un texto.
'''
def cuantos_sufijos_son_palindromos(texto: str) -> int:
    cantidad_palindromos: int = 0
    longitud: int = len(texto)

    for inicio in range(0, longitud):
        es_palindromo: bool = True
        fin: int = longitud - 1
        i: int = inicio

        # Recorremos desde ambos extremos hacia el centro
        while i < fin:
            if texto[i] != texto[fin]:
                es_palindromo = False
            i += 1
            fin -= 1

        if es_palindromo:
            cantidad_palindromos += 1

    return cantidad_palindromos

print(cuantos_sufijos_son_palindromos("ana"))
print(cuantos_sufijos_son_palindromos("oso"))
print(cuantos_sufijos_son_palindromos("Diego"))
print(cuantos_sufijos_son_palindromos("abba"))


'''
Ejercicio 12. Ta-Te-Ti-Facilito
Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una ”X” en su turno y Beto pone una ”O” en el
suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero est´a completo y no gan´o nadie,
entonces se declara un empate. El tablero comienza vac´ıo, representado por ” ” en cada posici´on. Notar que dado que juegan por
turnos y comienza Ana poniendo una ”X” se cumple que la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad
de ”X” son uno m´as que la cantidad de ”O”. Se nos pide implementar una funci´on en python quien gano el tateti facilito que
determine si gan´o alguno, o si Beto hizo trampa (puso una ”O” cuando Ana ya hab´ıa ganado).
problema quien gano el tateti facilito (in tablero:seq⟨seq⟨Char⟩⟩) : Z {
requiere: {tablero es una matriz cuadrada.}
requiere: {5 ≤ |tablero[0]| ≤ 10.}
requiere: {tablero s´olo tiene ”X”, ”O” y ”” (espacio vac´ıo) como elementos.}
requiere: {En tablero la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad de ”X” es uno m´as que la
cantidad de ”O”.}
asegura: {res = 1 ⇔ hay tres ”X” consecutivas en forma vertical(misma columna) y no hay tres ”O” consecutivas en
forma vertical(misma columna).}
asegura: {res = 2 ⇔ hay tres ”O” consecutivas en forma vertical (misma columna) y no hay tres ”X” consecutivas en
forma vertical(misma columna).}
asegura: {res = 0 ⇔ no hay tres ”O” ni hay tres ”X” consecutivas en forma vertical.}
asegura: {res = 3 ⇔ hay tres ”X” y hay tres ”O” consecutivas en forma vertical (evidenciando que beto hizo trampa).}
}
'''
def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    """
    Determina el resultado del Ta-Te-Ti-Facilito.

    Returns:
        1 -> ganó Ana (X)
        2 -> ganó Beto (O)
        0 -> empate (nadie tiene 3 seguidas verticales)
        3 -> ambos tienen 3 seguidas verticales (trampa de Beto)
    """
    n: int = len(tablero)
    hay_ganadora_X: bool = False
    hay_ganador_O: bool = False

    # Recorre cada columna
    for col in range(n):
        contador_X: int = 0
        contador_O: int = 0

        for fila in range(n):
            celda: str = tablero[fila][col]

            if celda == "X":
                contador_X += 1
                contador_O = 0
            elif celda == "O":
                contador_O += 1
                contador_X = 0
            else:
                contador_X = 0
                contador_O = 0

            if contador_X == 3:
                hay_ganadora_X = True
            if contador_O == 3:
                hay_ganador_O = True

    # Resultado según el estado
    if hay_ganadora_X and hay_ganador_O:
        return 3
    elif hay_ganadora_X:
        return 1
    elif hay_ganador_O:
        return 2
    else:
        return 0

tablero = [
    ["X", " ", "O", "O", " "],
    ["X", " ", "O", " ", " "],
    ["X", " ", " ", " ", " "],
    [" ", "O", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]
print(quien_gano_el_tateti_facilito(tablero))


'''
Ejercicio 13. Hospital - Atenci´on por Guardia
Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la informaci´on que maneja sobre
los pacientes y el personal de salud. En primer lugar debemos resolver en qu´e orden se deben atender los pacientes que llegan a
la guardia. En enfermer´ıa, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable
(esto se llama hacer triage). A partir de dichas colas que contienen la identificaci´on del paciente, se pide devolver una nueva cola
seg´un la siguiente especificaci´on.
problema orden de atencion (in urgentes: cola<Z>, in postergables: cola<Z>) : cola<Z> {
requiere: {No hay elementos repetidos en urgentes.}
requiere: {No hay elementos repetidos en postergables.}
requiere: {La intersecci´on entre postergables y urgentes es vac´ıa.}
requiere: {|postergables| = |urgentes|.}
asegura: {No hay repetidos en res.}
asegura: {res es permutaci´on de la concatenaci´on de urgentes y postergables.}
asegura: {Si urgentes no es vac´ıa, en la cabeza de res hay un elemento de urgentes.}
asegura: {En res no hay dos seguidos de urgentes.}
asegura: {En res no hay dos seguidos de postergables.}
asegura: {Para todo c1 y c2 de tipo ”urgente” pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces
c1 aparece antes que c2 en res.}
asegura: {Para todo c1 y c2 de tipo ”postergable” pertenecientes a postergables si c1 aparece antes que c2 en postergables
entonces c1 aparece antes que c2 en res.}
}
'''
def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    """
    Devuelve una nueva cola con el orden de atención:
    - Comienza con un paciente urgente.
    - Alterna entre urgente y postergable.
    - Mantiene el orden relativo de cada cola.
    """
    res: Cola[int] = Cola()

    # Mientras haya pacientes en ambas colas
    while not urgentes.empty() and not postergables.empty():
        res.put(urgentes.get())
        res.put(postergables.get())

    # En teoría, ambas colas deberían quedar vacías al mismo tiempo (según la especificación)
    # pero si alguna tuviera más elementos, los agregamos al final
    while not urgentes.empty():
        res.put(urgentes.get())
    while not postergables.empty():
        res.put(postergables.get())

    return res

# Creo las colas
urgentes = Cola()
postergables = Cola()

# Pacientes urgentes
urgentes.put(101)
urgentes.put(102)
urgentes.put(103)

# Pacientes postergables
postergables.put(201)
postergables.put(202)
postergables.put(203)

# Obtengo la cola final
resultado = orden_de_atencion(urgentes, postergables)

# Muestro el orden final
print(list(resultado.queue))


'''
Ejercicio 14. Hospital - Alarma epidemiol´ogica
Necesitamos detectar la aparici´on de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los
registros de atenci´on por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad
que motiv´o la atenci´on. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporci´on
de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas
cuya proporci´on supere cierto umbral.
problema alarma epidemiologica (in registros : seq⟨Z × str⟩, in infecciosas : seq⟨str⟩, in umbral : R) : dict<str, R> {
requiere: {0 < umbral < 1.}
asegura: {claves de res pertenecen a infecciosas.}
asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
}
'''
def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    res: dict[str, float] = {}
    total_registros: int = len(registros)

    if total_registros == 0:
        return res

    conteo: dict[str, int] = {}
    for expediente in registros:
        if expediente[1] in conteo.keys():
            conteo[expediente[1]] += 1
        else:
            conteo[expediente[1]] = 1
    
    for enfermedad in infecciosas:
        if enfermedad in conteo.keys():
            proporcion: float = conteo[enfermedad] / total_registros
            if proporcion >= umbral:
                res[enfermedad] = proporcion
    
    return res

registros = [
    (1, "gripe"),
    (2, "covid"),
    (3, "gripe"),
    (4, "dengue"),
    (5, "covid")
]
infecciosas = ["gripe", "covid", "dengue"]
umbral = 0.3

print(alarma_epidemiologica(registros, infecciosas, umbral))


'''
Ejercicio 15. Hospital - Empleado del mes
Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
una lista de las horas trabajadas por d´ıa, queremos saber quienes trabajaron m´as para darles un premio. Se deber´a buscar la o
las claves para la cual se tiene el m´aximo valor de cantidad total de horas, y devolverlas en una lista.
problema empleados del mes (horas:dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
requiere: {No hay valores en horas que sean listas vac´ıas.}
asegura: {Si ID pertence a res entonces ID pertence a las claves de horas.}
asegura: {Si ID pertenece a res, la suma de sus valores de horas es el m´aximo de la suma de elementos de horas de todos
los otros IDs.}
asegura: {Para todo ID de claves de horas, si la suma de sus valores es el m´aximo de la suma de elementos de horas de
los otros IDs, entonces ID pertenece a res.}
}
'''

'''
Ejercicio 16. Hospital - Nivel de ocupaci´on
Queremos saber qu´e porcentaje de ocupaci´on de camas hay en el hospital. El hospital se representa por una matriz en donde
las filas son los pisos, y las columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama est´a ocupada
o no. Si el valor es verdadero (True) indica que la cama est´a ocupada.
Se nos pide programar en Python una funci´on que devuelve una secuencia de reales, indicando la proporci´on de camas
ocupadas en cada piso.
problema nivel de ocupacion (in camas por piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
requiere: {Todos los pisos tienen la misma cantidad de camas.}
requiere: {Hay por lo menos 1 piso en el hospital.}
requiere: {Hay por lo menos una cama por piso.}
asegura: {|res| = |camas por piso|.}
asegura: {Para todo 0 ≤ i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el
total de camas del piso i).}
}
'''
def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []

    for piso in camas_por_piso:
        cant_camas: int = len(piso)
        cant_camas_ocupadas: int = 0

        for cama in piso:
            if cama == True:
                cant_camas_ocupadas += 1
            porcentaje: float = cant_camas_ocupadas / cant_camas
        
        res.append(porcentaje)
    
    return res

camas_por_piso: list[list[bool]] = [[False, True, False],
                                    [True, False, True],
                                    [True, True, True]]

print(nivel_de_ocupacion(camas_por_piso))


def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    cant_parejas: int = 0

    for i in range(0, len(s)):
        numero_actual: int = s[i]
        indice_mayor: int = i + 1

        for indice_posterior in range(indice_mayor, len(s)):
            numero_posterior: int = s[indice_posterior]
            suma_numeros: int = numero_actual + numero_posterior

            if suma_numeros == n:
                cant_parejas += 1
    
    return cant_parejas

print(cantidad_parejas_que_suman([1,2,3,4,5],5))


# Ejercicio 2 
def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    cola_aux: Cola = Cola()
    res: str = ""
    encontrado: bool = False

    while not clientes.empty():
        elem = clientes.get()

        if not encontrado and elem[1] != "efectivo" and elem[2] <= 15:
            res = elem[0]
            encontrado = True  # 🚩 Ya encontré el primero, no sigo buscando
        else:
            cola_aux.put(elem)

    # Restaurar la cola original (sin el cliente atendido)
    while not cola_aux.empty():
        clientes.put(cola_aux.get())

    return res

c: Cola = Cola()
c.put(("Ana","efectivo",13))
c.put(("Juan","qr",22))
c.put(("Bruno","tarjeta",14))
print(c.queue)
print(pasar_por_autoservicio(c))
print(c.queue)


# Ejercicio 3 
def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    res: list[list[int]] = []
    
    return


# Ejercicio 4
def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}

    for residente in censo1.keys():
        if censo1[residente] == censo2[residente]:
            localidad: tuple[str,str] = censo1[residente]
            if localidad not in res.keys():
                res[localidad] = 1
            else:
                res[localidad] += 1
    
    return res

print({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'})
print(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'}))


def suma_total(s: list[int]) -> int:
    res: int = 0

    for i in range(len(s)):
        res += s[i]
    
    return res

print(suma_total([1,2,3,4]))

def maximo(s: list[int]) -> int:
    maximo: int = s[0]

    for i in range(1, len(s)):
        if s[i] >= maximo:
            maximo = s[i]
    
    return maximo

print(maximo([1,2,3,4]))

def minimo(s: list[int]) -> int:
    minimo: int = s[0]

    for i in range(1, len(s)):
        if s[i] <= minimo:
            minimo = s[i]
    
    return minimo

print(minimo([1,2,3,4]))

def maximo_y_minimo(s: list[int]) -> tuple[int, int]:
    return (minimo(s), maximo(s))

print(maximo_y_minimo([1,2,3,4]))

def eliminar_fila_que_mas_suma(A: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    maximo: int = 0

    for i in range(len(A)):
        if suma_total(A[i]) >= maximo:
            maximo = suma_total(A[i])
        
    for fila in A:
        if suma_total(fila) != maximo:
            res.append(fila)
    
    return res

matriz = [[1,2,3],
          [7,8,9],
          [4,5,6]]

print(eliminar_fila_que_mas_suma(matriz))


def ordenar_lista(lista: list[int]) -> list[int]:
    res: list[int] = lista.copy()
    n: int = len(res)

    for i in range(n - 1):
        pos_min: int = i
        for j in range(i + 1, n):
            if res[j] < res[pos_min]:
                pos_min = j
        # intercambio de elementos
        aux: int = res[i]
        res[i] = res[pos_min]
        res[pos_min] = aux

        # otra forma de hacerlo

    return res


def ordenar_lista2(s: list[int]) -> list[int]:
    res = s.copy()
    for i in range(len(res)):
        for j in range(len(res) - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]  # swap elegante
    return res


def matriz_ordenada(m: list[list[int]]) -> list[list[int]]:
    # Paso 1: aplanar la matriz
    elementos: list[int] = []
    for fila in m:
        for elem in fila:
            elementos.append(elem)

    # Paso 2: ordenar con nuestra función
    elementos_ordenados: list[int] = ordenar_lista2(elementos)

    # Paso 3: reconstruir la matriz ordenada
    n: int = len(m)
    res: list[list[int]] = []
    k: int = 0

    for i in range(n):
        fila_nueva: list[int] = []
        for j in range(n):
            fila_nueva.append(elementos_ordenados[k])
            k += 1
        res.append(fila_nueva)

    return res

matriz = [
    [9, 3, 4],
    [2, 1, 5],
    [8, 7, 6]
]

print(matriz_ordenada(matriz))
