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

-- EJERCICIO 9 --
{-
problema esCapicua(n: Z): Bool {
    requiere: {n > 0}
    asegura: {res = () }
}
-}
