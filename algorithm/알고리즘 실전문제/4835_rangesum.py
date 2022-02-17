T = int(input())

for tc in range(1, T+1):
    NR = input() #갯수/구간수
    N = int(NR.split()[0]) #갯수
    R = int(NR.split()[1]) #구간수


    nums = list(map(int, input().split())) #숫자화
    nums_sum_list = []
    
    #여기에 문제로직이 들어감
    for i in range(N-R+1):
        nums_sum = sum(nums[i:i+R]) #슬라이싱 합
        nums_sum_list.append(nums_sum)
        answer = max(nums_sum_list) - min(nums_sum_list)
    
    #최종 출력 예시
    print('#{} {}'.format(tc, answer))