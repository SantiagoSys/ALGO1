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
def ultimos_tres_elementos(numero: int) -> int:
    return numero % 1000

def es_primo(numero: int) -> bool:
    if numero % 2 == 0:
        return False
    return True

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []

    for numero in codigos_barra:
        if es_primo(ultimos_tres_elementos(numero)):
            res.append(numero)
    
    return res


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
    indice_inicio_max: int = 0
    longitud_actual: int = 0
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
    res: dict[str, tuple[str, float]] = {}

    for amigo, tiempos in registro.items():
        exitosos: list[int] = []
        for t in tiempos:
            if 0 < t < 61:
                exitosos.append(t)
        if len(exitosos) > 0:
            res[amigo] = (len(exitosos), promedio(exitosos))
        else:
            res[amigo] = (0, 0.0)
            
    return res

def promedio(s: list[int]) -> float:
    return sumatoria(s) / len(s)

def sumatoria(s:list[int]) -> int:
    res: int = 0
    for i in range(len(s)):
        res += s[i]
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

print("EJERCICIO TIEMPO_MAS_RAPIDO")
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
    pass

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
    pass

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

print("EJERCICIO TORNEO_DE_GALLINAS")
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

print("EJERCICIO COLA_EN_EL_BANCO")
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

print("EJERCICIO SUFIJOS_SON_PALINDROMOS")
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
def quien_gano_el_tateti_facilito(tablero: list[str]) -> int:
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

print("EJERCICIO TATETI FACILITO")
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
print("EJERCICIO ORDEN DE ATENCION")
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

print("EJERCICIO ALARMA_EPIDEMIOLOGICA")
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
def empleado_del_mes(horas: dict[tuple[int, list[int]]]) -> list[int]:
    pass


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

print("EJERCICIO NIVEL_DE_OCUPACION")
print(nivel_de_ocupacion(camas_por_piso))


'''
Ejercicio 17.
problema ejercicio1 (in s: seq⟨Z⟩, in objetivo: Z) : Z x Z {
  requiere: { Existen al menos dos posiciones i < j en rango tales que s[i] + s[j] = objetivo }
  asegura: { s[res0] + s[res1] = objetivo }
  asegura: { res0 < res1 }
  asegura: { Sean i y j (con i < j) dos posiciones cualesquiera de s tales que s[i] + s[j] = objetivo, entonces res1 - res0 <= j - i }
}
'''
def ejercicio1(s: list[int], objetivo: int) -> tuple[int, int]:
    mejor = (0, 1)
    mejor_distancia = len(s)  # mayor que cualquier distancia posible (max len(s) - 1)

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == objetivo and j - i < mejor_distancia:
                mejor = (i, j)
                mejor_distancia = j - i

    return mejor

print("IIIIIIIIIIIIIIIIIII")
print(ejercicio1([1,2,3,5], 4))


'''
Ejercicio 18.
En la cocina de un restaurante, los pedidos se van apilando a medida que llegan (se prepara primero el que llegó último). Cada pedido es una tupla 
con el número de mesa y un booleano que indica si es un pedido express (True) o no (False). Se desea separar de la pila los pedidos express, 
pasándolos a una nueva pila, y dejar en la pila original solamente los pedidos que no son express. Implementar la función separar_pedidos_express.

problema separar_pedidos_express (inout pedidos: Pila⟨Z x Bool⟩) : Pila⟨Z⟩ {
  modifica: { pedidos }
  asegura: { res contiene exactamente los números de mesa de las tuplas cuya segunda componente en pedidos@pre era True, en el mismo orden 
  relativo (de tope a base) en que se encontraban en pedidos@pre }
  asegura: { pedidos contiene exactamente las tuplas de pedidos@pre cuya segunda componente era False, en el mismo orden relativo (de tope a base) 
  en que se encontraban originalmente }

Ejemplo: Si pedidos contiene (de tope a base):
[(5, True), (3, False), (8, True), (2, False)], entonces
separar_pedidos_express(pedidos) debe devolver una pila que (de tope a base) 
contiene [5, 8], y pedidos queda (de tope a base) con [(3, False), (2, False)].
'''
def separar_pedidos_express(pedidos: Pila[int, bool]) -> Pila[int]:
    express_aux = Pila()      # guarda solo números de mesa
    no_express_aux = Pila()   # guarda tuplas completas

    # 1) Vaciar la pila original, repartiendo cada pedido según su booleano
    while not pedidos.empty():
        mesa, es_express = pedidos.get()
        if es_express:
            express_aux.put(mesa)
        else:
            no_express_aux.put((mesa, es_express))

    # 2) Devolver los no express a la pila original (invierte de nuevo)
    while not no_express_aux.empty():
        pedidos.put(no_express_aux.get())

    # 3) Armar la pila resultado con los express (invierte de nuevo)
    res = Pila()
    while not express_aux.empty():
        res.put(express_aux.get())

    return res


'''
Ejercicio 19.
problema ejercicio5 (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  requiere: { Todos los elementos de A son distintos entre sí }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Sea max el máximo elemento de A@pre, y sea i la fila tal que existe una columna j con A@pre[i][j] = max, entonces A[i][k] = 2 * A@pre[i][k] para todo k en rango }
  asegura: { Sea max el máximo elemento de A@pre, y sea i la fila tal que existe una columna j con A@pre[i][j] = max, entonces A[f][k] = A@pre[f][k] para todo f en rango y todo k en rango tal que f ≠ i }
}
'''
def ejercicio5(A: list[list[int]]) -> None:
    # 1) Buscar la fila que contiene el máximo (sin modificar nada todavía)
    fila_max = 0
    maximo = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > maximo:
                maximo = A[i][j]
                fila_max = i

    # 2) Duplicar todos los elementos de esa fila, en el lugar
    for k in range(len(A[fila_max])):
        A[fila_max][k] = 2 * A[fila_max][k]


'''
Ejercicio 20.
Una plataforma de e-learning registra, para cada estudiante, la lista de calificaciones obtenidas en los distintos cursos que realizó a lo largo 
del tiempo. Estos datos se almacenan en un diccionario cuyas claves son los nombres de los estudiantes y cuyos valores son secuencias con las 
calificaciones (de 1 a 10) obtenidas en cada curso. Diremos que un estudiante es destacado si todas sus calificaciones son mayores o iguales a 
una nota mínima dada. Implementar la función estudiantes_destacados_por_cantidad_de_cursos, que agrupa a los estudiantes destacados según la 
cantidad de cursos que realizaron:

problema estudiantes_destacados_por_cantidad_de_cursos (in calificaciones: dict⟨String, seq⟨Z⟩⟩, in nota_minima: Z) : dict⟨Z, seq⟨String⟩⟩ {
  requiere: { Para toda clave c de calificaciones, calificaciones[c] no es vacía }
  asegura: { Una clave n de res existe si y sólo si existe al menos un estudiante destacado c que haya realizado exactamente n cursos, es decir, 
  tal que |calificaciones[c]| = n }
  asegura: { Para toda clave n de res, res[n] contiene exactamente los nombres de los estudiantes destacados que realizaron exactamente n cursos }
}
Nota: Un estudiante c de calificaciones es destacado si todas las calificaciones de calificaciones[c] son mayores o iguales a nota_minima

Ejemplo: estudiantes_destacados_por_cantidad_de_cursos({"Ana": [10, 9], 
  "Beto": [8], "Cami": [7, 8, 9], "Dani": [6, 3]}, 7) debe devolver 
{2: ["Ana"], 1: ["Beto"], 3: ["Cami"]} 
(Dani no es destacado, ya que tiene una calificación menor a 7)
'''
def estudiantes_destacados_por_cantidad_de_cursos(calificaciones: dict[str, list[int]], nota_minima: int) -> dict[int, list[str]]:
    res: dict[int, list[str]] = {}

    for alumno, notas in calificaciones.items():
        if not desaprobo_curso(notas, nota_minima):
            cantidad = len(notas)
            if cantidad not in res:
                res[cantidad] = []
            res[cantidad].append(alumno)
    return res

def desaprobo_curso(s: list[int], nota_minima: int) -> bool:
    for i in range(len(s)):
        if s[i] < nota_minima:
            return True
    return False



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


'''
Otros ejercicios
'''

'''
problema par_mas_lejano_que_suma_objetivo (in s: seq⟨Z⟩, in objetivo: Z) : Z x Z {
  requiere: { Existen al menos dos posiciones i < j en rango tales que s[i] + s[j] = objetivo }
  asegura: { s[res0] + s[res1] = objetivo }
  asegura: { res0 < res1 }
  asegura: { Sean i y j (con i < j) dos posiciones cualesquiera de s tales que s[i] + s[j] = objetivo, entonces res1 - res0 >= j - i }
}

Ejemplo: s = [3, 1, 4, 6, 2, 5], objetivo = 7 → (0, 2) y (1, 3) suman 7 con distancia 2, pero (2, 5)... verificá vos cuál es el más lejano.
'''
def par_mas_lejano_que_suma_objetivo(s: list[int], objetivo: int) -> tuple[int, int]:
    mejor = (0, 1)
    mejor_distancia = len(s)  # mayor que cualquier distancia posible (max len(s) - 1)
    
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == objetivo and j - i < mejor_distancia:
                mejor = (i, j)
                mejor_distancia = j - i
    
    return mejor

'''
problema par_con_mayor_diferencia (in s: seq⟨Z⟩) : Z x Z {
  requiere: { |s| >= 2 }
  asegura: { res0 < res1 }
  asegura: { Para todo par de posiciones i < j en rango, s[res1] - s[res0] >= s[j] - s[i] }
}

Ejemplo: s = [5, 1, 9, 3, 2] → (1, 2), porque 9 - 1 = 8 es la mayor diferencia con la derecha mayor.
'''
def par_con_mayor_diferencia(s: list[int]) -> tuple[int, int]:
    mejor = (0, 1)
    mejor_distancia = len(s)

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if j - i > mejor_distancia:
                mejor = (i, j)
                mejor_distancia = j - i

    return mejor

'''
problema separar_pares (inout p: Pila⟨Z⟩) : Pila⟨Z⟩ {
  modifica: { p }
  asegura: { res contiene exactamente los elementos pares de p@pre, en el mismo orden relativo (de tope a base) en que estaban en p@pre }
  asegura: { p contiene exactamente los elementos impares de p@pre, en el mismo orden relativo (de tope a base) en que estaban en p@pre }
}

Ejemplo: p (tope a base) [4, 7, 2, 9, 6] → res = [4, 2, 6], p = [7, 9].
'''

'''
problema atender_urgentes (inout turnos: Cola⟨Z x Bool⟩) : Cola⟨Z⟩ {
  modifica: { turnos }
  asegura: { res contiene los números de paciente de las tuplas de turnos@pre cuya segunda componente era True, en el mismo orden en que estaban en turnos@pre }
  asegura: { turnos contiene exactamente las tuplas de turnos@pre cuya segunda componente era False, en el mismo orden relativo }
}

Ejemplo: turnos (primero a último) [(1, False), (2, True), (3, True), (4, False)] → res = [2, 3], turnos = [(1, False), (4, False)].
'''

'''
problema duplicar_columna_del_minimo (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  requiere: { Todos los elementos de A son distintos entre sí }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Sea min el mínimo elemento de A@pre, y sea j la columna tal que existe una fila i con A@pre[i][j] = min, entonces A[f][j] = 2 * A@pre[f][j] para todo f en rango }
  asegura: { Para toda fila f y toda columna k en rango con k ≠ j, A[f][k] = A@pre[f][k] }
}
'''

'''
problema intercambiar_fila_del_maximo_con_la_primera (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  requiere: { Todos los elementos de A son distintos entre sí }
  modifica: { A }
  asegura: { A tiene las mismas dimensiones que A@pre }
  asegura: { Sea i la fila de A@pre que contiene el máximo elemento. Entonces A[0] = A@pre[i] y A[i] = A@pre[0] }
  asegura: { Para toda fila f en rango con f ≠ 0 y f ≠ i, A[f] = A@pre[f] }
}
'''

'''
problema productos_por_cantidad_de_ventas (in ventas: dict⟨String, seq⟨Z⟩⟩, in monto_minimo: Z) : dict⟨Z, seq⟨String⟩⟩ {
  requiere: { Para toda clave p de ventas, ventas[p] no es vacía }
  asegura: { Una clave n de res existe si y sólo si existe al menos un producto p cuyas ventas sean todas mayores o iguales a monto_minimo y tal que |ventas[p]| = n }
  asegura: { Para toda clave n de res, res[n] contiene exactamente los nombres de los productos con todas sus ventas >= monto_minimo y con exactamente n ventas }
}
Ejemplo: ventas = {"lapiz": [50, 60], "goma": [20, 90], "regla": [70]}, monto_minimo = 50 → {2: ["lapiz"], 1: ["regla"]}.
'''

'''
problema invertir_diccionario (in d: dict⟨String, Z⟩) : dict⟨Z, seq⟨String⟩⟩ {
  asegura: { Una clave v de res existe si y sólo si existe una clave c de d tal que d[c] = v }
  asegura: { Para toda clave v de res, res[v] contiene exactamente las claves c de d tales que d[c] = v }
}

Ejemplo: {"Ana": 8, "Beto": 5, "Cami": 8} → {8: ["Ana", "Cami"], 5: ["Beto"]}.
'''


'''
EJERCICIO 1
'''
def cantidad_parejas_iguales(s: list[int]) -> int:
    contador: int = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                contador += 1
    return contador

print(cantidad_parejas_iguales([1, 2, 1, 1]))

def cantidad_parejas_con_diferencia(s: list[int], d: int) -> int:
    contador: int = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if absoluto(s[i] - s[j]) == d:
                contador += 1
    return contador

def absoluto(n: int) -> int:
    if n < 0:
        return -n

print(cantidad_parejas_con_diferencia([1, 4, 6, 3], 2))

def parejas_que_suman(s: list[int], n: int) -> list[tuple[int, int]]:
    res: list[tuple[int]] =  []
    mejor = (0, 1)

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == n:
                mejor = (s[i], s[j])
                res.append(mejor)

    return res

print(parejas_que_suman([2, 4, 3, 3], 6))


'''
EJERCICIOS MATRICES
'''

def suma_de_esquinas(A: list[list[int]]) -> int:
    ultima_fila: int = len(A) - 1
    ultima_col: int = len(A[0]) - 1

    res: int = A[0][0] + A[0][ultima_col] + A[ultima_fila][0] + A[ultima_fila][ultima_col]
    return res

def iesima_columna(A: list[list[int]], i: int) -> int:
    res: list[int] = []

    for f in range(len(A)):
        res.append(A[f][i])

    return res

'''
problema duplicar_fila_del_minimo (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  requiere: { Todos los elementos de A son distintos entre sí }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Sea min el mínimo elemento de A@pre, y sea i la fila tal que existe una columna j con A@pre[i][j] = min, entonces A[i][k] = 2 * A@pre[i][k] para todo k en rango }
  asegura: { A[f][k] = A@pre[f][k] para todo f en rango y todo k en rango tal que f ≠ i }
}

Ejemplo: [[5,2,8],[7,1,9],[4,6,3]] → [[5,2,8],[14,2,18],[4,6,3]].
'''
def duplicar_fila_del_minimo(A: list[list[int]]) -> None:
    fila_min = 0
    minimo = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < minimo:
                minimo = A[i][j]
                fila_min = i

    for k in range(len(A[fila_min])):
        A[fila_min][k] = 2 * A[fila_min][k]

print("DUPLICAR FILA DEL MINIMO")
M: list[list[int]] = [[5,2,8],[7,1,9],[4,6,3]]
print(M)
duplicar_fila_del_minimo(M)
print(M)

'''
problema duplicar_columna_del_maximo (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  requiere: { Todos los elementos de A son distintos entre sí }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Sea max el máximo elemento de A@pre, y sea j la columna tal que existe una fila i con A@pre[i][j] = max, entonces A[f][j] = 2 * A@pre[f][j] para todo f en rango }
  asegura: { A[f][k] = A@pre[f][k] para todo f en rango y todo k en rango tal que k ≠ j }
}

Ejemplo: [[1,2,3],[4,9,6],[7,8,5]] → [[1,4,3],[4,18,6],[7,16,5]].
'''
def duplicar_columna_del_maximo(A: list[list[int]]) -> None:
    j: int = columna_del_maximo(A)

    for i in range(len(A)):
        A[i][j] = 2*A[i][j]

def columna_del_maximo(A: list[list[int]]) -> int:
    maximo: int = A[0][0]
    col_maximo: int = 0

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] >= maximo:
                maximo = A[i][j]
                col_maximo = j

    return col_maximo

def maximo_matriz(A: list[list[int]]) -> int:
    maximo: int = maximo_fila(A[0])

    for i in range(1, len(A)):
        if maximo_fila(A[i]) >= maximo:
            maximo = maximo_fila(A[i])
    return maximo

def maximo_fila(s: list[int]) -> int:
    maximo: int = s[0]

    for i in range(1, len(s)):
        if s[i] >= maximo:
            maximo = s[i]
    return maximo
print("LALALAL")
print(maximo_fila([1,2,3,4]))
print(maximo_matriz(M))

'''
problema intercambiar_filas_del_maximo_y_el_minimo (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  requiere: { Todos los elementos de A son distintos entre sí }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Sea i la fila de A@pre que contiene el máximo y sea j la fila de A@pre que contiene el mínimo. Entonces A[i] = A@pre[j] y A[j] = A@pre[i] }
  asegura: { A[f] = A@pre[f] para toda fila f en rango con f ≠ i y f ≠ j }
}

Ejemplo: [[5,2,8],[7,6,9],[4,1,3]] → [[5,2,8],[4,1,3],[7,6,9]]. Pensá qué pasa si el máximo y el mínimo están en la misma fila.
'''
def intercambiar_filas_del_maximo_y_el_minimo(A: list[list[int]]) -> None:
    fila_min: int = fila_del_minimo(A)
    fila_max: int = fila_del_maximo(A)

    A[fila_min], A[fila_max] = A[fila_max], A[fila_min]

def fila_del_maximo(A: list[list[int]]) -> int:
    fila_maxima: int = 0
    maximo: int = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] >= maximo:
                maximo = A[i][j]
                fila_maxima = i

    return fila_maxima

def fila_del_minimo(A: list[list[int]]) -> int:
    fila_minima: int = 0
    minimo: int = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] <= minimo:
                minimo = A[i][j]
                fila_minima = i

    return fila_minima

'''
problema restar_minimo_de_cada_fila (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todas las filas de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Para toda fila i y toda columna j en rango, A[i][j] = A@pre[i][j] - m, donde m es el mínimo elemento de A@pre[i] }
}

Ejemplo: [[5,2,8],[7,6,9]] → [[3,0,6],[1,0,3]].
'''
def restar_minimo_de_cada_fila(A: list[list[int]]) -> None:
    for i in range(len(A)):
        minimo: int = minimo_fila(A[i])
        for j in range(len(A[i])):
            A[i][j] = A[i][j] - minimo

def minimo_fila(s: list[int]) -> int:
    minimo: int = s[0]
    for i in range(len(s)):
        if s[i] <= minimo:
            minimo = s[i]

    return minimo

'''
problema poner_ceros_en_la_diagonal (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { A es cuadrada: todas sus filas tienen longitud |A| }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { A[i][i] = 0 para todo i en rango }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango con i ≠ j }
}

Ejemplo: [[1,2],[3,4]] → [[0,2],[3,0]].
'''
def poner_ceros_en_la_diagonal(A: list[list[int]]) -> None:
    for i in range(len(A)):
        A[i][i] = 0

'''
problema reemplazar_negativos_por_cero (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Para todo i, j en rango, si A@pre[i][j] < 0 entonces A[i][j] = 0, y si no, A[i][j] = A@pre[i][j] }
}

Ejemplo: [[1,-2],[-3,4]] → [[1,0],[0,4]].
'''
def reemplazar_negativos_por_ceros(A: list[list[int]]) -> None:
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < 0:
                A[i][j] = 0

'''
problema invertir_cada_fila (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Para toda fila i y toda columna j en rango, A[i][j] = A@pre[i][|A@pre[i]| - 1 - j] }
}

Ejemplo: [[1,2,3],[4,5,6]] → [[3,2,1],[6,5,4]].
'''
def invertir_cada_fila(A: list[list[int]]) -> None:
    for i in range(len(A)):
        n: int = len(A[i])
        for j in range(n // 2):
            A[i][j], A[i][n - 1 - j] = A[i][n - 1 - j], A[i][j]

'''
problema trasponer_matriz_cuadrada (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { A es cuadrada: todas sus filas tienen longitud |A| }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { Para todo i, j en rango, A[i][j] = A@pre[j][i] }
}

Ejemplo: [[1,2],[3,4]] → [[1,3],[2,4]].
'''
def trasponer_matriz_cuadrada(A: list[list[int]]) -> None:
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]


'''
EJERCICIOS DE PILAS Y COLAS
'''
'''
problema contar_pares_en_pila (in p: Pila⟨Z⟩) : Z {
  requiere: { - }
  asegura: { res es la cantidad de elementos pares de p }
}
'''
def contar_pares_en_pila(p: Pila) -> int:
    aux: Pila = Pila()
    res: int = 0

    # Vaciar p en aux, contando los pares
    while not p.empty():
        elem: int = p.get()
        if elem % 2 == 0:
            res += 1
        aux.put(elem)

    # Restaurar p (aux tiene el orden invertido, así que se invierte de nuevo)
    while not aux.empty():
        p.put(aux.get())

    return res

'''
problema copiar_pila (in p: Pila⟨Z⟩) : Pila⟨Z⟩ {
  requiere: { - }
  asegura: { res tiene los mismos elementos que p, en el mismo orden (de tope a base) }
}

Ejemplo: p = [1, 2, 3] → res = [1, 2, 3]
'''
def copiar_pila(p: Pila) -> Pila:
    aux: Pila = Pila()
    res: Pila = Pila()

    # Paso 1: vaciar p en aux (aux queda con el orden invertido)
    while not p.empty():
        aux.put(p.get())

    # Paso 2: pasar de aux a p y a res (restaura p y arma la copia)
    while not aux.empty():
        elem: int = aux.get()
        p.put(elem)
        res.put(elem)

    return res

'''
problema mayores_que_el_tope (in p: Pila⟨Z⟩) : Pila⟨Z⟩ {
  requiere: { p no es vacía }
  asegura: { res contiene exactamente los elementos de p estrictamente mayores al tope de p, en el mismo orden relativo (de tope a base) }
}

Ejemplo: p = [4, 7, 2, 9, 6] → res = [7, 9, 6].
'''
def mayores_que_el_tope(p: Pila) -> Pila:
    aux: Pila = Pila()
    res: Pila = Pila()

    # Paso 1: sacar el tope y guardarlo
    tope: int = p.get()
    aux.put(tope)

    # Paso 2: vaciar el resto de p en aux
    while not p.empty():
        aux.put(p.get())

    # aux tiene (tope a base): base original ... tope original (el tope original queda abajo de todo
    # pero lo guardamos en la variable "tope")
    # Paso 3: pasar de aux a p restaurando el orden original,
    # y armar res con los mayores al tope
    while not aux.empty():
        elem: int = aux.get()
        p.put(elem)
        if elem > tope:
            res.put(elem)

    return res

'''
problema pila_ordenada (in p: Pila⟨Z⟩) : Bool {
  requiere: { - }
  asegura: { res = true si y solo si, leyendo de tope a base, cada elemento es menor o igual al siguiente }
}

Ejemplos: [1, 3, 3, 8] → True, [1, 5, 2] → False.
'''
def pila_ordenada(p: Pila) -> bool:
    aux: Pila = Pila()
    ordenada: bool = True

    if not p.empty():
        anterior: int = p.get()
        aux.put(anterior)

        # Vaciar el resto de p en aux, comparando cada elemento con el anterior
        while not p.empty():
            actual: int = p.get()
            if anterior > actual:
                ordenada = False
            aux.put(actual)
            anterior = actual

    # Restaurar p (aux tiene el orden invertido, así que se invierte de nuevo)
    while not aux.empty():
        p.put(aux.get())

    return ordenada

'''
problema posicion_del_maximo_en_cola (in c: Cola⟨Z⟩) : Z {
  requiere: { c no es vacía }
  asegura: { res es la menor posición (contando desde 0 el primer elemento) en la que c tiene su máximo elemento }
}

Ejemplo: c = [3, 9, 2, 9] → 1.
'''
def posicion_del_maximo_en_cola(c: Cola) -> int:
    n: int = c.qsize()
    maximo: int = 0
    pos_maximo: int = 0

    for i in range(n):
        elem: int = c.get()
        if i == 0 or elem > maximo:
            maximo = elem
            pos_maximo = i
        c.put(elem)   # se reencola al final: tras n vueltas, c queda como estaba

    return pos_maximo

'''
problema intercalar_colas (in c1: Cola⟨Z⟩, in c2: Cola⟨Z⟩) : Cola⟨Z⟩ {
  requiere: { - }
  asegura: { res alterna elementos de c1 y de c2 empezando por c1. Cuando una de las dos se agota, los elementos que quedan de la otra se agregan al final en su orden }
}

Ejemplo: c1 = [1, 2, 3], c2 = [10, 20] → res = [1, 10, 2, 20, 3].
'''
def intercalar_colas(c1: Cola, c2: Cola) -> Cola:
    res: Cola = Cola()
    n1: int = c1.qsize()
    n2: int = c2.qsize()
    menor: int = min(n1, n2)

    # Alternar mientras haya elementos en ambas
    for _ in range(menor):
        e1: int = c1.get()
        res.put(e1)
        c1.put(e1)      # se reencola al final para restaurar c1

        e2: int = c2.get()
        res.put(e2)
        c2.put(e2)      # se reencola al final para restaurar c2

    # Pasar lo que queda de la más larga (solo una de las dos tiene resto)
    for _ in range(n1 - menor):
        e1: int = c1.get()
        res.put(e1)
        c1.put(e1)

    for _ in range(n2 - menor):
        e2: int = c2.get()
        res.put(e2)
        c2.put(e2)

    return res

'''
problema primeros_k_de_cola (in c: Cola⟨Z⟩, in k: Z) : Cola⟨Z⟩ {
  requiere: { 0 <= k <= |c| }
  asegura: { res contiene los primeros k elementos de c, en el mismo orden }
}

Ejemplo: c = [5, 1, 8, 3, 9], k = 3 → res = [5, 1, 8].
'''
def primeros_k_de_cola(c: Cola, k: int) -> Cola:
    res: Cola = Cola()
    n: int = c.qsize()

    for i in range(n):
        elem: int = c.get()
        if i < k:
            res.put(elem)
        c.put(elem)   # se reencola al final: tras n vueltas, c queda como estaba

    return res

'''
problema invertir_cola (in c: Cola⟨Z⟩) : Cola⟨Z⟩ {
  requiere: { - }
  asegura: { res tiene los mismos elementos que c, en el orden inverso (el primero de res es el último de c) }
}

Ejemplo: c = [1, 2, 3] → res = [3, 2, 1]. Acá se combinan una cola y una pila auxiliar.
'''
def invertir_cola(c: Cola) -> Cola:
    res: Cola = Cola()
    aux: Pila = Pila()
    n: int = c.qsize()

    # Paso 1: recorrer c copiando cada elemento a la pila (y reencolándolo para restaurar c)
    for _ in range(n):
        elem: int = c.get()
        aux.put(elem)
        c.put(elem)

    # Paso 2: vaciar la pila en res (sale en orden inverso)
    while not aux.empty():
        res.put(aux.get())

    return res


'''
EJERCICIOS DE DICCIONARIOS
'''
'''
problema suma_de_notas_por_estudiante (in calificaciones: dict⟨String, seq⟨Z⟩⟩) : dict⟨String, Z⟩ {
  requiere: { -  }
  asegura: { Las claves de res son exactamente las claves de calificaciones }
  asegura: { Para toda clave c de res, res[c] es la suma de los elementos de calificaciones[c] }
}

Ejemplo: {"Ana": [10, 9], "Beto": [8]} → {"Ana": 19, "Beto": 8}.
'''
def suma_de_notas_por_estudiante(calificaciones: dict[str, list[int]]) -> dict[str, int]:
    res: dict[str, int] = {}

    for nombre in calificaciones:
        suma: int = 0
        for nota in calificaciones[nombre]:
            suma += nota
        res[nombre] = suma

    return res

'''
problema estudiantes_con_alguna_nota_baja (in calificaciones: dict⟨String, seq⟨Z⟩⟩, in nota_minima: Z) : seq⟨String⟩ {
  requiere: { - }
  asegura: { res contiene exactamente los nombres de los estudiantes que tienen al menos una calificación menor a nota_minima, sin repetidos }
}

Ejemplo: {"Ana": [10, 9], "Beto": [8], "Cami": [7, 8, 9], "Dani": [6, 3]}, nota_minima = 7 → ["Dani"]. Es el complemento de "destacado" del parcial.
'''
def estudiantes_con_alguna_nota_baja(calificaciones: dict[str, list[int]], nota_minima: int) -> list[str]:
    res: list[str] = []

    for nombre in calificaciones:
        tiene_nota_baja: bool = False
        for nota in calificaciones[nombre]:
            if nota < nota_minima:
                tiene_nota_baja = True

        if tiene_nota_baja:
            res.append(nombre)

    return res

'''
problema clave_con_mayor_valor (in d: dict⟨String, Z⟩) : String {
  requiere: { d no es vacío }
  requiere: { Todos los valores de d son distintos entre sí }
  asegura: { res es una clave de d tal que d[res] >= d[c] para toda clave c de d }
}

Ejemplo: {"a": 3, "b": 9, "c": 5} → "b". Es el equivalente a maximo_lista, pero sobre valores de un diccionario.
'''
def clave_con_mayor_valor(d: dict[str, int]) -> str:
    mejor_clave: str = ""
    mejor_valor: int = 0
    primera: bool = True

    for clave in d:
        if primera or d[clave] > mejor_valor:
            mejor_clave = clave
            mejor_valor = d[clave]
            primera = False

    return mejor_clave

'''
problema agrupar_por_longitud (in palabras: seq⟨String⟩) : dict⟨Z, seq⟨String⟩⟩ {
  requiere: { - }
  asegura: { Una clave n de res existe si y sólo si existe al menos una palabra de palabras de longitud n }
  asegura: { Para toda clave n de res, res[n] contiene exactamente las palabras de palabras de longitud n, en el mismo orden en que aparecen en palabras }
}

Ejemplo: ["sol", "cielo", "luz", "nube"] → {3: ["sol", "luz"], 5: ["cielo"], 4: ["nube"]}.
'''
def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    res: dict[int, list[str]] = {}

    for palabra in palabras:
        n: int = len(palabra)
        if n in res:
            res[n].append(palabra)
        else:
            res[n] = [palabra]

    return res

'''
problema agrupar_por_inicial (in nombres: seq⟨String⟩) : dict⟨String, seq⟨String⟩⟩ {
  requiere: { Todos los nombres de nombres tienen al menos un carácter }
  asegura: { Una clave k de res existe si y sólo si existe un nombre en nombres cuya primera letra es k }
  asegura: { Para toda clave k de res, res[k] contiene exactamente los nombres de nombres que empiezan con k, en el mismo orden en que aparecen en nombres }
}

Ejemplo: ["Ana", "Beto", "Alan", "Bruno", "Cami"] → {"A": ["Ana", "Alan"], "B": ["Beto", "Bruno"], "C": ["Cami"]}.
'''
def agrupar_por_inicial(nombres: list[str]) -> dict[str, list[str]]:
    res: dict[str, list[str]] = {}

    for nombre in nombres:
        inicial: str = nombre[0]
        if inicial in res:
            res[inicial].append(nombre)
        else:
            res[inicial] = [nombre]

    return res

'''
problema frecuencia_de_elementos (in s: seq⟨Z⟩) : dict⟨Z, Z⟩ {
  requiere: { - }
  asegura: { Una clave x de res existe si y sólo si x aparece en s }
  asegura: { Para toda clave x de res, res[x] es la cantidad de veces que x aparece en s }
}

Ejemplo: [3, 1, 3, 2, 1, 3] → {3: 3, 1: 2, 2: 1}.
'''
def frecuencia_de_elementos(s: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}

    for elem in s:
        if elem in res:
            res[elem] += 1
        else:
            res[elem] = 1

    return res

'''
problema elemento_mas_frecuente (in s: seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { res es un elemento de s tal que su cantidad de apariciones en s es mayor o igual que la de cualquier otro elemento de s }
}

Ejemplo: [4, 2, 4, 7, 2, 4] → 4. Si hay empate, cualquiera de los empatados es válido. Se resuelve combinando el 6 con el 3.
'''
def frecuencia_de_elementos(s: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}
    for elem in s:
        if elem in res:
            res[elem] += 1
        else:
            res[elem] = 1
    return res

def elemento_mas_frecuente(s: list[int]) -> int:
    frecuencias: dict[int, int] = frecuencia_de_elementos(s)

    mejor_elem: int = s[0]
    mejor_cant: int = frecuencias[s[0]]

    for elem in frecuencias:
        if frecuencias[elem] > mejor_cant:
            mejor_elem = elem
            mejor_cant = frecuencias[elem]

    return mejor_elem

'''
problema unir_sumando (in d1: dict⟨String, Z⟩, in d2: dict⟨String, Z⟩) : dict⟨String, Z⟩ {
  requiere: { - }
  asegura: { Una clave c de res existe si y sólo si c es clave de d1 o de d2 }
  asegura: { Si c es clave de d1 y de d2, res[c] = d1[c] + d2[c] }
  asegura: { Si c es clave solo de d1, res[c] = d1[c]; si c es clave solo de d2, res[c] = d2[c] }
}

Ejemplo: {"a": 1, "b": 2} y {"b": 5, "c": 7} → {"a": 1, "b": 7, "c": 7}.
'''
def unir_sumando(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    res: dict[str, int] = {}

    # Paso 1: copiar todo d1
    for clave in d1:
        res[clave] = d1[clave]

    # Paso 2: agregar d2, sumando si la clave ya está
    for clave in d2:
        if clave in res:
            res[clave] += d2[clave]
        else:
            res[clave] = d2[clave]

    return res
