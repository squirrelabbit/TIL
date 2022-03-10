# 4874 forth

## 문제

```
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
결과값은 연산결과
만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
```

## 빌드업

```
에러가나는 경우 처리를 어떻게 할것인가
연산자와 숫자의 구분 
```

## 코드-1

에러처리: try/except

```python
T = int(input())
for tc in range(1,T+1):
    data = list(input().split())
    N = len(data)
    stack = []
    flag = 0

    # 마침표는 제외하기 위해 N-1까지 반복
    for i in range(N-1):  
        
        #숫자인 경우, stack에 append
        if data[i].isdigit():
            stack.append(data[i])

        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if data[i] == "+": result = num1 + num2
                elif data[i] == "-": result = num1 - num2
                elif data[i] == "/": result = num1 / num2
                elif data[i] == "*": result = num1 * num2
                stack.append(result)
            
            except: #에러 발생 예외 처리 예) 숫자 + 연산자 + 연산자
                flag = 333 ##임의의 숫자
    #예외처리 조건 (X) + Stack의 길이가 1인 경우(계산이 성공적인경우)
    if flag == 0 and len(stack) == 1:
        print(f'#{tc} {stack[0]}')

    #예외처리 조건 (O) + stack의 길이가 2이상인 경우 ex) 숫자만 입력된 경우
    elif flag == 333 or len(stack)>1:
        print(f'#{tc} error')
```

## 코드-2

에러처리:

1. "."일때 stack에 결과값만있지않은경우->에러 

2. 연산자일때 (스택에 숫자가 2개이상없을때->에러)

   람다함수로 딕셔너리 설정

   operators = {
           '+': lambda x, y: x + y, 
           '-': lambda x, y: x - y, 
           '*': lambda x, y: x * y, 
           '/': lambda x, y: x // y, 
           }     

   연산자 = operators.keys()

3. 숫자일때 걍 스택에 추가

```python
T = int(input())
for tc in range(1,T+1):
    data = input().split()
    stack = []
    operators = {
        '+': lambda x, y: x + y, 
        '-': lambda x, y: x - y, 
        '*': lambda x, y: x * y, 
        '/': lambda x, y: x // y, 
        }        #기호에 대한 연산자를 만들어둔다.



    # 마침표는 제외하기 위해 N-1까지 반복
    for i in data:  
        if i == '.': #만약 '.'가 나왔을때 
            if len(stack) > 1: #stack에 결과값하나만 있지않은경우
                result = "error" #error를 도출하고
            else:
                result = int(stack.pop()) #stack이 비어있지 않으면 정수로 변환 후 pop한것을 결과


        elif i in operators.keys():
            if len(stack) < 2: #만약 stack이 계산할 수 없는 상황일때 
                result = "error" #error를 도출 
                break 
            else: 
                a = int(stack.pop()) #a는 pop한 정수
                b = int(stack.pop()) #b는 pop한 정수 
                c = operators[i](int(b), int(a)) #연산자의 i번째를 계산
                stack.append(int(c)) #정수로 변환후 stack에 추가 
        else : stack.append(i) 
    
    print("#{} {}".format(t, result))


# 출처: https://totoma3.tistory.com/131 [토토모의 분석일지]

```

