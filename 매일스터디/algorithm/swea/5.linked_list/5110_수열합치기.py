T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    array = [list(map(int,input().split())) for _ in range(M)] #다차원으로받음
    first = array.pop(0) # 뽑아냄
    
    for i in array: #남은 수열을 순서대로
        for j in range(N): #수열 갯수범위내에서
            if i[0] < first[j]: #남은수열 첫번째값과 수열1번의 각 원소비교후
                
                first[j:j] = i #삽입 중요!!(리스트형태가아닌원소로들어감)
            
                break #첫번째 큰값에서 삽입하고 나오기
        else: # for else문!! 중요 for문 아닌경우 else문으로 감
            first.extend(i)
    
    answer = first[-1:-11:-1] #10개 역순
    print('#{}'.format(tc), end = ' ') #end로 \n없애고 띄우기넣어줌
    print(*answer) #리스트 원소로 출력
    