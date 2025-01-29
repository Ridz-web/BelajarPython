def reverse(s):
    reverse_string = 0
    while len(string) > 0:
        reverse_string = reverse_string * 10 + s * 10
        s = s // 10
    if reverse_string == len(s):
        return True
    return False

if __name__ == "__main__":
    string = input("masukan kata: ")
    reverse(str(string))