numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
siswa= [100, 90, 80, 70, 60, 50 ,30, 0]

even_numbers = [number for number in numbers if number % 2 == 0]
numbers2 = [number * number for number in range(1, 11)]
siswa_lulus = list(filter(lambda x: x >= 60, siswa))
siswa_lulus2 = [lulus if lulus >= 60 else "gagal" for lulus in siswa]

even_ten = [even for even in numbers if even % 2 == 0 and even >= 10]

python = ["hello", "world", "python", "is", "great"]

saring = [i.upper() for i in python if len(i) >= 4]

hello = 'hello'
print(len(hello))

print(even_numbers)
print(numbers2)
print(siswa_lulus)
print(siswa_lulus2)
print(even_ten)
print(saring)