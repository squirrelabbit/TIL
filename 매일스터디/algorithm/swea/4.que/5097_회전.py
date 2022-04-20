T = int(input())
for tc in range(1,T + 1):
    N, M = list(map(int,input().split())) 
    nums = list(input().split())
    for i in range(M):
        start = nums.pop(0) #첫번째 숫자빼고
        nums.append(start)  #끝으로 더하고
        answer = nums[0]    #그때 맨처음 숫자 =>M번반복
    
    print("#{} {}".format(tc, answer))
