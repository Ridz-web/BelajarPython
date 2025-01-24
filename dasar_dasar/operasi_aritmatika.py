# pertambahan +
x = 10
y = 3
hasil = x + y
print(x , '+', y, '=', hasil)

# pengurangan -
x = 10
y = 3
hasil = x - y
print(x , '-', y, '=', hasil)

# perkalian *
x = 10
y = 3
hasil = x * y
print(x , '*', y, '=', hasil)

# pembagian /
x = 10
y = 3
hasil = x / y
print(x , '/', y, '=', hasil)

# eksponen(pangkat) **
x = 10
y = 3
hasil = x ** y
print(x , '**', y, '=', hasil)

# modulus(sisa pembagian) %
x = 10
y = 3
hasil = x % y
print(x , '%', y, '=', hasil)

# floor division(semacam pembulatan) //
x = 10
y = 3
hasil = x // y
print(x , '//', y, '=', hasil)

# prioritas operasi, operasional presedence ()
x = 10
y = 3
z = 4
hasil = x + y / (x * y) % z # x * y akan didahulukan
print(x,'+',y,'/',(x,'*',y),'%',z,'=', hasil)
