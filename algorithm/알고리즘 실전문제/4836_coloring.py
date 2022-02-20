T = int(input())

for tc in range(1, T+1):
    N= int(input()) #갯수
    e1_list = []
    e2_list = []

    for nc in range(N):
        nums = list(map(int, input().split())) #숫자화
        a,b,c,d,e = nums


    #여기에 문제로직이 들어감
        if e == 1:
            for i in range(a,c+1):
                for j in range(b,d+1):
                    e1_list.append((i,j))
        else:
            for i in range(a,c+1):
                for j in range(b,d+1):
                    e2_list.append((i,j))


    answer = len(list(set(e1_list) & set(e2_list)))
            
    #최종 출력 예시
    print('#{} {}'.format(tc, answer))