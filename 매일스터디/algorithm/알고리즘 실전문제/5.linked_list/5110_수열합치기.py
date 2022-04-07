T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    array = [list(map(int,input().split())) for _ in range(M)]
    first = array.pop(0)
    
    for i in array:
        for j in range(N):
            if i[0] < first[j]:
                first[j:j] = i
                break
        else:
            first.extend(i)
    
    answer = first[-1:-11:-1]
    print('#{}'.format(tc), end = ' ')
    print(*answer)