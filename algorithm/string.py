customers = 'alex@hphk.kr'
real_id = ''  # 일단 id 를 모아줄 변수를 하나 설정하고
print(customers[::-1])
for letter in customers[::-1]:  # 문자열을 하나씩 돌아볼건데,
    if letter != '@':  # 골뱅이가 아닌 경우에만
        real_id += letter  # 아까 변수에 모아주고
    else:  # 골뱅이를 발견하는 순간 
        break  # 포문을 파괴하자!
real_id=real_id[::-1]
print(real_id)
