-- EJERCICIO 1 --
-- a)
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- b)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- c)
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

--d)
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]


-- EJERCICIO 2 --
-- a)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

-- b)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:xs) | pertenece x xs = todosIguales xs
                    | otherwise = False

-- c)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

-- d)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = True
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- e)
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e xs

-- f)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x : quitarTodos e xs
                     
-- 7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x : eliminarRepetidos xs

-- 8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos l1 [] | eliminarRepetidos l1 == [] = True
                      | otherwise = False
mismosElementos [] l2 | eliminarRepetidos l2 == [] = True
                      | otherwise = False
mismosElementos (x:xs) l2 | pertenece x (eliminarRepetidos l2) = mismosElementos xs (quitarTodos x l2)
                          | otherwise = False


-- EJERCICIO 3 --
-- 1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

-- 2)
productoria :: [Integer] -> Integer
productoria [] = 0
productoria [x] = x
productoria (x:xs) = x * productoria xs

-- 3)
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo xs

-- 4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x+n) : sumarN n xs

-- 5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [x] = [x]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- 7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

-- 8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

-- 9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar l = ordenar (quitar (maximo l) l) ++ [maximo l]


-- EJERCICIO 4 --
-- a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && x == y = x : sacarBlancosRepetidos xs
                               | otherwise = x : sacarBlancosRepetidos (y:xs)

-- b)
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) = contarBlancos () + 1

contarBlancos :: [Char] -> Integer
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar l = ordenar (quitar (maximo l) l) ++ [maximo l]

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((n, t) : xs) | nombre == n = True
                                    | otherwise = enLosContactos nombre xs

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto p [] = [p]
agregarContacto p (c : cs) | p == c = c : cs
                           | otherwise = c : agregarContacto p cs
