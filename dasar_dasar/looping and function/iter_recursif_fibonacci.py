def fibonacci_iter(n):
   a,b = 0,1
   string = str(a)
   for _ in range(n):
       string += str(b)
       a,b = b, a+b
   return string

def fibonacci_recursion(n, a=0, b=1):
    if n <= 1:
        return str(a)
    elif n == b:
        return str(a) + str(b)
    else:
        return str(a) + fibonacci_recursion(n - 1, b, a + b)

if __name__ == "__main__":
    n = int(input("masukan angka: "))
    print("Fibonacci (rekursif):", fibonacci_recursion(n))
    print("Fibonacci (iteratif):", fibonacci_iter(n))