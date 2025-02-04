x = [i for i in range(1, 11)]
print(x)

# matrix of 3x3
M,N = 3,3
matrix = []
for m in range(M):
    rows = []
    for N in range(N):
        rows.append(1)
    matrix.append(rows)

R,C = 3,3
matrix2 = [[1 for c in range(C)] for r in range(M)]

print(matrix)
print(matrix2)

genap = [i for i in range(1, 21) if i % 2 == 0]
print(genap)

one = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(one)

vocal = "python adalah bahasa pemograman yang menarik"
vocal_list = [i for i in vocal if i in "aeiou"]
print(vocal_list)

pangkat2 = [i**2 for i in range(1,11)]
print(pangkat2)

buah = ["Apple", "Banana", "Cherry", "Orange", "Eagle"]
new_buah = [i[::-1] if i[0].upper() in "AEIOU" else i.lower() for i in buah]
print(new_buah)