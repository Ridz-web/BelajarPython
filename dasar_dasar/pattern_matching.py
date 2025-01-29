

if __name__ == "__main__":
    operation = input("Enter operation : ")
    number1 = int(input("Enter number 1 : "))
    number2 = int(input("Enter number 2 : "))
    
    match operation:
        case "add":
            result = number1 + number2
        case "sub":
            result = number1 - number2
        case "div":
            result = number1 / number2
        case "multiply":
            result = number1 * number2
        case _:
            result = -1
            print("invalid input")
    print("result: ", result)
