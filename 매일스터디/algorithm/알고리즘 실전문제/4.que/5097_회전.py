T = int(input())
for tc in range(1,T + 1):
    N, M = list(map(int,input().split())) 
    nums = list(input().split())
    for i in range(M):
        start = nums.pop(0)
        nums.append(start)
        answer = nums[0]
    
    print("#{} {}".format(tc, answer))
