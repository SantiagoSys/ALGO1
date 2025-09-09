{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use even" #-}
{-# HLINT ignore "Redundant bracket" #-}
import System.Win32 (xBUTTON1, zeroMemory)
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
algunoEsCero x y = (x == 0 || y == 0)

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
ambosSonCero x y = (x == 0 && y == 0)

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
digitoUnidades x = mod x 10

{- j)
problema digitoDecenas(x: Z): Z {
    requiere: {True}
    asegura: {mod abs x 100 == y -> res = y}
}
-}
digitoDecenas :: Int -> Int
digitoDecenas x = mod x 100


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


{- b) 
problema esParMenor(x: (R, R), y: (R, R)): Bool {
    requiere: {True}
    asegura: {res = True <=> fst x < fst y && snd x z snd y}
}
-}


{- c)
problema distancia(x: (R, R), y: (R, R)): Float {
    requiere: {True}
    asegura: {res = sqrt((fst x - fst y)**2 + (snd x - snd y)**2)}
}
-}


{- d)
problema sumaTerna(x: (Z, Z, Z)): Z {
    requiere: {True}
    asegura: {res = fst x + snd x + }
}
-}


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


{- g)
problema crearPar(a: A, b: B): (A, B) {
    requiere: {True}
    asegura: {res = (a, b)}
}
-}

{- h)
problema invertir(x: (a, b)): (b, a) {
    requiere: {True}
    asegura: {res = (snd x, fst x)}
}
-}



-- EJERCICIO 5 --
{-
problema todosMenores (t : Z × Z × Z) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
}
-}


{-
problema f (n : Z) : Z {
    requiere: {True}
    asegura: {(n ≤ 7 → res = n^2) ∧ (n > 7 → res = 2n − 1)}
}
-}


{-
problema g (n : Z) : Z {
requiere: {True}
asegura: {Si n es un n´umero par entonces res = n/2, en caso contrario, res = 3n + 1}
}
-}



-- EJERCICIO 6 --
type Año = Int
type EsBisnieto = Bool
{-
problema bisiesto (a˜no : Z) : Bool {
requiere: {True}
asegura: {(res = false) ↔ (a˜no no es m´ultiplo de 4, o bien, a˜no es m´ultiplo de 100 pero no de 400)}
}
Por ejemplo:
bisiesto 1901 ⇝ False bisiesto 1904 ⇝ True
bisiesto 1900 ⇝ False bisiesto 2000 ⇝ True
-}



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