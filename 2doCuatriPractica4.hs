
-- EJERCICIO 1 --
{-
problema fibonacci (n: Z) : Z {
requiere: { n ≥ 0 }
asegura: { resultado = fib(n) }
}
-}
fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci (n-1) + fibonacci (n-2)


-- EJERCICIO 2 --
{-
problema parteEntera (x: R) : Z {
requiere: { x ≥ 0 }
asegura: { resultado ≤ x < resultado + 1 }
}
-}
parteEntera :: Float -> Int
parteEntera r | r < 1 = 0
              | otherwise = 1 + parteEntera (r-1)


-- EJERCICIO 3 --
{-
problema esDivisible(x: Z, y: Z) -> Bool {
    requiere: {y /= 0}
    asegura: {res = True <=> ∃k∈N: x = k*y}
}
-}
esDivisible :: Int -> Int -> Bool
esDivisible x y | x == 0 = True
                | x < y = False
                | otherwise = esDivisible (x-y) y


-- EJERCICIO 4 --
{-
problema sumaImpares(n: Integer): Integer
    requiere: { n ≥ 0 }
    asegura: { resultado = 1 + 3 + 5 + ... + (2*n - 1)}
-}
sumaImpares :: Int -> Int
sumaImpares n | n == 0 = 0
              | n == 1 = 1
              | otherwise = 2*n-1 + sumaImpares (n-1)


-- EJERCICIO 5 --


-- EJERCICIO 6 -- ¡¡PREGUNTAR!! --------------?
{-
problema todosDigitosIguales (n: Z) : B {
requiere: { n > 0 }
asegura: { resultado = true ↔ todos los d´ıgitos de n son iguales }
}
-}
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | mod n 10 /= mod(div n 10) 10 = False
                      | otherwise = True


-- EJERCICIO 7 --
{-
problema iesimoDigito (n: Z, i: Z) : Z {
requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
asegura: { resultado = (n div 10cantDigitos(n)−i
) mod 10 }
}
P´agina 1 de 3 Compilado el 2025/04/12
problema cantDigitos (n: Z) : N {
requiere: { n ≥ 0 }
asegura: { n = 0 → resultado = 1}
asegura: { n ̸= 0 → (n div 10resultado−1 > 0 ∧ n div 10resultado = 0) }
}
-}
cantDigitos :: Int -> Int
cantDigitos n | div n 10 == 0 = 1
              | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n i = mod (div n 10^(cantDigitos (n)-i)) 10


-- EJERCICIO 8 --
{-
problema sumaDigitos(n: N): Z {
    requiere: {n >= 0}
    asegura: {res = suma de todos los digitos de n}
}
-}
sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos (div n 10)

-- EJERCICIO 9 -- ¡¡PREGUNTAR!! --------------?
{-
problema esCapicua(n: Z): Bool {
    requiere: {n > 0}
    asegura: {res = () }
}
-}
primerDigito :: Int -> Int
primerDigito n = div n (10^cantDigitos(n-1))

ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

esCapicua :: Int -> Bool
esCapicua n | n < 10 = True
            | (primerDigito n == ultimoDigito n) && (esCapicua (sacarPrimeroYUltimo n)) = True
            | otherwise = False

numerosASacar :: Int -> Int -> Int
numerosASacar n i = (cantDigitos n) - i

sacarPrimeroYUltimo :: Int -> Int
sacarPrimeroYUltimo n = (mod (div n 10) (10^(cantDigitos n)-1))


-- EJERCICIO 14 --
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = (sumatoria q n) * (sumatoria q m)

sumatoria :: Integer -> Integer -> Integer
sumatoria q 1 = q
sumatoria q k = sumatoria q (k-1) + q^k


-- EJERCICIO 16 --
menorDivisor :: Integer -> Integer
menorDivisor 2 = 2
menorDivisor n = esDivisor n 2

esDivisor :: Integer -> Integer -> Integer
esDivisor n m | mod n m == 0 = m
              | otherwise = esDivisor n (m+1)

esPrimo :: Integer -> Bool
esPrimo n = n == menorDivisor n


-- EJERCICIO 19 --
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = esSumaDePrimerosKPrimos 1 n

esSumaDePrimerosKPrimos :: Int -> Int -> Bool
esSumaDePrimerosKPrimos k n | (sumaKprimos k) == n = True
                            | (sumaKprimos k) > n = False
                            | otherwise = esSumaDePrimerosKPrimos (k+1) n

sumaKprimos :: Integer -> Integer
sumaKprimos 1 = 2
sumaKprimos k = 

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo k = nEsimoPrimoAux 2 k

nEsimoPrimoAux :: Integer -> Integer -> Integer
nEsimoPrimoAux n k | esPrimo n && k == 1 = n
                   | esPrimo n && k /= 1 = nEsimoPrimoAux (n+1) (k-1)
                   | otherwise = nEsimoPrimoAux (n+1) k
