T = int(input())

for tc in range(1, T+1):
    N= int(input()) #갯수
    tenarray = [[[0] * 10] * 10]

    for nc in range(N):
        nums = list(map(int, input().split())) #숫자화
        a,b,c,d,e = nums


    #여기에 문제로직이 들어감
        if e == 1:
            for i in range(a-1,c):
                for j in range(b-1,d):
                    if tenarray[i][j] == 0:
                        tenarray[i][j] == 1
                    else:
                        tenarray[i][j] == 1
            
        else:
            for i in range(a-1,c):
                for j in range(b-1,d):
                    if tenarray[i][j] == 1:
                        tenarray[i][j] == 2
                    else:
                        tenarray[i][j] == 1


    answer = tenarray.count[2]
            
    #최종 출력 예시
    print('#{} {}'.format(tc, answer))