# def hello_world():
#     print("Hello World!")
#     hello_world()

# hello_world()

def hitung_mundur(n):
    if n <= 0:
        print("Stop!")
    else:
        print(n)
        hitung_mundur(n - 1)


hitung_mundur(5)