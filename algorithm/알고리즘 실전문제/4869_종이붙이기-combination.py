T = int(input())
for tc in range(1,T+1):
    H = (int(input()))/10
    print(H)
    #기본도형모형
    #(1,2) (2,1) (2,2)
    #############가로합 = H / 세로합 = 2
    combi = []
    for a in range(31) :
        for b in range(15):
            for c in range(3):
                if a + 2 * b + 2 * c == H : ###가로(첫번째숫자)
                    combi.append([a,b,c])
    answer = 0
    print(combi)
    