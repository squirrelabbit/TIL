def RSP(x,y): #1<2<3<1
    rsp_x = [[1,3],[2,1],[3,2]] #x가 이기는 경우
    rsp_y = [[1,2],[2,3],[3,1]] #y가 이기는 경우
    if card[x] == card[y]: #같을때는 번호가작은쪽 즉 왼쪽이 이긴다
        return x
    else:
        if [card[x],card[y]] in rsp_x: #x값이 이기는경우
            return x    #카드번호인x를 반환
        else:
            return y

def half(start,end): 
    if start == end: # 각각 한명이되는경우
        return start #자기자신이됨
    a = half(start, (start+end)//2) #재귀함수=>위 if문에 걸릴때까지 반복됨
    b = half((start+end)//2 +1, end)
    return RSP(a,b) #각각 하나씩되면 RSP함수를 써줌

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(map(int,(input().split())))
    
    answer = half(0,N-1)+1 #인데스 번호값으로 함수설정=> +1을 해준다
    print("# {} {}".format(tc, answer))
