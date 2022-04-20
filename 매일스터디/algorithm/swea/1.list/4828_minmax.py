T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    #여기에 문제로직이 들어감
    answer = max(nums) - min(nums)
    
    #최종 출력 예시
    print('{} {}'.format(tc, answer))