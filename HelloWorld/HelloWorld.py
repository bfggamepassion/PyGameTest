def eratosthene(n):
    primes = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]

print("")
print("Hello World !")
print("")

nombres_premiers = eratosthene(250)
print(nombres_premiers[:50])