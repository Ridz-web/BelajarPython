from collections import defaultdict,OrderedDict,Counter

buah = defaultdict(int)

buah['apple'] += 1
buah['banana'] += 2

total_buah = Counter(['apple', 'banana', 'orange', 'banana', 'banana', 'apple'])

if __name__ == "__main__":
    print('\ndefaultdict')
    print(buah['apple']) # output 1
    print(buah['banana']) # output 2
    print(f"{buah['orange']}\n") # output 0



    print("orderedDict")
    buah = OrderedDict()
    buah['apple'] = 1
    buah['banana'] = 2
    buah['orange'] = 3
    print(f'{buah}\n')
    
    print("Counter")
    print(total_buah)
    