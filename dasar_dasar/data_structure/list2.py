numbers = [1,2,3,4,5]
numbers.extend([6,7])

buah = ["apel", "nanas", "semangka"]
buah.sort(key=len)

print(f"extend: {numbers}")
print(f"pop: {numbers.pop()}")

numbers.insert(1, 'a')
print(f"insert: {numbers}")

print(f"sort: {buah}")