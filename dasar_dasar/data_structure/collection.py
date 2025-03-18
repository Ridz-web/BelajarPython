from collections import defaultdict,OrderedDict,Counter,deque

buah = defaultdict(int)

buah['apple'] += 1
buah['banana'] += 2

new_buah = OrderedDict()
new_buah['apple'] = 1
new_buah['banana'] = 2
new_buah['orange'] = 3

total_buah = Counter(['apple', 'banana', 'orange', 'banana', 'banana', 'apple'])

buah_deque = deque([1,2,3])
buah_deque.append(4) # add to right end
buah_deque.appendleft(0) # add to left end

if __name__ == "__main__":
    print('\ndefaultdict')
    print(buah['apple']) # output 1
    print(buah['banana']) # output 2
    print(f"{buah['orange']}\n") # output 0



    print("orderedDict")
    print(f'{new_buah}\n')
    
    print("Counter")
    print(total_buah)
    print(f"{total_buah.most_common(1)}\n")
    
    print("deque")
    print(buah_deque)
    print(buah_deque.pop())
    print(buah_deque.popleft())
    