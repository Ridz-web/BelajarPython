def reverse(s):
    n = len(s)
    for i in range(n // 1):
       if s[i] != s[n - i - 1]:
           return False
    return True

if __name__ == "__main__":
    string = input("masukan kata: ")
    print(reverse(string))