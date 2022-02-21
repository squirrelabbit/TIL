T = int(input())
for tc in range(1, T + 1):
    N,K = map(int, input().split())
    A = [i for i in range (1,13)]
########################################
    # 부분집합구하기
    subset = [] #부분집합 리스트
    for i in range(1 << 12):
        element = [] #부분집합
        for j in range(12):
            if i & (1<<j):
                element.append(A[j])
        if len(element) == N:
            subset.append(element)

#########################################
    # 부분집합 합구하기
    count = 0
    for i in range (len(subset)):
        total = 0
        for j in subset[i]:
            total += j
        if total == K:
            count += 1

##########################################
    # 답구하기
    print('#{} {}'.format(tc,count))
