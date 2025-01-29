def iteration(n):
    hasil = 0
    for numbers in n:
        hasil += numbers
    return hasil

def recursion(numbers, index):
        if index >= len(numbers):
            return 0
        else:
            return numbers[index] + recursion(numbers, index + 1)




if __name__ == "__main__":
    Numbers = [1,2,3,4,5]
    print(iteration(Numbers))
    print(recursion(Numbers, 0))