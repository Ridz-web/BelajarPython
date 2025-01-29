import math

def prima(angka):
    for prime in range(2, int(math.sqrt(angka +1))):
        if angka % prime == 0:
            return False
    return True

def cetak_prime(angka):
    primes = []
    for i in range(2, angka + 1):
        if prima(i):
            primes.append(i)
    return primes

angka = int(input("masukkan angka: "))
print(cetak_prime(angka))