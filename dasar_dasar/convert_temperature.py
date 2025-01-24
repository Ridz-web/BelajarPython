print("PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("masukkan suhu dalam celcius: "))
print(f"suhu adalah: {celcius} Celcius")

# reamur: (4/5)C
reamur = ( 4 / 5 ) * celcius
print(f"{celcius} Celcius = {reamur} Reamur")

#fahrenheit: ( (9/5) C ) + 32
fahrenheit = ( ( 9 / 5 ) * celcius ) + 32
print(f"{celcius} Celcius = {fahrenheit} Fahrenheit")

#kelvin: C + 273
kelvin = celcius + 273
print(f"{celcius} Celcius = {kelvin} Kelvin")
