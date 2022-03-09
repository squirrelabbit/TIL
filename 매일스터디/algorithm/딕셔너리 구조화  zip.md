

# 딕셔너리 구조화 / zip

```f = dict(zip(range(1,4),[0,0,0]))
f = dict(zip(range(1,4),[0,0,0]))
```

`주의`  key값은 변하는 것이 지정안됨 따라서 리스트는 key값X



전치=>zip함수활용

```
# 풀이2
T = int(input())

for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]

    longest_word= 0  # 일단 제일 긴게 뭔지부터 확인합니다.
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)

    for idx, word in enumerate(words):  # 짧은 애들 있으면 뒤에 안쓸만한 - 이런거 하나 붙여서 길이 맞춰 줍니다.
        if len(word) < longest_word:
            word.extend(['-']*(longest_word-len(word)))
            words[idx] = word

    transposed_words = list(zip(*words))  # 세로로 찝으면 전치 효과를 줄 수 있어요

    answer = ''
    for vertical_line in transposed_words:  # 각각 하나씩 가로로 뽑아서 볼때 (원리스트 기준으론 세로로 보는것과 같습니다)
        for letter in vertical_line:  # 그 문자 자체가
            if letter != '-':  # 공간 채우기용으로 넣어뒀던 문자가 아니라면
                answer += letter  # 읽어줍니다!

    print('#{} {}'.format(tc, answer))
```

