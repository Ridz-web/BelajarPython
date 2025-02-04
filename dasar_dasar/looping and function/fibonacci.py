panjang = int(input("masukkan angka "))

a, b = 0, 1 
for _ in range(panjang):
    print(a, end=" ") 
    a, b = b, a + b 