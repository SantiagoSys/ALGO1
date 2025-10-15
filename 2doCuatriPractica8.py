from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
separacion: str = "--------------------------------------------------"
'''
1. Pilas
Ejercicio 1. Implementar una soluci´on para el siguiente problema.
problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tama˜no de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
}
Para generar n´umeros en un rango con probabilidad uniforme, pueden usar la funci´on random.randint(< desde >, < hasta >)
que devuelve un n´umero en el rango indicado. Recuerden importar el m´odulo random con import random. Adem´as, pueden usar
la clase LifoQueue() que es un ejemplo de una implementaci´on b´asica de una pila:
from queue import LifoQueue as Pila # importa LifoQueue y le asigna el alias Pila
p = Pila () # crea una pila
p . put (1) # apila un 1
elemento = p . get () # desapila
p . empty () # devuelve true si y solo si la pila est ´a vac ´ı a
'''
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila: Pila[int] = Pila()
    for i in range(cantidad):
        nro_random = random.randint(desde, hasta)
        pila.put(nro_random)
    return pila
p = generar_nros_al_azar(3, 1, 10)
print(p.queue)
print(separacion)

'''
Ejercicio 2. Implementar una soluci´on para el siguiente problema.
problema cantidad elementos (in p: Pila) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de elementos que contiene p}
}
No se puede utilizar la funci´on LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el
par´ametro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificaci´on lo define como de tipo in, debe
restaurarse posteriormente.
'''
def cantidad_elementos (p: Pila) -> int:
    p1: Pila = Pila()
    p2: Pila = Pila()
    cantidad: int = 0
    while not p.empty():
        elem = p.get()
        p1.put(elem)
        p2.put(elem)
        
    while not p1.empty():
        p1.get()
        cantidad += 1
        
    while not p2.empty():
        p.put(p2.get())
    
    return cantidad

p: Pila = generar_nros_al_azar(3, 1, 9)
print(p.queue)
print(cantidad_elementos(p))
print(p.queue)
m: Pila = generar_nros_al_azar(5, 1, 100)
print(m.queue)
print(cantidad_elementos(m))
print(m.queue)
print(separacion)

'''
Ejercicio 3. Implementar una soluci´on para el siguiente problema.
problema buscar el maximo (in p: Pila[Z]) : Z {
requiere: {p no est´a vac´ıa}
asegura: {res es un elemento de p}
asegura: {res es mayor o igual a todos los elementos de p}
}
'''
def buscar_el_maximo (p: Pila[int]) -> int:
    p2: Pila = Pila()
    max: int = p.get()
    p2.put(max)
    
    while not p.empty():
        elem: int = p.get()
        p2.put(elem)
        if elem > max:
            max = elem
    
    while not p2.empty():
        p.put(p2.get())
        
    return max

p = generar_nros_al_azar(4, 1, 100)
print(p.queue)
print(buscar_el_maximo(p))
print(p.queue)
print(separacion)
        
'''
Ejercicio 4. Implementar una soluci´on para el siguiente problema.
problema buscar nota maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z {
requiere: {p no est´a vac´ıa}
requiere: {los elementos de p no tienen valores repetidos en la segunda posici´on de las tuplas}
asegura: {res es una tupla de p}
asegura: {No hay ning´un elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}
P´agina 1 de 10 Compilado el 2025/05/27
'''
def buscar_nota_maxima (p: Pila[tuple[str, int]]) -> tuple[str, int]:
    p2: Pila = Pila()
    max: int = p.get()
    p2.put(max)
    
    while not p.empty():
        elem: int = p.get()
        p2.put(elem)
        if elem[1] > max[1]:
            max = elem
    
    while not p2.empty():
        p.put(p2.get())
        
    return max

p: Pila = Pila()
p.put(("alex", 7))
p.put(("ana", 6))
p.put(("tomas", 9))
print(p.queue)
print(buscar_nota_maxima(p))
print(p.queue)
print(separacion)

'''
Ejercicio 5. Implementar una soluci´on, que use pila, para el siguiente problema.
problema esta bien balanceada (in s: seq⟨Char⟩) : Bool {
requiere: {s solo puede tener n´umeros enteros, espacios y los s´ımbolos ’(’, ’)’, ’+’, ’-’, ’*’, ’/’}
asegura: {res = true ↔ (La cantidad de par´entesis de apertura ’(´es igual a la de cierre ’)’) y (Para todo prefijo de ‘s‘,
la cantidad de par´entesis de cierre no supera a la de apertura)}
}
Por cada par´entesis de cierre debe haber uno de apertura correspondiente antes de ´el. Las f´ormulas pueden tener:
n´umeros enteros
operaciones b´asicas +, −, ∗ y /
par´entesis
espacios
Entonces las siguientes son f´ormulas aritm´eticas con sus par´entesis bien balanceados:
1 + ( 2 x 3 = ( 2 0 / 5 ) )
10 * ( 1 + ( 2 * ( =1)))
Y la siguiente es una f´ormula que no tiene los par´entesis bien balanceados:
1 + ) 2 x 3 ( ( )
'''
def esta_bien_balanceada(s: str) -> bool:
    p: Pila = Pila()
    i: int = 0
    
    while i < len(s):
        c: str = s[i]
        if c == '(':
            p.put('(')
        elif c == ')':
            if p.empty():
                return False
            p.get()
        i = i + 1
        
    if p.empty():
        return True
    else:
        return False

print(esta_bien_balanceada("1 + (2 * 3)"))
print(esta_bien_balanceada("(1 + (2 + 3))"))
print(esta_bien_balanceada("((1 + 2) * (3 + 4))"))
print(esta_bien_balanceada("1 + 2) * 3("))
print(separacion)

'''
Ejercicio 6. La notacion polaca inversa, tambien conocida como notacion postfix, es una forma de escribir expresiones ma-
tematicas en la que los operadores siguen a sus operandos. Por ejemplo, la expresion “3 + 4” se escribe como “3 4 +” en notacion
postfix. Para evaluar una expresion en notacion postfix, se puede usar una pila. Implementar una solucion para el siguiente
problema.
problema evaluar expresion (in s: seq⟨Char⟩) : R {
requiere: {s solo contiene numeros enteros y los operadores binarios +, -, * y /}
requiere: {Todos los elementos (operandos y operadores) estan separados por un unico espacio}
requiere: {La expresion es sintacticamente valida: cada operador binario tiene exactamente dos operandos previos
disponibles en el momento de su evaluacion.}
asegura: {res es el valor obtenido al evaluar la expresion postfija representada por s}
}
Para resolver este problema, se recomienda seguir el siguiente algoritmo:
1. Dividir la expresion en tokens (operandos y operadores) utilizando espacios como delimitadores.
2. Recorre los tokens uno por uno.
a) Si es un operando, agregalo a una pila.
b) Si es un operador, saca los dos operandos superiores de la pila, aplicale el operador y luego coloca el resultado en la
pila.
3. Al final de la evaluacion, la pila contendra el resultado de la expresion.
Ejemplo de uso:
expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Deberia imprimir 33
'''

'''
Ejercicio 7. Implementar una solucion para el siguiente problema.
problema intercalar (in p1: Pila, in p2: Pila) : Pila {
requiere: {p1 y p2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de p1 y p2}
asegura: {res contiene todos los elementos de p1 y p2, intercalados y respetando el orden original}
asegura: {El tope de la pila res es el tope de p2}
asegura: {El tama˜no de res es igual al doble del tama˜no de p1}
}
Nota: Ojo que hay que recorrer dos veces para que queden en el orden apropiado al final.
'''
def intercalar(p1: Pila, p2: Pila) -> Pila:
    pila_res: Pila = Pila()

    while not p1.empty() and not p2.empty():
        elemento1 = p1.get()
        elemento2 = p2.get()
        pila_res.put(elemento1)
        pila_res.put(elemento2)
    return pila_res.queue

'''
2. Colas
Ejercicio 8. Implementar una solucion para el siguiente problema.
problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Cola[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tama˜no de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
}
Para generar numeros en un rango con probabilidad uniforme, pueden usar la funci´on random.randint(< desde >, < hasta >)
que devuelve un n´umero en el rango indicado. Recuerden importar el m´odulo random con import random. Pueden usar la clase
Queue() que es un ejemplo de una implementaci´on b´asica de una Cola:
from queue import Queue as Cola # importa Queue y le asigna el alias Cola
c = Cola () # creo una cola
c . put (1) # encolo el 1
elemento = c . get () # desencolo
c . empty () # devuelve true si y solo si la cola está vacía
'''
def generar_nros_al_azar2 (cantidad: int, desde: int, hasta: int) -> Cola[int]:
    cola: Cola = Cola()
    for i in range(cantidad):
        nros: int = random.randint(desde, hasta)
        cola.put(nros)
    return cola

c = generar_nros_al_azar2(3, 1, 10)
print(c.queue) # Debe devolver "deque([nro, nro, nro])"
print(separacion)

'''
Ejercicio 9. Implementar una solución para el siguiente problema.
problema cantidad elementos (in c: Cola) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de elementos que contiene c}
}
No se puede utilizar la función Queue.qsize().
Comparar el resultado con la implementación utilizando una pila en lugar de una cola.
'''
def cantidad_elementos2 (c: Cola) -> int:
    cantidad: int = 0
    cola2: Cola = Cola()

    while not c.empty():
        elem = c.get()
        cola2.put(elem)
        cantidad += 1

    while not cola2.empty():
        c.put(cola2.get())

    return cantidad

c: Cola = generar_nros_al_azar2(3, 1, 10)
print(c.queue)
print(cantidad_elementos2(c))
print(c.queue)
m: Cola = generar_nros_al_azar2(5, 1, 10)
print(m.queue)
print(cantidad_elementos2(m))
print(m.queue)
print(separacion)

'''
Ejercicio 10. Implementar una solución para el siguiente problema.
problema buscar el maximo (in c: Cola[Z]) : Z {
requiere: {c no está vacía}
asegura: {res es un elemento de c}
asegura: {res es mayor o igual a todos los elementos de c}
}
Comparar con la versión usando pila.
'''
def buscar_el_maximo2 (c: Cola[int]) -> int: # ???
    cola2: Cola = Cola()
    max: int = c.get()
    cola2.put(max)

    while not c.empty():
        elem = c.get()
        if elem > max:
            max = elem
        cola2.put(elem)
    
    while not cola2.empty():
        c.put(cola2.get())
    
    return max

c: Cola[int] = generar_nros_al_azar2(3, 1, 10)
print(c.queue)
print(buscar_el_maximo2(c))
print(c.queue)

'''
Ejercicio 11. Implementar una solución para el siguiente problema.
problema buscar nota minima (in c: Cola[seq⟨Char × Z⟩]) : (seq⟨Char × Z⟩) {
requiere: {c no está vacía}
requiere: {los elementos de c no tienen valores repetidos en la segunda componente de las tuplas}
asegura: {res es una tupla de c}
asegura: {No hay ningún elemento en c cuya segunda componente sea menor que la de res }
}
Página 3 de 10 Compilado el 2025/05/27
'''

'''
Ejercicio 12. Implementar una solución para el siguiente problema.
problema intercalar (in c1: Cola, in c2: Cola) : Cola {
requiere: {c1 y c2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de c1 y c2}
asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
asegura: {El primer elemento de res es el primer elemento de c1}
asegura: {El tama˜no de res es igual al doble del tama˜no de c1}
}
'''

'''
Ejercicio 13. Bingo: un cartón de bingo contiene 12 números al azar en el rango [0, 99]. Implementar una solución para cada
uno de los siguientes problemas.
1. problema armar secuencia de bingo () : Cola[Z] {
requiere: {True}
asegura: {res solo contiene 100 n´umeros del 0 al 99 inclusive, sin repetidos}
asegura: {Los n´umeros de res est´an ordenados al azar}
}
Para generar n´umeros pseudoaleatorios pueden usar la funci´on random.randint(< desde >, < hasta >) que devuelve un
n´umero en el rango indicado. Recuerden importar el m´odulo random con import random.
2. problema jugar carton de bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
requiere: {carton solo contiene 12 n´umeros, sin repetidos, con valores entre 0 y 99, ambos inclusive}
requiere: {bolillero solo contiene 100 n´umeros, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
asegura: {res es la cantidad m´ınima de jugadas necesarias para que todos los n´umeros del carton hayan salido del
bolillero}
}
'''

'''
Ejercicio 14. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la m´as urgente
y requiere atenci´on inmediata) junto con su nombre y la especialidad m´edica que le corresponde. Implementar una soluci´on para
el siguiente problema.
problema pacientes urgentes (in c:Cola[Z× seq⟨Char⟩ × seq⟨Char⟩]) : Z {
requiere: {Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11}
asegura: {res es la cantidad de elementos de c que tienen como primer componente de la tupla un n´umero menor a 4}
}
'''

'''
Ejercicio 15. La gerencia de un banco nos pide modelar la atenci´on de los clientes usando una cola donde se van registrando
los pedidos de atenci´on. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que est´a a la
entrada: Nombre y Apellido, DNI, tipo de cuenta (true si es preferencial o f alse en el caso contrario) y si tiene prioridad (true
o f alse) por ser adulto +65, embarazada o con movilidad reducida.
La atenci´on a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
bancaria preferencial y por ´ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.

1. Dar una especificaci´on para el problema planteado.

2. Implementar atencion a clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que da-
da la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
P´agina 4 de 10 Compilado el 2025/05/27

3. Diccionarios

En esta secci´on trabajaremos con el tipo dict de Python, que nos permite asociar claves con valores.
'''

'''
Ejercicio 16. Implementar una soluci´on para el siguiente problema.
problema calcular promedio por estudiante (in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
requiere: {El primer componente de las tuplas de notas no es una cadena vac´ıa}
requiere: {El segundo componente de las tuplas de notas est´a en el rango [0, 10]}
asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
asegura: {Todos los nombres de notas (primer componente) son clave en res}
asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segunda componente
de notas)}
}
'''

'''
Ejercicio 17. Se debe desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
usuarios del sistema. El navegador debe permitir al usuario navegar hacia atr´as en la historia de navegaci´on.

1. Crea un diccionario llamado historiales que almacenar´a el historial de navegaci´on para cada usuario. Las claves del
diccionario ser´an los nombres de usuario y los valores ser´an pilas de String.

2. Implementar una soluci´on para el siguiente problema.
problema visitar sitio (inout historiales: Diccionario⟨seq⟨Char⟩, P ila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩)
{
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historia-
les@pre[usuario]}
asegura: {Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila
que tiene solo el elemento sitio}
asegura: {No se modifica ning´un otro historial salvo, si existe, el de usuario}
asegura: {Todos los pares clave-valor de historiales@pre est´an en historiales}
asegura: {Todos los pares clave-valor de historiales est´an en historiales@pre, salvo historiales[usuario] que
podr´ıa no existir en historiales@pre}
}

3. Implementar una soluci´on para el siguiente problema.
problema navegar atras (inout historiales: Diccionario⟨ seq⟨Char⟩, Pila[ seq⟨Char⟩, in usuario: seq⟨Char⟩⟩) : seq⟨Char⟩
{
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
requiere: {usuario es una clave de historiales}
requiere: {La pila asociada a usuario no est´a vac´ıa}
asegura: {res es igual al tope de historiales@pre[usuario]}
asegura: {historiales[usuario] es igual a historiales@pre[usuario] quitando el tope de la pila de
historiales@pre[usuario]}
asegura: {En historiales, salvo la pila asociada a usuario, no se modifica ning´un otro por clave-valor}
}
Ejemplo de uso:
historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
P´agina 5 de 10 Compilado el 2025/05/27
'''

'''
Ejercicio 18. Se debe desarrollar un sistema de gesti´on de inventario para una tienda de ropa. Este sistema debe permitir llevar
un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y
calcular el valor total del inventario.
Para resolver este problema vamos a utilizar un diccionario llamado inventario que almacenar´a la informaci´on de los
productos. En este diccionario, cada clave ser´a el nombre de un producto, y su valor asociado ser´a otro diccionario con los
atributos del producto. Este segundo diccionario tendr´a dos claves posibles: ’precio’y ’cantidad’, cuyos valores ser´an de tipo float
e int, respectivamente.
Un ejemplo de inventario, con un solo producto, es: {“remera”: {“precio”: 999.99, “cantidad”: 3}}).
Implementar una soluci´on para cada uno de los siguientes problemas. Agregar en las funciones los tipos de datos correspondientes
(ver nota al final de la primera especificaci´on).

1. problema agregar producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in precio: R, in cantidad: Z) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {precio ≥ 0}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
requiere: {nombre no es una clave de inventario }
asegura: {Todas los pares clave-valor de inventario@pre est´an tal cual en inventario}
asegura: {Todas los pares clave-valor de inventario est´an en inventario@pre y, adem´as, hay una nueva con clave
igual a nombre y como valor tendr´a un diccionario con los pares clave-valor (“precio”, precio) y (“cantidad”,
cantidad)}
}
Se necesitar´a un diccionario cuyas claves son de tipo String (“precio” y “cantidad”) y cuyos valores ser´an de tipo float
y enteros respectivamente. Para declarar los tipos de este diccionario mediante anotaciones en Python, se procede de la
siguiente manera:
En Python 3.9:
Es necesario importar Union desde el m´odulo typing para indicar que los valores pueden ser de m´as de un tipo.
from typing import Union
mi diccionario: dict[str, Union[int, float]]
En Python 3.10 o superior:
No es necesario importar Union, ya que se puede usar el operador | para representar una uni´on de tipos.
mi diccionario: dict[str, int | float]

2. problema actualizar stock (inout inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in cantidad: R) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Todos los pares clave-valor de inventario@pre est´an tal cual en inventario, con excepci´on del que tiene
como clave nombre}
asegura: {Todos los pares clave-valor de inventario est´an en inventario@pre}
asegura: {En inventario, el valor asociado a la clave nombre, tendr´a el mismo precio que antes y la cantidad ser´a
cantidad}
}

3. problema actualizar precio (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre:seq⟨Char⟩,
in precio: R) {
requiere: {T ∈ [Z, R]}
requiere: {precio ≥ 0}
P´agina 6 de 10 Compilado el 2025/05/27
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Todos los pares clave-valor de inventario@pre est´an tal cual en inventario, con excepci´on del valor que
tiene como clave nombre}
asegura: {Todos los pares clave-valor de inventario est´an en inventario@pre}
asegura: {En inventario el diccionario asociado a nombre, tendr´a la misma cantidad que antes y el precio ser´a
precio}
}

4. problema calcular valor inventario (in inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario ⟨ seq⟨Char⟩, T ⟩⟩) : R {
requiere: {T ∈ [Z, R]}
requiere: {Ninguno de los Strings del inventario es vac´ıo}
asegura: {res es la suma, para cada producto, del precio multiplicado por la cantidad}
}
Ejemplo de uso:
inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantal´on", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deber´ıa imprimir 1100.0
'''

'''
4. Archivos
Para usar archivos contamos con las funciones: open, close, read, readline, readlines, write, os.path.join(), os.path.exists().
Para m´as informaci´on referirse a la documentaci´on: https://docs.python.org/es/3/tutorial/inputoutput.html#
reading-and-writing-files
Todos los archivos referidos en las especificaciones ser´an de texto plano como por ejemplo:
.txt: Archivos de texto sin formato.
.csv: Archivos de valores separados por comas.
.json: Archivos de texto con formato JSON (diccionarios).
.html o .xml: Archivos de texto con marcado.
.log: Archivos de registro o logs.
.md: Archivos de texto con formato Markdown.
.py o .java o .c o .cpp: Archivos con c´odigo en distintos lenguajes de programaci´on.
Una l´ınea termina cuando hay un salto de l´ınea: un caracter \n.
Una palabra es una secuencia de caracteres alfab´eticos (y opcionalmente n´umeros o guiones) separada por espacios o
puntuaci´on, que puede incluir letras con tilde y caracteres del alfabeto extendido como ˜n. Los caracteres de puntuaci´on
que consideraremos son: . , ; : “ ” ‘ ’ ¡ ! ¿ ? ( ) [ ] { } ><\n.
Ejemplos de palabras: IP Algo1 P5P ip-algo1 ip
Ejemplos que no son palabras: Hola! sal-\nto
P´agina 7 de 10 Compilado el 2025/05/27
'''

'''
Ejercicio 19. Implementar una soluci´on para cada uno de los siguientes problemas.
1. problema contar lineas (in nombre archivo: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {res es igual a la cantidad de l´ıneas que contiene el archivo indicado por nombre archivo}
}

2. problema existe palabra (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vac´ıa}
asegura: {res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre archivo}
}

3. problema cantidad de apariciones (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vac´ıa}
asegura: {res es la cantidad de veces que palabra aparece en el archivo indicado por nombre archivo}
}
'''

'''
Ejercicio 20. Implementar una soluci´on para el siguiente problema.
problema agrupar por longitud (in nombre archivo: seq⟨Char⟩) : Diccionario⟨Z, Z⟩ {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {Para cada longitud n tal que existe al menos una palabra de longitud n en el archivo indicado por nombre archivo,
res[n] es igual a la cantidad de palabras de esa longitud}
asegura: {No hay otras claves en res que no correspondan a longitudes de palabras presentes en el archivo}
}
Por ejemplo, el diccionario
{
1: 2 ,
2: 10 ,
5: 4
}
indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras de longitud 5. Para este ejercicio
se consideran como palabras todas aquellas secuencias de caracteres delimitadas por espacios en blanco.
'''

'''
Ejercicio 21. Implementar una soluci´on para el siguiente problema.
problema la palabra mas frecuente (in nombre archivo: seq⟨Char⟩) : seq⟨Char⟩ {
requiere: {nombre archivo es un archivo existente y accesible que tiene, por lo menos, una palabra}
asegura: {res es una palabra que aparece en el archivo nombre archivo}
asegura: {No hay ninguna palabra contenida en el archivo nombre archivo que aparezca m´as veces que la palabra res }
}
Para resolver el problema se aconseja utilizar un diccionario de palabras.
'''

'''
Ejercicio 22. Implementar una soluci´on para el siguiente problema.
problema clonar sin comentarios (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩) {
requiere: {nombre archivo entrada es el path con el nombre de un archivo existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
P´agina 8 de 10 Compilado el 2025/05/27
asegura: {El archivo indicado por nombre archivo salida contiene las mismas l´ıneas y en el mismo orden que el archivo
nombre archivo entrada, excepto aquellas que comienzan con el car´acter #}
}
Para este ejercicio vamos a considerar que una l´ınea es un comentario si tiene un ‘#’como primer car´acter de la l´ınea, o si no
es el primer car´acter, se cumple que todos los anteriores son espacios.
Por ejemplo, si se llama a clonar sin comentarios con un archivo con este contenido: ´
nombre archivo salida solo contendr´a la ´ultima l´ınea:
esto no es un comentario # esto tampoco
'''

'''
Ejercicio 23. Implementar una soluci´on para el siguiente problema.
problema invertir lineas (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩ ) {
requiere: {nombre archivo entrada es el path de un archivo de texto existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas l´ıneas que el archivo nombre archivo entrada,
pero en orden inverso}
}
Por ejemplo, si el archivo contiene lo siguiente:
Esta es la primera linea .
Y esta es la segunda .
debe generar:
Y esta es la segunda .
Esta es la primera linea .
'''

'''
Ejercicio 24. Implementar una soluci´on para el siguiente problema.
problema agregar frase al final (in nombre archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
requiere: {nombre archivo es el path de un archivo existente y accesible}
requiere: {f rase no es vac´ıa}
asegura: {f rase se agrega como una nueva l´ınea al final del archivo nombre archivo}
}
Este problema no crea una copia del archivo de entrada, sino que lo modifica.
'''

'''
Ejercicio 25. Dado un archivo de texto y una frase, implementar una funci´on
agregar frase al principio(in nombre archivo : str, in frase : str), que agregue la frase al comienzo del archivo original
(similar al ejercicio anterior, sin hacer una copia del archivo).
problema agregar frase al principio (in nombre archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
requiere: {nombre archivo es el path de un archivo existente y accesible}
requiere: {f rase no es vac´ıa}
asegura: {f rase se agrega como primera l´ınea del archivo nombre archivo, desplazando las anteriores hacia abajo}
}
Este problema no crea una copia del archivo de entrada, sino que lo modifica.
'''

'''
Ejercicio 26. Implementar una soluci´on para el siguiente problema.
problema listar textos de archivo (in nombre archivo: seq⟨Char⟩ ) : seq⟨seq⟨Char⟩⟩ {
requiere: {nombre archivo es el path de un archivo existente y accesible}
asegura: {res contiene exactamente los textos legibles que aparecen en el archivo nombre archivo}
}
Definimos un texto como legible si:
P´agina 9 de 10 Compilado el 2025/05/27
solo contiene secuencias de car´acteres legibles (n´umeros, letras may´usculas/min´usculas, espacios o ‘ ’(gui´on bajo)
tienen longitud >= 5
Referencia: https://docs.python.org/es/3/library/functions.html#open
Para resolver este ejercicio se puede abrir un archivo en modo binario ‘b’. Al hacer read() vamos a obtener
una secuencia de bytes, que al hacer chr(byte) nos va a devolver un car´acter correspondiente al byte
le´ıdo.
Una vez implementada la funci´on, probarla con diferentes archivos binarios (.exe, .zip, .wav, .mp3, etc).
'''

'''
Ejercicio 27. Implementar una soluci´on para el siguiente problema.
problema calcular promedio por estudiante (in nombre archivo notas: seq⟨Char⟩, in nombre archivo promedios: seq⟨Char⟩)
{
requiere: {nombre archivo notas es el path de un archivo existente y accesible, con formato CSV: cada l´ınea tendr´a
n´umero de LU, materia, fecha y nota, todo separado por comas}
requiere: {nombre archivo promedios es el path de un archivo distinto, accesible para escritura}
asegura: {El archivo nombre archivo promedios contiene una l´ınea por estudiante del archivo nombre archivo notas,
con su LU y su promedio separados por una coma}
}
El contenido del archivo nombre archivo notas tiene el siguiente formato:
nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
Analizar el problema y modularizar el c´odigo apropiadamente. Una opci´on es implementar una funci´on auxiliar que cumpla
la siguiente especificaci´on.
problema promedio estudiante (in notas de estudiantes: seq⟨seq⟨Char⟩⟩, in lu: seq⟨Char⟩ ) : R {
requiere: {notas de estudiantes tiene el contenido del archivo de notas. Cada elemento de la lista es una l´ınea de ese
archivo, con formato CSV: tendr´a n´umero de LU, materia, fecha y nota, todo separado por comas}
requiere: {lu corresponde a una LU presente en notas de estudiantes}
asegura: {res es el promedio de las notas asociadas a lu en notas de estudiantes}
}
'''
