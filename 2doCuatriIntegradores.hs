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
valoresDeCamino (x:xs) [] = []
valoresDeCamino []
