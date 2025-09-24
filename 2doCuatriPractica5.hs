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
