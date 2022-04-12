# 5174_subtree

## 문제

```
간선 E개의 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
노드번호 = E+1
```

## 입력

```
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
```

## 출력

```
#1 3
#2 1
#3 3
```

## 접근

이진트리=> 자식노드는 최대 2개

tree 2차원리스트 => row = 자식넘버/ 컬럼 = 부모넘버

## 코드

```python
def sub_tree(idx): 
    global count  # 횟수세기

    for i in range(2): #자식 row 0,1 탐색
        if tree[i][idx]: # 해당되는 곳에 값이 있으면
            count += 1 # 카운트 증가
            nidx = tree[i][idx] # 그값을 인덱스값으로 활용
            sub_tree(nidx) # 다음 세대 확인(반복)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int,input().split()))
    
    # 문제에 주어진것 처럼 row 기준으로 0, 1로 활용
    tree = [[0 for _ in range(E+2)]for _ in range(2)] 
    #노드번호 = E+1=> 인덱스때문에 E+1+1

    for i in range(E): #간선E개에 대해서
        
        idx = temp[2*i]
        number = temp[2*i+1]
        
        if not tree[0][idx]: # 값이없다면
            tree[0][idx] = number #값할당
        
        else: #  이미 있다면 가지 하나 더 만들어줌
            tree[1][idx] = number

    # 시작하면서 자동으로 하나 포함
    count = 1
    # N부터 실행
    sub_tree(N)
    print("#{} {}".format(tc, count))
```

