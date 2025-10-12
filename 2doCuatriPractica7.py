# EJERCICIO 1
'''
 1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
 requiere: { True }
 asegura: { (res = true) ↔ (existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
 }
 Implementar al menos de 3 formas distintas este problema.
'''
def pertenece (s: list[int], e: int) -> bool:
    for i in s:
        if s[i] == e:
            return True
        else:
            return False
print(pertenece([1,2,3,4],1))

def pertenece2 (s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if s[i] == e:
            return True
        else:
            return False
print(pertenece2([1,2,3,4],1))

def pertenece3(s: list[int], e: int)-> bool:
    longitud = len(s) - 1

    while(longitud >= 0):
        if(s[longitud] == e):
            return True
        longitud -= 1
    return False
print(pertenece3([1,2,3,4], 1))
print("\n")

'''
 2. problema divide_a_todos (in s:seq⟨Z⟩, in e: Z) : Bool {
 requiere: { e ̸ = 0 }
 asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
 }
'''
def divide_a_todos (s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if s[i] % e != 0:
            return False
    return True
print(divide_a_todos([4,4,4,4], 2))
print("\n")

'''
 3. problema suma_total (in s:seq⟨Z⟩) : Z {
 requiere: { True }
 asegura: { res es la suma de todos los elementos de s }
 }
 Nota: no utilizar la funcion sum() nativa.
'''
def suma_total (s: list[int]) -> int:
    res: int = 0
    for i in range(len(s)):
        res = res + s[i]
    return res
print(suma_total([1,2,3,4]))
print("\n")

'''
 4. problema maximo (in s:seq⟨Z⟩) : Z {
 requiere: { |s| > 0 }
 asegura: { res = al mayor de todos los numeros que aparece en s }
 }
 Nota: no utilizar la funcion max() nativa.
'''
def maximo (s: list[int]) -> int:
    res = s[0]
    for i in range(1,len(s)):
        if s[i] >= res:
            res = s[i]
    return res
print(maximo([1,2,3,4]))
print("\n")

'''
5. problema minimo (in s:seq⟨Z⟩) : Z {
 requiere: { |s| > 0 }
 asegura: { res = al menor de todos los numeros que aparece en s }
 }
 Nota: no utilizar la funcion min() nativa.
'''
def minimo (s: list[int]) -> int:
    res = s[0]
    for i in range(1,len(s)):
        if s[i] <= res:
            res = s[i]
    return res
print(minimo([1,2,3,4]))
print("\n")

'''
 6. problema ordenados (in s:seq⟨Z⟩) : Bool {
 requiere: { True }
 asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s|−1) → s[i] < s[i+1] }
 }
'''
def ordenados (s: list[int]) -> bool:
    res = True
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            res = False
    return res
print(ordenados([1,2,3,4]))
print(ordenados([4,3,2,1]))
print("\n")

'''
 7. problema pos_maximo (in s:seq⟨Z⟩) : Z {
 requiere: { True }
 asegura: { (Si |s| = 0, entonces res = −1; si no, res = al índice de la posicion donde aparece el mayor elemento
 de s (si hay varios es la primera aparicion) }
 }
'''
def pos_maximo (s: list[int]) -> int:
    if len(s) == 0:
        res = -1
    else:
        maximo: int = s[0]
        indice: int = 0
        for i in range(len(s)):
            if s[i] > maximo:
                maximo = s[i]
                indice = i
        return indice
    
print(pos_maximo([1,2,4,56,2]))
print(pos_maximo([56,2,4,56,2]))
print("\n")

'''
 8. problema pos_minimo (in s:seq⟨Z⟩) : Z {
 requiere: { True }
 asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ındice de la posicion donde aparece el menor elemento
 de s (si hay varios es la ultima aparicion) }
 }
'''
def pos_minimo (s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        minimo: int = s[0]
        indice: int = 0
        for i in range(len(s)):
            if s[i] <= minimo:
                minimo = s[i]
                indice = i
        return indice
print(pos_minimo([1,2,4,56,2]))
print(pos_minimo([56,2,4,56,2]))
print("\n")

'''
 9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
 [“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
 problema long
 mayorASiete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
 requiere: { True }
 asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s|−1)) y (|s[i]| > 7) }
 }
'''
def mayor_a_siete (s: list[str]) -> bool:
    res = False
    for i in range(len(s)):
        if len(s[i]) > 7:
            res = True
    return res
print(mayor_a_siete(["Cubo", "Circulo", "Triangulo"]))
print(mayor_a_siete(["Cubo", "Circulo"]))
print("\n")

'''
 10. Dado un texto en formato string, devolver verdadero si es palíndromo (se lee igual en ambos sentidos), falso en caso
 contrario. Las cadenas de texto vacías o con 1 solo elemento son palíndromo.
 problema es_palindromo (in s:seq⟨Char⟩) : Bool {
 requiere: { True }
 asegura: { (res = true) ↔ (s es igual a su reverso) }
 }
'''
def es_palindromo (s: str) -> bool:
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
print(es_palindromo("hannah"))
print(es_palindromo("gaspar"))
print("\n")

'''
 11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 numeros iguales consecutivos, en cualquier posicion y False en caso
 contrario.
 problema iguales_consecutivos (in s:seq⟨Z⟩) : Bool {
 requiere: { True }
 asegura: { (res = true) ↔ (existe i,j,k ∈ Z tal que (0 ≤ i,j,k < (|s| − 1)) y (i + 2 = j + 1 = k) y
 (s[i] = s[j] = s[k])) }
 }
'''
def iguales_consecutivos (s: list[int]) -> bool:
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            return True
    return False
print(iguales_consecutivos([1,1,1,4]))
print(iguales_consecutivos([4,1,1,1]))
print(iguales_consecutivos([1,2,3,4]))
print("\n")

'''
 12. Recorrer una palabra en formato string y devolver True si esta tiene al menos 3 vocales distintas y False en caso
 contrario.
 problema vocales_distintas (in s:seq⟨Char⟩) : Bool {
 requiere: { True }
 asegura: { (res = true) ↔ (existe i,j,k ∈ Z tal que (0 ≤ i,j,k < (|s| − 1)) y (s[i] ̸ = s[j] ̸ = s[k]) y
 (s[i], s[j], s[k] ∈ {‘a‘,‘e‘, ‘i‘, ‘o‘, ‘u‘})) }
 }
'''
def vocales_distintas (s: str) -> bool:
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u']
    vocales_palabra: list[str] = []

    for i in range(len(s)):
        if s[i] in vocales and s[i] not in vocales_palabra:
            vocales_palabra.append(s[i])
    
    if len(vocales_palabra) >= 3:
        return True
    return False

print(vocales_distintas("Santiago"))
print(vocales_distintas("Santi"))
print(vocales_distintas("Amanda"))
print("\n")

'''
13. Recorrer una seq⟨Z⟩ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos
 subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vacía.
 problema pos_secuencia_ordenada_mas_larga (in s:seq⟨Z⟩) : Z {
 requiere: { |s| > 0 }
 asegura: { (res = i) ↔ (existe i,j ∈ Z tal que (0 ≤ i,j < (|s|-1)) y i ≤ j y (para todo k tal que i ≤ k < j →
 s[k] ≤ s[k + 1]) y j-i+1 es máximo e i es el mínimo valor que lo cumple) }
 }
'''
def pos_secuencia_ordenada_mas_larga (s: list[int]) -> int:
    cantidad: int = 0
    indice: int
    cantidad_mayor: int = 0
    indice_mayor: int
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] + 1 == s[i+1]:
            if cantidad == 0:
                indice = i
            cantidad += 1
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                indice_mayor = indice
        else:
            cantidad = 0
    return indice_mayor
print(pos_secuencia_ordenada_mas_larga([1,2,3,0,1,2,3,4,0,1,2,3]))
print(pos_secuencia_ordenada_mas_larga([0,1,2,0,10,11,12,13]))
print(pos_secuencia_ordenada_mas_larga([0,1,2,3,0,1,2,3,0,1,2,3]))
print("\n")

'''
 14. Cantidad de dígitos impares.
 problema cantidad_digitos_impares (in s:seq⟨Z⟩) : Z {
 requiere: { Todos los elementos de números son mayores o iguales a 0 }
 asegura: { res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números }
 }
 Por ejemplo, si la lista de números es [57, 2383, 812, 246], entonces el resultado esperado sería 5 (los dígitos impares
 son 5, 7, 3, 3 y 1).
'''
def cantidad_digitos_impares(s: list[int]) -> int:
    res: int = 0
    for i in range(len(s)):
        numero: int = s[i]
        while numero > 0:
            digito: int = numero % 10
            if digito % 2 != 0:
                res += 1
            numero = numero // 10
    return res
print(cantidad_digitos_impares([57, 2383, 812, 246]))
print(cantidad_digitos_impares([22,46,88,26]))
print(cantidad_digitos_impares([22,46,88,26,77,54]))


# EJERCICIO 2
'''
 1. problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
 requiere: { True }
 modifica: { s }
 asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
 es par, entonces s[i] = 0) }
 }
'''
def ceros_en_posiciones (s: list[int]) -> list[int]:
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0
    return s
print(ceros_en_posiciones([3,3,3,3,3,3]))
print("\n")

'''
 2. problema CerosEnPosicionesPares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: { True }
 asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es
 par, entonces res[i] = 0) }
 }
'''
'''
 3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
 sino que borra la vocal y concatena a continuación.
 problema sin_vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
 requiere: { True }
 asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
 }
''' # ???
def sin_vocales (s: str) -> str:
    vocales: str = ['a', 'e', 'i', 'o', 'u']
    res = ""
    for i in range(len(s)):
        if s[i] not in vocales:
            res += s[i]
    return res
print(sin_vocales("Hola"))
print("\n")

'''
 Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena
 original, conservando el orden de los elementos restantes.
 4. problema reemplaza
 vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
 requiere: { True }
 asegura: { |res| = |s| }
 asegura: { Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
 (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i])) }
 }
'''
def reemplaza_vocales (s: str) -> str:
    vocales: str = ['a', 'e', 'i', 'o', 'u']
    res = ""
    for i in range(len(s)):
        if s[i] in vocales:
            res += " "
        else:
            res += s[i]
    return res
print(reemplaza_vocales("Hola"))
print("\n")

'''
5. problema da_vuelta
 str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
 requiere: { True }
 asegura: { |res| = |s| }
 asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s|−i−1] }
 }
'''
def da_vuelta (s: str) -> str:
    palabra_invertida: str = ""

    for i in range(len(s)):
        letra = s[len(s) - 1 - i]
        palabra_invertida += letra

    return palabra_invertida

print(da_vuelta("Hola"))
print("\n")

'''
 6. problema eliminar_repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
 requiere: { True }
 asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i],res)) ∧ (para todo i,j ∈ Z si
 (0 ≤ i,j < |res|∧i ̸ = j) → res[i] ̸ = res[j]) }
 }
'''
def pertenece_mas_de_una_vez (palabra: str, letra: str) -> bool:
    repeticiones: int = 0

    for i in range(len(palabra)):
        if letra == palabra[i]:
            repeticiones += 1

    if repeticiones > 1:
        return True
    return False

def eliminar_repetidos (s: str) -> str:
    palabras_sin_repetidos: str = ""

    for i in range(len(s)):
        if pertenece_mas_de_una_vez(s, s[i]):
            palabras_sin_repetidos += ""
        else:
            palabras_sin_repetidos += s[i]
    return palabras_sin_repetidos

print(eliminar_repetidos("fafefifofu"))
print("\n")

'''
 Ejercicio 3. Implementar una funcion para conocer el estado de aprobacion de una materia a partir de las notas obtenidas
 por un/a alumno/a cumpliendo con la siguiente especificacion:
 problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
 requiere: { |notas| > 0 }
 requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
 asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
 asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio esta entre 4 (inclusive) y 7 }
 asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
 }
'''
def suma_notas (notas: list[int]) -> int:
    res = 0
    for i in range(len(notas)):
        res += notas[i]
    return res

def promedio_notas (notas: list[int]) -> int:
    res: float = suma_notas(notas) / len(notas)
    return res
print(promedio_notas([10,10,10,10]))

def notas_aprobadas (notas: list[int]) -> bool:
    for i in range(len(notas)):
        if notas[i] < 4:
            return False
    return True

def resultado_materia (notas: list[int]) -> int:
    if notas_aprobadas(notas) and (promedio_notas(notas) >= 7):
        res = 1
    elif notas_aprobadas(notas) and (4 <= promedio_notas(notas) < 7):
        res = 2
    elif not notas_aprobadas(notas) or (promedio_notas(notas) < 4):
        res = 3
    return res

print(resultado_materia([7,8,9,10])) # Debe devolver 1
print(resultado_materia([5,6,7]))    # Debe devolver 2
print(resultado_materia([1,10,10]))  # Debe devolver 3
print(resultado_materia([1,2,3]))    # Debe devolver 3
print("\n")

'''
 Ejercicio 4. Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo
 actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso
 de dinero y “R” para retiro de dinero, y ademas el monto de cada operacion. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
 2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280.
 problema saldoActual (in movimientos: seq⟨Char × Z⟩) : Z {
 requiere: { Para todo i ∈ Z si 0 ≤ i < |movimientos| → movimientos[i]0 ∈ {“I”,“R”} y movimientos[i]1 > 0 }
 asegura: { res = ingresos
 i
 }
'''
def saldo_actual (movimientos: list[(chr, int)]) -> int:
    saldo: int = 0
    for operacion in movimientos:
        if operacion[0] == 'I':
            saldo += operacion[1]
        elif operacion[0] == 'R':
            saldo -= operacion[1]
    return saldo

print(saldo_actual([('I',2000), ('R', 20),('R', 1000),('I', 300)]))
print("\n")


# EJERCICIO 3
'''
1. problema pertenece
 a
 cada
 uno
 version
 movimientos[i]1 }
 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
 requiere: { True }
 asegura: { |res| ≥ |s| }
 asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i],e)) }
 }
 Nota: Reutilizar la función pertenece() implementada previamente para listas.
'''
def pertenece (s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False

def pertenece_a_cada_uno_version1 (s: list[list[int]], e: int, res: list[bool]) -> None:
    res.clear()
    for i in range(len(s)):
        res.append(pertenece(s[i], e))

    return res

print(pertenece_a_cada_uno_version1([[4,5,6], [7,8,10], [4,4,4]], 4, [True, False, True]))
print("\n")

'''
 2. problema pertenece
 a
 cada
 uno
 version
 2 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
 requiere: { True }
 asegura: { |res| = |s| }
 asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i],e)) }
 }
'''
'''
 3. problema pertenece
 a
 cada
 uno
 requiere: { True }
 asegura: { |res| = |s| }
 version
 3 (in s:seq⟨seq⟨Z⟩⟩, in e:Z) : seq⟨Bool⟩ {
 asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i],e)) }
 }
'''
'''
4. Pensar: ¿C´omo cambia este problema respecto de la versi´on 1? Pensar en relaci´on de fuerza entre: implementaci´on en
 Python y las especificaciones. ¿Se puede usar la implementaci´on del ejercicio 2 para la especificaci´on del 1? ¿Se puede
 usar la implementaci´on del ejercicio 1 para la especificaci´on del 2? Justificar su respuesta.
 Ejercicio 6. Implementar las siguientes funciones sobre matrices (secuencias de secuencias):
'''
'''
 1. problema es
 matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
 requiere: { True }
 asegura: { res = true ↔ (|s| > 0)∧(|s[0]| > 0)∧(Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|) }
 }
'''
def es_matriz (s: list[list[int]]) -> bool:
    for i in range(len(s)):
        if len(s) > 0 and len(s[0]) > 0 and len(s[i] == len(s[0])):
            return True
    return False

'''
 2. problema filas
 ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
 requiere: { esMatriz(m) }
 asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
 }
 Nota: Reutilizar la función ordenados() implementada previamente para listas
'''
def filas_ordenadas (m: list[list[int]], res: list[bool]):
    res: list[bool] = []
    for i in range(len(m)):
        res.append(ordenados(m[i]))
    return res

m = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
res = [True, True, True]
print(filas_ordenadas(m, res))
print("\n")

'''
 3. problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
 requiere: { esMatriz(m) }
 requiere: { c < |m[0]| }
 requiere: { c ≥ 0 }
 asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
 el mismo orden que aparecen }
 }
'''
def columna (m: list[list[int]], c: int) -> list[int]:
    res: list[int] = []

    for fila in m:
        elemento: int = fila[c]
        res.append(elemento)
    
    return res

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

print(columna(m1, 0)) # Debe devolver [1, 4, 7]
print(columna(m1, 1)) # Debe devolver [2, 5, 8]
print(columna(m1, 2)) # Debe devolver [3, 6, 9]
print("\n")

'''
 4. problema columnas
 ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
 requiere: { esMatriz(m) }
 asegura: { Para todo índice de columna c: 0 ≤ c < |m[0]| → (res[c] = true ↔ ordenados(columna(m,c))) }
 asegura: {|res| = |m[0]|}
 }
 Nota: Reutilizar la función ordenados() implementada previamente para listas
'''
def columnas_ordenadas (m: list[list[int]]) -> list[bool]:
    res: list[bool] = []

    for i in range(len(m[0])):
        if ordenados(columna(m, i)):
            res.append(True)
        else:
            res.append(False)

    return res

print(columnas_ordenadas(m1)) # Debe devolver [True, True, True]
print("\n")

'''
 5. problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
 requiere: { esMatriz(m) }
 asegura: { Devuelve mt (o sea la matriz transpuesta) }
 }
 Nota: Usar columna() para ir obteniendo todas las columnas de la matriz.
'''

def transponer (m: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []

    for i in range(len(m[0])):
        res.append(columna(m, i))

    return res

print(transponer(m1))
print("\n")

'''
 6. Ta-Te-Ti Tradicional:
 problema quien
 gana
 tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
 requiere: { esMatriz(m) }
 requiere: { |m| = 3 }
 requiere: { |m[0]| = 3 }
 requiere: { En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente }
 requiere: { En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente }
 requiere: { En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente }
 requiere: { En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente }
 requiere: { Para todo i,j ∈ {0,1,2} =⇒ m[i][j] = X ∨ m[i][j] = O ∨ m[i][j] = ” ”}
 asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
 asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
 asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }
 }
'''
'''
7. Opcional: Implementar una función que tome un entero d y otro p y eleve una matriz cuadrada de tama˜no d con
 valores generados al azar a la potencia p. Es decir, multiplique a la matriz generada al azar por sí misma p veces.
 Realizar experimentos con diferentes valores de d. ¿Qué pasa con valores muy grandes?
 problema exponenciacion
 matriz (in d:Z, in p:Z) : seq⟨seq⟨Z⟩⟩ {
 requiere: { d,p ∈ Z y d,p > 0 }
 asegura: { esMatriz(m) y |columna(m,0)| = d y |columna(transponer(m),0)| = d y res = p
 i=1m }
 }
 Nota 1: recordá que en la multiplicaci´on de una matriz cuadrada de dimensi´on d por si misma cada posici´on se calcula
 como res[i][j] = d−1
 k=0(m[i][k] × m[k][j])
 Nota 2: para generar una matriz cuadrada de dimensi´on d con valores aleatorios hay muchas opciones de implemen
taci´on, analizar las siguientes usando la biblioteca numpy (ver recuadro):
 Opci´on 1:
 import numpy as np
 m = np.random.random((d, d))1
 Opci´on 2:
 import numpy as np
 m = np.random.randint(i,f, (d, d))2
'''
'''
 Ejercicio 7. Vamos a elaborar programas interactivos (usando la funci´on input()3) que nos permita solicitar al usuario
 informaci´on cuando usamos las funciones.
 1. Implementar una funci´on para construir una lista con los nombres de mis estudiantes. La funci´on solicitar´a al usuario
 los nombres hasta que ingrese la palabra “listo”, o vac´ıo (el usuario aprieta ENTER sin escribir nada). Devuelve la
 lista con todos los nombres ingresados.
 2. Implementar una funci´on que devuelve una lista con el historial de un monedero electr´onico (por ejemplo la SUBE).
 El usuario debe seleccionar en cada paso si quiere:
 “C” = Cargar cr´editos,
 “D” = Descontar cr´editos,
 “X” = Finalizar la simulaci´on (terminar el programa).
 En los casos de cargar y descontar cr´editos, el programa debe adem´as solicitar el monto para la operaci´on. Vamos a
 asumir que el monedero comienza en cero. Para guardar la informaci´on grabaremos en el historial tuplas que representen
 los casos de cargar (“C”, monto a cargar) y descontar cr´edito (“D”, monto a descontar).
 3. Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deber´a generar un n´umero
 aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber´a luego preguntarle al usuario si desea seguir sacando otra “carta”
 o plantarse. En este ´ultimo caso el programa debe terminar. Los n´umeros aleatorios obtenidos deber´an sumarse seg´un
 el n´umero obtenido salvo por las “figuras” (10, 11 y 12) que sumar´an medio punto cada una. El programa debe ir
 acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funci´on devuelve
 el historial de “cartas” que hizo que el usuario gane o pierda. Para generar n´umeros pseudo-aleatorios entre 1 y 12
 utilizaremos la funci´on random.randint(1,12). Al mismo tiempo, la funci´on random.choice() puede ser de gran
 ayuda a la hora de repartir cartas.
 4. Analizar la fortaleza de una contrase˜na. Solicitar al usuario que ingrese un texto que ser´a su contrase˜na. Armar una
 funci´on que tenga de par´ametro de entrada un string con la contrase˜na a analizar, y la salida otro string con tres
 posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “˜n/˜ N” es considerado un car´acter especial y no
 se comporta como cualquier otra letra. String es seq⟨Char⟩. Consejo: para ver si una letra es may´uscula se puede ver
 si est´a ordenada entre A y Z.
 La contrase˜na ser´a VERDE si:
 a) la longitud es mayor a 8 caracteres
 b) tiene al menos 1 letra min´uscula.
 c) tiene al menos 1 letra may´uscula.
 d) tiene al menos 1 d´ıgito num´erico (0..9)
 La contrase˜na ser´a ROJA si:
 a) la longitud es menor a 5 caracteres.
 En caso contrario ser´a AMARILLA.
'''
