# 4839_binarysearch

문제출처: [SW Expert Academy](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg)

```
문제 - A, B에서 이진탐색 게임을 시킨다 
끝페이지(page), 각각 찾을 페이지(a,b) 를 주고 누가 먼저 찾는지?
```

```python
T = int(input())
for tc in range(1, T+1):
    P,Pa,Pb = map(int,input().split()) # 1<= P, Pa, Pb <=1000
    pages =[1,P] #첫번째 페이지/ 끝페이지
    
    A_cnt = 0 #A가 이겼을때 1로 바뀜
    B_cnt = 0 #B가 이겼을 때 1초 바뀜
    for j in range(10): # 2^10 = 1024, P<=1000이므로 10회 반복되면 1~1000까지 모든페이지를 담을수있다
        element =[] #이진 탐색후 페이지 리스트
        for i in range(len(pages)-1):
            pg_i = int((pages[i]+pages[i+1])/2)
            element.append(pg_i) #리스트에 담기
        pages = list(set((pages + element))) #페이지와 엘리먼트를 합해서 중복 제거
        pages.sort() #순서대로 정렬
        if pages.count(Pa) == 1: #Pa값이 있을경우
            A_cnt += 1
            
        if pages.count(Pb) == 1: #Pb값이 있을경우
            B_cnt += 1

        if A_cnt != 0 or B_cnt != 0: #A나 B가 먼저이겼을 경우 반복중단
            break    
        
    
    if A_cnt > B_cnt:
        answer ="A"
    elif A_cnt < B_cnt: 
        answer = "B"
    else:
        answer = 0
    print('#{} {}'.format(tc,answer))

        
```

지수님

```python
# page는 끝페이지, target은 찾을 페이지 
def binary_search(page, target):
    start = 1     # 시작점 
    end = page    # 끝점
    count = 0 # 검색 수행할 때마다 +1 
    
    # 이진탐색 구현하는 while문
    while start <= end: 
        mid = int((start+end) / 2) # 중앙점
        if mid == target: 
            # 중앙점과 target 일치 -> count 리턴
            return count
        elif mid < target: # 중앙점이 타겟보다 작으면
            start = mid # 시작점을 중앙점으로 바꿈 
            count += 1 
        elif mid > target: # 중앙점이 타겟보다 크면
            end = mid  # 끝점을 중앙점으로 바꿈  
            count += 1
            
            
```

```python
T = int(input())
for tc in range(1, T + 1):
    # 책 끝페이지, a가 찾을 페이지, b가 찾을 페이지
    page, a, b = map(int, input().split())
    
    count_a = binary_search(page, a) 
    count_b = binary_search(page, b)
    
    if count_a > count_b: 
        result = 'B'
    elif count_b > count_a:
        result = 'A'
    else:
        result = 0 
    
    print(f'#{tc} {result}')
```

