def fact_iter(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

def fact_recursion(n):
    if n <= 1:
        return 1
    return fact_recursion(n-1) * n

if __name__ == "__main__":
    number = int(input("masukkan angka: "))
    print(fact_iter(number))
    print(fact_recursion(number))