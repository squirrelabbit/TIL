T = int(input())
for tc in range(1,T +1 ):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()
    ordered_list = []
    for i in range(5): #10/2
        ordered_list.append(numbers.pop(N-1-2*i))
        ordered_list.append(numbers.pop(0))
    answer =  " ".join(map(str, ordered_list))
    print('#{} {}'.format(tc, answer))