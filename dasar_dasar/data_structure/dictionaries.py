bahasa_pemograman = {1: "Python", 2: "Java", 3: "c++"}

# get value bahasa_pemograman
print("mendapatkan value")
for value in bahasa_pemograman.values():
    print(f"values: {value}")

# get key bahasa_pemograman
print("\nmendapatkan key")
for key in bahasa_pemograman.keys():
    print(f"key: {key}")

# get value and key
print("\nmendapatkan keduanya")
for key, value in bahasa_pemograman.items():
    print(f"key: {key}, value: {value}")

def count_word(words: str) -> dict[str, int]: # menghitung berapa banyak kata yang terduplikat/sama
    word_map = {}
    for word in words.split():
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    return word_map

words = "This document is a document of words. are important. This document"
print(count_word(words))