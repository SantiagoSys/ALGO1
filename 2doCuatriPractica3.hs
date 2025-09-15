{- notacion PREfija:
    mod n 10

   notacion INfija:
   n 'mod' 10

   notacion POSfija:
   n 10 'mod'
-}
-- EJERCICIO 1 --
{- a)
problema f(n: Z): Z {
    requiere: {n = 1 || n = 4 || n = 16}
    asegura: {(n = 1 -> res = 8) && (n = 4 -> res = 131) && (n = 16 -> res = 16)}
}
-}
f :: Int -> Int
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

{- b)
problema g(n: Z): Z {
    requiere: {n = 8 || n = 131 || n = 16}
    asegura: {(n = 8 -> res = 1) && (n = 131 -> res = 4) && (n = 16 -> res = 16)}
}
-}
g :: Int -> Int
g n  | n == 8 = 1
     | n == 131 = 4
     | n == 16 = 16

{- c)
problema h(k: g(n: f(n: Z))): Z {
    requiere: {k = g(f(n)))}
    asegura: {res = n}
}
-}
h :: Int -> Int
h n = f (g n)

k :: Int -> Int
k n = g (f n)


-- EJERCICIO 2 --
{- a)
problema absoluto(n: Z): Z {
    requiere: {True}
    asegura: {n >= 0 -> res = n}
    asegura: {n < 0 -> res = -n}
}
-}
absoluto :: Int -> Int
absoluto n | n >= 0 = n
           | otherwise = -n

{- b)
problema maximoAbsoluto(x: Z, y: Z): Z {
    requiere: {True}
    asegura: {(|x| >= |y| -> res = |x|) || (|x| <= |y| -> res = |y|)}
}
-}
maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y | absoluto x >= absoluto y = absoluto x
                   | otherwise = absoluto y

{- c)
problema maximo3(x: Z, y: Z, z: Z): Z {
    requiere: {True}
    asegura: {((x >= y) && (y >= z) -> res = x) || ((z >= y) && (y >= x) -> res = z) || res = y}
}
-}
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | (x >= y) && (y >= z) = x
              | (y >= z) && (z >= x) = y
              | otherwise = z

{- d)
problema algunoEsCero(x: R, y: R): Bool {
    requiere: {True}
    asegura: {(x == 0 || y == 0) -> res = False}
}
-}
-- Con pattern matching
algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y = x == 0 || y == 0

-- Sin pattern matching
algunoEsCero2 :: Float -> Float -> Bool
algunoEsCero2 x y | x == 0 || y == 0 = True
                  | otherwise = False

{- e)
problema ambosSonCero(x: R, y: R): Bool {
    requiere: {True}
    asegura: {(x == 0 && y == 0) -> res = False}
}
-}
-- Con pattern matching
ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y = x == 0 && y == 0

-- Sin pattern matching
ambosSonCero2 :: Float -> Float -> Bool
ambosSonCero2 x y | x == 0 && y == 0 = True
                  | otherwise = False

{- f)
problema enMismoIntervalo()
-}

{- g)
problema sumaDistintos(x: Z, y: Z, z: Z): Z {
    requiere: {True}
    asegura: {((x == y) -> res = z) || ((y == z) -> res = x) || ((x == z) -> res = y) || ((x /= y /= z) -> res = x + y + z)}
}
-}
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x == y = z
                    | y == z = x
                    | x == z = y
                    | otherwise = x + y + z

{- h)
problema esMultiploDe(x: N, y: N): Bool {
    requiere: {True}
    asegura: {mod x y = 0 -> res = True}
}
-}
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

{- i)
problema digitoUnidades(x: Z): Z {
    requiere: {True}
    asegura: {mod abs x 10 == y -> res = y}
}
-}
digitoUnidades :: Int -> Int
digitoUnidades x = mod (abs x) 10

{- j)
problema digitoDecenas(x: Z): Z {
    requiere: {True}
    asegura: {mod abs x 100 == y -> res = y}
}
-}
digitoDecenas :: Int -> Int
digitoDecenas x = div (mod (abs x) 100) 10


-- EJERCICIO 3 --
{-
problema estanRelacionados(a: Z, b: Z): Bool {
    requiere: {a /= 0 && b /= 0}
    asegura: {(res = True) <=> (a*a + a*b*k = 0 para algún k ∈ Z con k /= 0)}
}
-}
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b = mod a b == 0


-- EJERCICIO 4 --
{- a)
problema productoInterno(x: (R, R), y: (R, R)): R {
    requiere: {True}
    asegura: {res = fst x * fst y + snd x * snd y}
}
-}
productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno x y = fst x * fst y + snd x * snd y

{- b) 
problema esParMenor(x: (R, R), y: (R, R)): Bool {
    requiere: {True}
    asegura: {res = True <=> fst x < fst y && snd x < snd y}
}
-}
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor p1 p2 = (fst p1 < fst p2) && (snd p1 < snd p2)

esParMenor2 :: (Float, Float) -> (Float, Float) -> Bool
esParMenor2 t1 t2 | (fst t1 < fst t2) && (snd t1 < snd t2) = True
                  | otherwise = False

esParMenor3 :: (Float, Float) -> (Float, Float) -> Bool
esParMenor3 (a,b) (c,d) = (a < c) && (b < d)

{- c)
problema distancia(x: (R, R), y: (R, R)): Float {
    requiere: {True}
    asegura: {res = sqrt((fst x - fst y)**2 + (snd x - snd y)**2)}
}
-}
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia x y = sqrt(fst x - fst y)^2 + (snd x - snd y)^2

{- d)
problema sumaTerna(x: (Z, Z, Z)): Z {
    requiere: {True}
    asegura: {res = fst x + snd x + }
}
-}
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x, y, z) = x + y + z

{- e)
problema sumarSoloMultiplos(x: (Z, Z, Z), n: N): Z {
    requiere: {n > 0}  -- n es natural
    asegura: {
        res = sumMult (fst x) + sumMult (fst (snd x)) + sumMult (snd (snd x))
    }
    donde
        sumMult y
            | y `mod` n == 0 = y
            | not (y `mod` n == 0) = 0
}
-}
sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) n = sumMult x + sumMult y + sumMult z
    where sumMult a | mod a n == 0 = a
                    | otherwise = 0

{- f)
problema posPrimerPar(x: (Z, Z, Z)): N {
    requiere: {True}
    asegura: {
        res = 1  | fst x `mod` 2 == 0
        res = 2  | fst x `mod` 2 /= 0 && fst (snd x) `mod` 2 == 0
        res = 3  | fst x `mod` 2 /= 0 && fst (snd x) `mod` 2 /= 0 && snd (snd x) `mod` 2 == 0
        res = 4  | fst x `mod` 2 /= 0 && fst (snd x) `mod` 2 /= 0 && snd (snd x) `mod` 2 /= 0
    }
}
-}
posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z) | mod x 2 == 0 = 1
                       | mod x 2 /= 0 && mod y 2 == 0 = 2
                       | mod x 2 /= 0 && mod y 2 /= 0 && mod z 2 == 0 = 3
                       | otherwise = 4

esPar :: Int -> Bool
esPar n | mod n 2 == 0 = True
        | otherwise = False

posPrimerPar2 :: (Int, Int, Int) -> Int
posPrimerPar2 (x, y, z) | esPar x = 1
                        | esPar y = 2
                        | esPar z = 3
                        | otherwise = 4

{- g)
problema crearPar(a: A, b: B): (A, B) {
    requiere: {True}
    asegura: {res = (a, b)}
}
-}
crearPar :: Int -> Int -> (Int, Int)
crearPar a b = (a, b)

{- h)
problema invertir(x: (a, b)): (b, a) {
    requiere: {True}
    asegura: {res = (snd x, fst x)}
}
-}
invertir :: (Int, Int) -> (Int, Int)
invertir (a, b) = (b, a)


-- EJERCICIO 5 -- ¡¡PREGUNTAR!! --------------?
{-
problema todosMenores (t : Z × Z × Z) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
}
-}
todosMenores :: (Int, Int, Int) -> Bool
todosMenores (t0, t1, t2) = (f2 t0 > g2 t0) && (f2 t1 > g2 t1) && (f2 t2 > g2 t2)

{-
problema f2 (n : Z) : Z {
    requiere: {True}
    asegura: {(n ≤ 7 → res = n^2) ∧ (n > 7 → res = 2n − 1)}
}
-}
f2 :: Int -> Int
f2 n | n <= 7 = n^2
     | otherwise = 2*n - 1

{-
problema g2 (n : Z) : Z {
requiere: {True}
asegura: {Si n es un n´umero par entonces res = n/2, en caso contrario, res = 3n + 1}
}
-}
g2 :: Int -> Int
g2 n | mod n 2 == 0 = div n 2
     | otherwise = 3*n + 1


-- EJERCICIO 6 --
type Año = Int
type EsBisiesto = Bool
{-
problema bisiesto (a˜no : Z) : Bool {
requiere: {True}
asegura: {(res = false) ↔ (a˜no no es m´ultiplo de 4, o bien, a˜no es m´ultiplo de 100 pero no de 400)}
}
Por ejemplo:
bisiesto 1901 ⇝ False bisiesto 1904 ⇝ True
bisiesto 1900 ⇝ False bisiesto 2000 ⇝ True
-}
bisiesto :: Int -> Bool
bisiesto año = (mod año 4 == 0) || (mod año 100 /= 0 && mod año 400 == 0)


-- EJERCICIO 7 --
{- a)
distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
requiere: {T rue}
asegura: {res =
P2
i=0 |pi − qi
|}
}
Por ejemplo:
distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8
-}
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan p q = sumaTernaf p - sumaTernaf q

sumaTernaf :: (Float, Float, Float) -> Float
sumaTernaf (x, y, z) = x + y + z

{- b)
Reimplementar la funci´on teniendo en cuenta el siguiente tipo: type Punto3D = (Float, Float, Float)
-}


-- EJERCICIO 8 --
{-
problema comparar (a : Z, b : Z) : Z {
    requiere: {True}
    asegura: {(res = 1) ↔ (sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
    asegura: {(res = −1) ↔ (sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
    asegura: {(res = 0) ↔ (sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
}
-}
comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | otherwise     = 0

{-
problema sumaUltimosDosDigitos (x : Z) : Z {
    requiere: {True}
    asegura: {res = (|x| m´od 10) + (j
    |x|
    10 k
    m´od 10)}
}
Por ejemplo:
comparar 45 312 ⇝ -1 porque 45 ≺ 312 y 4 + 5 > 1 + 2.
comparar 2312 7 ⇝ 1 porque 2312 ≺ 7 y 1 + 2 < 0 + 7.
comparar 45 172 ⇝ 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45.
-}
sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = (mod (abs x) 10) + (mod (div (abs x) 10) 10)


-- EJERCICIO 9 --
{-
a)
f1 :: Float -> Float
f1 n | n == 0 = 1
     | otherwise = 0

b)
f2 :: Float -> Float
f2 n | n == 1 = 15
     | n == -1 = -15

c)
f3 :: Float -> Float
f3 n | n <= 9 = 7
     | n >= 3 = 5

d)
f4 :: Float -> Float -> Float
f4 x y = ( x + y )/2

e)
f5 :: ( Float , Float ) -> Float
f5 (x , y ) = ( x + y )/2

f)
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b
-}
