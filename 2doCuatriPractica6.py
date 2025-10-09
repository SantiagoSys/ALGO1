# EJERCICIO 1
'''
 1. problema imprimir_hola_mundo () {
 requiere: { True }
 asegura: { imprime “¡Hola mundo!"por consola}
 }
'''
def imprimir_hola_mundo () -> None:
    x = "Hola mundo"
    return x

saludo = imprimir_hola_mundo ()
print(saludo)

'''
 2. imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de línea mediante
 el caracter \n.
'''
def imprimir_un_verso () -> None:
    x = "Soy\nSantiago\nSuarez"
    return x

verso = imprimir_un_verso ()
print(verso)

'''
 3. raizDe2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round
'''
def raizDe2 () -> None:
    print(round(2**(1/2), 4))

print(raizDe2())

'''
 4. factorial_de_dos()
 problema factorial_2 () : Z {
 requiere: { True }
 asegura: {res = 2!}
 }
'''
def factorial_de_dos () -> None:
    print(2*1)

factorial = factorial_de_dos ()
print(factorial)

'''
perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando
 import math y la constante math.pi
 problema perimetro () : R {
 requiere: { True }
 asegura: {res = 2×π }
 }
'''
import math
def perimetro () -> None:
    print(2*math.pi)

perimetro = perimetro ()
print(perimetro)


# EJERCICIO 2
'''
 1. problema imprimir_saludo (in nombre: String) {
 requiere: { True }
 asegura: {imprime “Hola < nombre >"por pantalla}
 }
'''
def imprimir_saludo (nombre: str) -> None:
    print("Hola", nombre)

saludo_personal = imprimir_saludo ("Santiago")
print(saludo_personal)

print("\n")

'''
 2. raiz_cuadrada_de(numero): que devuelva la raíz cuadrada del número.
'''
def raiz_cuadrada_de (numero: int) -> None:
    print(numero**(1/2))

raiz_cuadrada = raiz_cuadrada_de (4)
print(raiz_cuadrada)

print("\n")

'''
 3. fahrenheit_a_celsius(temp_far): que convierta una temperatura en grados Fahrenheit a grados Celcius.
 problema fahrenheit_a_celsius (in t: R) : R {
 requiere: { True }
 asegura: {res = ((t−32)×5)/9}
 }
'''
def farenheit_a_celsius (temp_far: float) -> float:
    print(((temp_far-32)*5)/9)

temperatura = farenheit_a_celsius (41.0)
print(temperatura)

print("\n")

'''
4. imprimir_dos_veces(estribillo): que imprima dos veces el estribillo de una canción. Nota: Analizar el comporta
miento del operador (*) con strings.
'''
def imprimir_dos_veces (estribillo: str) -> str:
    print(estribillo*2)

estribillo_doble = imprimir_dos_veces("Let me take the suffering from you.")
print(estribillo_doble)

print("\n")

'''
 5. problema es_multiplo_de (in n: Z, in m:Z) : Bool {
 requiere: {m̸ = 0}
 asegura: {(res = true) ↔ (existe un k ∈ Z tal que n = m×k)}
 }
'''
def es_multiplo_de (n: int, m: int) -> bool:
    resto_n_m: int = n % m
    return resto_n_m == 0

print(es_multiplo_de (2,3))
print(es_multiplo_de (2,4))
print(es_multiplo_de (16,4))

print("\n")

'''
 6. es_par(numero): que indique si numero es par (usar la función es_multiplo_de()).
'''
def es_par (numero: int) -> bool:
    return es_multiplo_de(numero, 2)

print(es_par(4))
print(es_par(5))
print(es_par(-1))

print("\n")

'''
 7. cantidad_de_pizzas(comensales, min_cant_de_porciones) que devuelva la cantidad de pizzas que necesitamos
 para que cada comensal coma como mínimo min_cant_de_porciones porciones de pizza. Considere que cada pizza
 tiene 8 porciones y que se prefiere que sobren porciones.
'''
def cantidad_de_pizzas (comensales: int, min_cant_de_porciones) -> int:
    return round((comensales * min_cant_de_porciones)/8)

print("\n")


# EJERCICIO 3
'''
 1. alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0.
'''
def alguno_es_0 (numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

print(alguno_es_0(1,1))
print(alguno_es_0(1,0))
print(alguno_es_0(0,1))
print(alguno_es_0(0,0))

print("\n")

'''
 2. ambos_son_0(numero1, numero2): dados dos números racionales, decide si ambos son iguales a 0.
'''
def ambos_son_0 (numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

print(ambos_son_0(1,1))
print(ambos_son_0(1,0))
print(alguno_es_0(0,1))
print(alguno_es_0(0,0))

print("\n")

'''
 3. problema es_nombre_largo (in nombre: String) : Bool {
 requiere: { True }
 asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
 }
'''
def es_nombre_largo (nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

print(es_nombre_largo("Santiago"))

print("\n")

'''
 4. es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400, o bien
 es múltiplo de 4 pero no de 100.
'''
def es_bisiesto (año: int) -> bool:
    return es_multiplo_de (año,400) or (es_multiplo_de (año,4) and not (es_multiplo_de (año,100)))

print(es_bisiesto(2024))
print(es_bisiesto(2000))
print(es_bisiesto(1900))
print(es_bisiesto(2025))

print("\n")


# EJERCICIO 4
'''
En una plantación de pinos, de cada árbol se conoce la altura expresada en metros. El peso de un pino se puede estimar
 a partir de la altura de la siguiente manera:
 3 kg por cada centímetro hasta 3 metros,
 2 kg por cada centímetro arriba de los 3 metros.
 Por ejemplo:
 2 metros pesan 600 kg, porque 200 * 3 = 600
 5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.
 Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos, un pino
 fuera de este rango no le sirve a la fábrica.
 Definir las siguientes funciones, deducir qué parámetros tendrán a partir del enunciado. Se pueden usar funciones auxiliares
 si fuese necesario para aumentar la legibilidad.
 1. Definir la función peso_pino
 2. Definir la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.
 3. Definir la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
 4. Definir sirve_pino usando composición de funciones.
'''
def peso_pino (metros: float) -> float:
    altura: float = metros * 100
    if altura <= 300:
        peso: float = altura*3
    else:
        peso: float = 300*3 + (altura-300)*2
    return peso

print(peso_pino(2))
print(peso_pino(5))
print("\n")

def es_peso_util (peso: float) -> bool:
    return peso >= 400 and peso <= 1000

print(es_peso_util(500))
print(es_peso_util(300))
print("\n")

def sirve_pino (metros: float) -> bool:
    return 400 <= peso_pino(metros) <= 1000

print(sirve_pino(3))
print(sirve_pino(7))
print("\n")

def sirve_pino1 (metros: float) -> bool:
    return es_peso_util(peso_pino(metros))

print(sirve_pino(3))
print(sirve_pino(7))
print("\n")


# EJERCICIO 5
'''
1. devolver_el_doble_si_es_par(numero); que devuelve el doble del número en caso de ser par y el mismo número en
 caso contrario.
'''
def devolver_el_doble_si_es_par (numero: int) -> int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero

print(devolver_el_doble_si_es_par(2))
print(devolver_el_doble_si_es_par(3))
print("\n")

'''
2. devolver_valor_si_es_par_si_no_el_que_sigue(numero): devuelve el mismo número si es par, y si no, el siguiente.
 Analizar distintas formas de implementación (usando un if-then-else y dos if). ¿Todas funcionan?
'''
def devolver_valor_si_es_par_si_no_el_que_sigue (numero: int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero+1
'''
 3. devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero): en otro caso, devolver el número ori
ginal. Analizar distintas formas de implementación (usando un if-then-else, dos if, o alguna opción de operación
 lógica). ¿Todas funcionan? ¿Cuál es el resultado si la entrada es 18?
'''
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero: int) -> int:
    if es_multiplo_de(numero, 9):
        return numero*3
    elif es_multiplo_de(numero,3):
        return numero*2
    else:
        return numero

x = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(3)
y = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(9)
z = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(7)    
print(x)
print(y)
print(z)

'''
 4. lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga “Tu
 nombre tiene muchas letras!” y si no, “Tu nombre tiene menos de 5 caracteres”.
'''
def lindo_nombre (nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
print(lindo_nombre("Santiago"))
print(lindo_nombre("Sol"))
print("\n")

'''
 5. elRango(numero) que imprime por pantalla “Menor a 5” si el número es menor a 5, “Entre 10 y 20” si el número está
 en ese rango y “Mayor a 20” si el número es mayor a 20.
'''
def el_rango (numero: int) -> str:
    if numero < 5:
        return "Menor a 5"
    elif 10 <= numero <= 20:
        return "Entre 10 y 20"
    else:
        return "Mayor a 20"

print(el_rango(4))
print(el_rango(11))
print(el_rango(21))
print("\n")

'''
 6. En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan
 a los 65 años. Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de
 las personas se les ordena ir a trabajar. Implemente una función que, dados los parámetros de sexo (F o M) y edad,
 imprima la frase que corresponda según el caso: “Andá de vacaciones” o “Te toca trabajar”.
'''
def situacion_laboral (sexo: chr, edad: int) -> str:
    if (sexo == 'F' and edad >= 60) or (sexo == 'M' and edad >= 65) or (edad < 18):
        return "Andá de vacaciones"
    else:
        return "Te toca trabajar"
    
print(situacion_laboral('F', 60))
print(situacion_laboral('M', 65))
print(situacion_laboral('F', 17))
print(situacion_laboral('M', 17))
print(situacion_laboral('F', 18))
print(situacion_laboral('M', 18))
print("\n")


# EJERCICIO 6
'''
 1. Escribir una función que imprima los números del 1 al 10.
'''
def imprimir_numeros () -> None:
    i: int = 1
    while i <= 10:
        print(i)
        i += 1
imprimir_numeros()

'''
 2. Escribir una función que imprima los números pares entre el 10 y el 40.
'''
def imprimir_pares () -> None:
    i: int = 10
    while i <= 40:
        print(i)
        i += 2
imprimir_pares()

'''
 3. Escribir una función que imprima la palabra “eco” 10 veces.
'''
def imprimir_eco () -> None:
    print("eco\n"*10)
imprimir_eco()

'''
 4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me
 pasan por parámetro (que será positivo) hasta el 1, y por último “Despegue”.
'''
def cuenta_regresiva (i: int) -> None:
    while i >= 1:
        print(i)
        i -= 1
    print("Despegue!!!")
cuenta_regresiva(10)

'''
 5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, “el año de partida” y
 “algún año de llegada”, siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos
 de un año y la función debe mostrar el texto: “Viajó un año al pasado, estamos en el año: <año>” cada vez que se
 realice un salto de año.
'''
def viaje_en_el_tiempo (año_partida: int, año_llegada: int) -> None:
    while año_partida > año_llegada:
        print("Viajó un año al pasado, estamos en el año: ", año_partida-1)
        año_partida -= 1
viaje_en_el_tiempo(2025, 2000)

'''
 6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
 al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada
 salto!
'''
def viaje_en_el_tiempo2 (año_partida: int) -> None:
    while año_partida > -384:
        año_partida -= 20
        print("Viajó 20 años al pasado, estamos en el año: ", año_partida)
viaje_en_el_tiempo2(2025)


# EJERCICIO 7
'''
 1. Escribir una función que imprima los números del 1 al 10.
'''
def imprimir_numeros2 () -> None:
    for num in range(1, 10, 1):
        print(num)
imprimir_numeros2()

'''
 2. Escribir una función que imprima los números pares entre el 10 y el 40.
'''
def imprimir_pares2 () -> None:
    for num in range (10,40,2):
        print(num)
imprimir_pares2()

'''
 3. Escribir una función que imprima la palabra “eco” 10 veces.
'''
def imprimir_eco2 () -> None:
    for eco in range (10):
        print("eco")
imprimir_eco2()

'''
 4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me
 pasan por parámetro (que será positivo) hasta el 1, y por último “Despegue”.
'''
def cuenta_regresiva2 (num) -> None:
    for i in range (0, num, 1):
        print(num)
        num -= 1
    print ("Despegue!!")
cuenta_regresiva2(11)

'''
 5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, “el año de partida” y
 “algún año de llegada”, siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos
 de un año y la función debe mostrar el texto: “Viajó un año al pasado, estamos en el año: <año>” cada vez que se
 realice un salto de año.
'''
def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> None:
    for num in range (año_llegada, año_partida, 1):
        año_partida -= 1
        print("Viajó un año al pasado, estamos en el año:", año_partida)

'''
 6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
 al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada
 salto!
'''
def viaje_en_el_tiempo2(año_partida: int) -> None:
    for num in range (384, año_partida, 20):
        print("Viajó 20 años al pasado, estamos en el año:", año_partida)
        año_partida -= 20
