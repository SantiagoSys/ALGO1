{-Ejercicio 1. Implementar la funci´on generarStock :: [String] ->[(String, Int)]
problema generarStock (mercader´ıa: seq⟨String⟩) : seq⟨String × Z⟩ {
requiere: {True}
asegura: { La longitud de res es igual a la cantidad de productos distintos que hay en mercader´ıa}
asegura: {Para cada producto que pertenece a mercader´ıa, existe un i tal que 0 ≤ i < |res| y res[i]0=producto y
res[i]1 es igual a la cantidad de veces que aparece producto en mercader´ıa}
} -}
generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs) = añadirProducto x (generarStock xs)

añadirProducto :: String -> [(String, Int)] -> [(String, Int)]
añadirProducto p [] = [(p, 1)]
añadirProducto p ((n, c) : xs) | p == n = (n, c+1) : xs
                               | otherwise = (n, c) : añadirProducto p xs


{-Ejercicio 2. Implementar la funci´on stockDeProducto :: [(String, Int))] ->String
problema stockDeProducto (stock: seq⟨String × Z⟩, producto: String ) : Z {
requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
asegura: {si no existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a 0 }
asegura: {si existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a stock[i]1 }
} -}
stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((n, c):xs) p | n == p = c
                              | otherwise = stockDeProducto xs p


{-Ejercicio 3. Implementar la funci´on dineroEnStock :: [(String, Int))] ->[(String, Float)] ->Float
problema dineroEnStock (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : R {
requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
requiere: {Todo producto de stock aparece en la lista de precios}
asegura: {res es igual a la suma de los precios de todos los productos que est´an en stock multiplicado por la cantidad
de cada producto que hay en stock}
} -}
dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] _ = 0.0
dineroEnStock ((n, c):xs) ys = (precioProducto ys n) * (fromIntegral c) + (dineroEnStock xs ys)

precioProducto :: [(String, Float)] -> String -> Float
precioProducto ((n, v) : xs) p | n == p = v
                               | otherwise = precioProducto xs p


{-Ejercicio 4. Implementar la funci´on aplicarOferta :: [(String, Int)] ->[(String, Float)] ->[(String,Float)]
problema aplicarOferta (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : seq⟨String × R⟩ {
requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
requiere: {Todo producto de stock aparece en la lista de precios}
asegura: {|res| = |precios|}
asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) > 10, entonces res[i]0 = precios[i]0 y
res[i]1 = precios[i]1∗ 0,80}
asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) ≤ 10, entonces res[i]0 = precios[i]0 y
res[i]1 = precios[i]1 }
} -}
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta _ [] = []
aplicarOferta ss ((n, v) : ps) | (stockDeProducto ss n) > 10 = (n, v*0.80) : aplicarOferta ss ps
                               | otherwise = (n, v) : aplicarOferta ss ps


{-Fila = seq⟨Z⟩
Tablero = seq⟨Fila⟩
Posicion = Z × Z – Observaci´on: las posiciones son: (fila, columna)
Camino = seq⟨Posicion⟩
Ejercicio 5. Implementar la funci´on maximo :: Tablero ->Int
problema maximo (t: Tablero) : Z {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
asegura: {res es igual al n´umero m´as grande del tablero t}
} -}
type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maximo :: Tablero -> Int
maximo (x:xs) = maximoAux (unirFilas (x:xs))

maximoAux :: Fila -> Int
maximoAux [x] = x
maximoAux (x:y:xs) | x <= y = maximoAux(y:xs)
                   | otherwise = maximoAux (x:xs)

unirFilas :: Tablero -> Fila
unirFilas [] = []
unirFilas (x:xs) = x ++ unirFilas xs

t :: Tablero
t = [[2, 5, 7],
     [3, 8, 1],
     [6, 4, 9]]


{-Ejercicio 6. Implementar la funci´on masRepetido :: Tablero ->Int
problema masRepetido (t: Tablero) : Z {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
asegura: {res es igual al n´umero que m´as veces aparece en un tablero t. Si hay empate devuelve cualquiera de ellos}
} -}
masRepetido :: Tablero -> Int
masRepetido t = masRepetidoLista (unirFilas t)

cantRepeticiones :: Int -> [Int] -> Int
cantRepeticiones n [x] | n == x = 1
                       | otherwise = 0
cantRepeticiones n (x:xs) | n == x = 1 + cantRepeticiones n xs
                          | otherwise = cantRepeticiones n xs

masRepetidoLista :: [Int] -> Int
masRepetidoLista [x] = x
masRepetidoLista (x:xs) | cantRepeticiones x (x:xs) >= cantRepeticiones (masRepetidoLista xs) (x:xs) = x
                        | otherwise = masRepetidoLista xs


{-Ejercicio 7. Implementar la funci´on valoresDeCamino :: Tablero ->Camino ->[Int]
problema valoresDeCamino (t: Tablero, c: Camino) : seq⟨Z⟩ {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayores estrictos a 0}
requiere: {El camino c es un camino v´alido, es decir, secuencia de posiciones adyacentes en la que solo es posible
desplazarse hacia la posici´on de la derecha o hacia abajo y todas las posiciones est´an dentro de los limites del tablero
t}
asegura: {res es igual a la secuencia de n´umeros que est´an en el camino c, ordenados de la misma forma que aparecen
las posiciones correspondientes en el camino.}
} -}
valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino tablero [] = []
valoresDeCamino tablero (y:ys) = devolverPosicion y tablero : valoresDeCamino tablero ys

devolverPosicion :: Posicion -> Tablero -> Int
devolverPosicion (i,j) (fila:filas)  | i == 0    = elementoFila j fila
                                     | otherwise = devolverPosicion (i-1,j) filas

elementoFila :: Int -> Fila -> Int
elementoFila j (x:xs) | j == 0    = x
                      | otherwise = elementoFila (j-1) xs


-- EJERCICIO 8 --
{-Implementar la funci´on esCaminoFibo :: [Int]->Int->Bool
 problema esCaminoFibo (s:seq⟨Z⟩, i : Z) : Bool {
 requiere: {La secuencia de numeros s es no vacıa y esta compuesta por numeros positivos (mayores estrictos a 0)
 que representan los numeros ubicados en las posiciones que forman un camino en un tablero}
 requiere: {i ≥ 0}
 asegura: {res = true ⇔ los valores de s son la sucesion de Fibonacci inicializada con el numero pasado como
 parametro i}}
 -}
esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo (x:xs) i = empiezaConFibo x i && esSucesionDeFibo (x:xs) i

fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci (n-1) + fibonacci (n-2)

empiezaConFibo :: Int -> Int -> Bool
empiezaConFibo x i = x == fibonacci i

esSucesionDeFibo :: [Int] -> Int -> Bool
esSucesionDeFibo [x] _ = True
esSucesionDeFibo (x:y:xs) n | y == fibonacci (n + 1) = esSucesionDeFibo (y:xs) (n + 1)
                            | otherwise = False


-- EJERCICIO 9 --
{- 
 Implementar la funcion divisoresPropios :: Int->[Int]
 problema divisoresPropios (n: Z) : seq⟨Z⟩ {
 requiere: {n > 0}
 asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
 asegura: {res no tiene elementos repetidos}
 asegura: {res no contiene a ning´ un elemento que no sea un divisor propio de n}}
 -}
divisoresPropios :: Integer -> [Integer]
divisoresPropios n = divisoresPropiosAux n 1 []

divisoresPropiosAux :: Integer -> Integer -> [Integer] -> [Integer]
divisoresPropiosAux n i divisores | n <= i = divisores
                                  | mod n i == 0 && n /= i = divisoresPropiosAux n (i + 1) (divisores ++ [i])
                                  | otherwise = divisoresPropiosAux n (i + 1) divisores


-- EJERCICIO 10 --
{-
 Implementar la funci´on sonAmigos :: Int->Int->Bool
 problema sonAmigos (n,m: Z) : Bool {
 requiere: {n > 0}
 requiere: {m > 0}
 requiere: {m= n}
 asegura: {res = True ⇔ n y m son n´ umeros amigos}}
 -}
sonAmigos :: Integer -> Integer -> Bool
sonAmigos n m = sumaDivisoresPropios n == m && sumaDivisoresPropios m == n

sumaDivisoresPropios :: Integer -> Integer
sumaDivisoresPropios n = suma (divisoresPropios n)

suma :: [Integer] -> Integer
suma [] = 0
suma (x:xs) = x + suma xs


-- EJERCICIO 11 --
{-
Implementar la funcion losPrimerosNPerfectos :: Int->[Int]
 problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
 requiere: {n > 0}
 asegura: {|res| = n}
 asegura: {res es la lista de los primeros n numeros perfectos, de menor a mayor}}
 -}
losPrimerosNPerfectos :: Integer -> [Integer]
losPrimerosNPerfectos n = primerosPerfectos n 1

primerosPerfectos :: Integer -> Integer -> [Integer]
primerosPerfectos 0 _ = []
primerosPerfectos k x | esPerfecto x = x : primerosPerfectos (k-1) (x+1)
                      | otherwise = primerosPerfectos k (x+1)

esPerfecto :: Integer -> Bool
esPerfecto n = sumaDivisoresPropios n == n

-- EJERCICIO 13 --
{-
Problema cantidadNumerosAbundantes (d : Z, h : Z) : Z {
Requiere : {0 <= d <= h}
Asegura : {res es la cantidad de números abundantes en el rango [d..h]}}
-}
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes d h | d > h = 0
                              | esAbundante d = 1 + cantidadNumerosAbundantes (d+1) h
                              | otherwise = cantidadNumerosAbundantes (d+1) h

esAbundante :: Integer -> Bool
esAbundante n | (sumaDivisoresPropios n) > n = True
              | otherwise = False


{-
Problema cursadasVencidas (s : seq <String X Z X Z>) : seq <String> {
Requiere : {s[i]1 >= 1993 para todo i tal que 0 <= i < |5|}
Requiere : {0 <= s[i]2 <= 2 para todo i tal que 0 <= i < |5|}
Asegura : {res no tiene elementos repetidos}
Asegura : {res contiene los nombres de todas las materias incluidas en s tales que la materia fue aprobada a mas tardar en el primer cuatrimestre de 2021, inclusive}
}
-}
cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas [] = []
cursadasVencidas ((materia, año, cuatri) : xs) | esVencida año cuatri = agregarSiNoEsta materia (cursadasVencidas xs)
                                               | otherwise = cursadasVencidas xs

esVencida :: Integer -> Integer -> Bool
esVencida año cuatri = año < 2021 || (año == 2021 && cuatri <= 1)

agregarSiNoEsta :: (Eq t) => t -> [t] -> [t]
agregarSiNoEsta x [] = [x]
agregarSiNoEsta e (x:xs) | e == x = x:xs
                         | otherwise = x : agregarSiNoEsta e xs


{-
Problema saturarEnUmbralHastaNegativo (s : seq <Z>, u : Z) : seq<Z>, {
Requiere : {u > 0}
Asegura : {la longitud de res es igual a la cantidad de elementos no negativos consecutivos desde el inicio de s}
Asegura : {para cualquier i en el rango 0 <= i < |res| tal que 0 <= s[i] <= u, se cumple que res[i] = s[i]}
Asegura : {para cualquier i en el rango 0 <= i < |res| tal que s[i] > u, se cumple que res[i] = u}
}
-}
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] _ = []
saturarEnUmbralHastaNegativo (x:xs) u | x < 0 = []
                                      | x <= u = x : saturarEnUmbralHastaNegativo xs u
                                      | otherwise = u : saturarEnUmbralHastaNegativo xs u


{-
Problema cantidadParesColumna (matriz : seq<seq<Z>>, col : Z) : Z {
Requiere : {todos los elementros de la secuencia matriz tienen la misma longitud}
Requiere : {|matriz| > 0}
Requiere : {|matriz[0]| > 0}
Requiere : {1 <= col <= |matriz[0]|}
Asegura : {res es la cantidad de números pares de los elementos matriz[i] [col-1] para todo i tal que 0 <= i < |matriz|}
}
-}
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] _ = 0
cantidadParesColumna (fila:filas) col | esPar (elementoEnColumna fila col) = 1 + cantidadParesColumna filas col
                                      | otherwise = cantidadParesColumna filas col

elementoEnColumna :: [Integer] -> Integer -> Integer
elementoEnColumna (x:_) 1 = x
elementoEnColumna (_:xs) n = elementoEnColumna xs (n-1)

esPar :: Integer -> Bool
esPar x = mod x 2 == 0


-- EJERCICIO 17 --
{-
problema hayPrimosGemelos (d: Z,h: Z) : Bool {
  requiere: {0 < d â‰¤ h}
  asegura: {res = true <=> existen dos nÃºmeros p1 y p2 contenidos en el rango [d..h] tales que p1 y p2 son primos gemelos}
}
AclaraciÃ³n: Se dice que p1 y p2 son primos gemelos si ambos son primos y ademÃ¡s |p2-p1| = 2
-}


-- EJERCICIO 18 --
{- 
Representaremos un dÃ­a de cursada de cierta materia con una tupla String x String x Z x Z, donde:
    La primera componente de la tupla contiene el nombre de una materia
    La segunda componente de la tupla contiene el dÃ­a de cursada (lunes, martes, etc)
    La tercera componente de la tupla contiene el horario de inicio de la cursada de ese dÃ­a
    La cuarta componente de la tupla contiene el horario de fin de la cursada de ese dÃ­a
Se pide implementar materiasTurnoTarde, que dada una lista de cursadas devuelva aquellas materias que se cursan en el turno tarde (14 a 17hs)

problema materiasTurnoTarde (s: seqâŸ¨String x String x Z x ZâŸ©) :seqâŸ¨StringâŸ© {
  requiere: { s[i]1 es alguno de los siguientes valores: "Lunes", "Martes", "MiÃ©rcoles", "Jueves", "Viernes"}
  requiere: { s[i]2 â‰¥ 8 para todo i tal que 0 â‰¤ i < |s|}
  requiere: { s[i]3 â‰¤ 22 para todo i tal que 0 â‰¤ i < |s|}
  requiere: { s[i]2 < s[i]3 para todo i tal que 0 â‰¤ i < |s|}
  asegura: { res no tiene elementos repetidos}
  asegura: { res contiene los nombre de todas las materias incluÃ­das en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
  asegura: { res contiene solamente los nombre las materias incluÃ­das en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
}
-}


-- EJERCICIO 19 --
{-
problema maximaSumaDeTresConsecutivos (s: seqâŸ¨ZâŸ©) : Z {
  requiere: { |s| â‰¥ 3}
  asegura: { res es la suma de tres elementos que se encuentran en posiciones consecutivas de s }
  asegura: {Para cualquier i en el rango 1 â‰¤ i < |s|-1, se cumple que s[i-1]+s[i]+s[i+1] â‰¤ res}
}
-}


-- EJERCICIO 20 --
{-
problema sumaIesimaColumna (matriz: seqâŸ¨seqâŸ¨IntegerâŸ©âŸ©, col: Integer) : IntegerâŸ©{
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {1 â‰¤ col â‰¤ |matriz[0]| }
  asegura: {res es la sumatoria de los elementos matriz[i][col-1] para todo i tal que 0 â‰¤ i < |matriz| }
}
-}


-- EJERCICIO 21 --
{-
problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
  requiere: {|lista| > 0}
  requiere: {n > 0 ∧ n ≤ |lista|}
  asegura: {res es el promedio de los últimos n elementos de lista}
 }
-}


-- EJERCICIO 22 --
{-
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]
-}


-- EJERCICIO 23 --
{-
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True.
-}


-- EJERCICIO 24 --
{-
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }
-}


{-
problema aproboMasDeNMaterias (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, alumno:seq⟨Char⟩, n: Z) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {n > 0}
  requiere: {El alumno se encuentra en el registro }
  asegura: {res = true <=> el alumno tiene más de n notas de finales mayores o iguales a 4 en el registro}
}
-}


{-
problema buenosAlumnos (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨seq⟨Char⟩⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  asegura: {res es la lista de los nombres de los alumnos que están en registro cuyo promedio de notas es mayor o igual a 8 y no tiene aplazos (notas menores que 4)}
}
Para resolver el promedio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Int devuelve su equivalente de tipo Float.
-}


{-
problema mejorPromedio (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨Char⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {|registro| > 0 }
  asegura: {res es el nombre del alumno cuyo promedio de notas es el más alto; si hay más de un alumno con el mismo promedio de notas, devuelve el nombre de alumno que aparece primero en registro}
}
-}


{-
problema seGraduoConHonores (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, cantidadDeMateriasDeLaCarrera: Z, alumno: seq⟨Char⟩ ) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {cantidadDeMateriasDeLaCarrera > 0}
  requiere: {El alumno se encuentra en el registro }
  requiere: {|buenosAlumnos(registro)| > 0}
  asegura: {res <=> true si aproboMasDeNMaterias(registro, alumno, cantidadDeMateriasDeLaCarrera -1) = true y alumno pertenece al conjunto de buenosAlumnos(registro) y el promedio de notas de finales de alumno está a menos (estrictamente) de 1 punto del mejorPromedio(registro)}
}
-}


{-
problema porcentajeDeVotosAfirmativos (formulas: seq⟨String x String⟩,votos:seq< Z >, cantTotalVotos: Z) : R {
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {La suma de todos los elementos de votos es menor o igual a cantTotalVotos}
 asegura: {res es el porcentaje de votos no blancos (es decir, asociados a alguna de las fórmulas) sobre el total de votos emitidos}
}
Para resolver este ejercicio pueden utilizar la siguiente función que devuelve como Float la división entre dos números de tipo Int:
division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)
-}


{-
problema formulasInvalidas (formulas: seq⟨String x String⟩) : Bool {
 requiere: {True}
 asegura: {(res = true) <=> formulas contiene un candidato se propone para presidente y vicepresidente en la misma fórmula;
  o algún candidato se postula para presidente o vice en más de una fórmula }
-}


{-
problema porcentajeDeVotos (vice: String, formulas: seq⟨String x String⟩,votos:seq< Z >) : R {
 requiere: {La segunda componente de algún elemento de formulas es vice}
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {Hay al menos un elemento de votos mayores estricto a 0}
 asegura: {res es el porcentaje de votos que obtuvo vice sobre el total de votos afirmativos}
}
Para resolver este ejercicio pueden utilizar la función division presentada en el Ejercicio 1.
-}


{-
problema menosVotado (formulas: seq⟨String x String⟩, votos:seq< Z >) : String {
 requiere: {¬formulasInvalidas(formulas)}
 requiere: {|formulas| = |votos|}
 requiere: {Todos los elementos de votos son mayores o iguales a 0}
 requiere: {Hay al menos un elemento de votos mayores estricto a 0}
 requiere: {|formulas| > 0}
 asegura: {res es el candidato a presidente de formulas menos votado de acuerdo a los votos contabilizados en votos}
}
A continuación te dejamos una estructura básica para resolver los ejercicios.
 Este código no pretende resolver ningun caso de los ejercicios planteados, es sólo una plantilla.
-}
