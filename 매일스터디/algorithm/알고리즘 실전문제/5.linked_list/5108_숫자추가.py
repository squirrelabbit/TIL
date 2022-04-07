T = int(input())
for tc in range(1,T+1):
    N,M,L = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    for i in range(M):
        idx, val = list(map(int,input().split()))
        nums.insert(idx,val)
    
    answer = nums[L]
    print('#{} {}'.format(tc, answer))
