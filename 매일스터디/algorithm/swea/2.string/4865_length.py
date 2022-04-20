T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
#################################### 문자열 잘라내기(컴프리헨션은 꼭 range??)
    str1_c = [str1[i:i+1] for i in range(len(str1))]
    str2_c = [str2[i:i+1] for i in range(len(str2))]
############################################카운트
    count_list = []
    for i in range(len(str1_c)):
        count = str2_c.count(str1_c[i])
        count_list.append(count)
##########################################답찾기
    answer = max(count_list)

    print('#{} {}'.format(tc, answer))
