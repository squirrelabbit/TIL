T = int(input())
for tc in range(1,T+1):
    N,M,L = list(map(int,input().split())) #N:수열길이 M:반복횟수 L:출력인덱스
    nums = list(map(int,input().split())) #수열받기
    for i in range(M): #M번규칙반복
        temp = input().split() #편집규칙커맨드받기
        comm = temp.pop(0) #첫번째값 뽑기
                
        if comm == 'I': #i일때
            idx = int(temp[0]) #정수로 변환
            val = int(temp[1])
            nums.insert(idx,val) #삽입
        elif comm == 'D': #d일때 
            idx = int(temp[0])
            nums.pop(idx) #제거
        else: #c일때
            idx = int(temp[0])
            val = int(temp[1])
            nums[idx] = val #값변경
    if L<=len(nums): #L인덱스가 수열범위에 있을때 출력
        answer = nums[L]
    else:
        answer = -1 #아니면 -1출력
    print ("#{} {}".format(tc,answer))
