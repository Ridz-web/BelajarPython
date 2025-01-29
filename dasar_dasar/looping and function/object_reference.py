list = [1, 2, 3] # objek yang dapat di ubah/ mutable object
def new_list(lst):
    lst.append(4)

print(f"before: {list}") # nilai default dari list
new_list(list) # list dimomdifikasi menggunakan function
print(f"after: {list}")

nama = "Ridho" # string, integer,float adalah immutable object/tidak bisa di ubah nilainya
def new_name(nama):
    nama = "Ridz"
    return nama

print(f"\nbefore: {nama}")
new_name(nama)
print(f"after: {nama}") # output tetap memunculkan 'Ridho'
