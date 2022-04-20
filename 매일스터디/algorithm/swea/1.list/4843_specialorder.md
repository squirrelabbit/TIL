# 4843_specialorder

문제

```
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
```

답

```python
T = int(input())
for tc in range(1,T +1 ):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort() 
    ordered_list = []
    for i in range(5): #10/2
        ordered_list.append(numbers.pop(N-1-2*i)) 
        #정렬후 가장 마지막값 = 가장큰값
        ordered_list.append(numbers.pop(0))
        #정렬후 가장 첫번째값 = 가장작은값
    answer =  " ".join(map(str, ordered_list)) 
    #str아닌 값을 join으로 합치기위해 str함수를 map으로 적용시킨 후 join함수로 합쳐줌
    print('#{} {}'.format(tc, answer))
```

추가사항

reverse()함수이용해서 max값찾아보기
