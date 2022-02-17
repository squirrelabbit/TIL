# input()

str_num = input()
print(str_num, type(str_num))
num = int(str_num)
print(num, type(num))



vs



num = int(input())
print(num, type(num))



1번풀이

```
str_nums = input()
nums= str_nums.split()
print(nums)

num_a = []
for num in nums:
    num_a.append(int(num))

print(num_a)
```

2번풀이

[map함수]([TIL/map함수.md at master · squirrelabbit/TIL (github.com)](https://github.com/squirrelabbit/TIL/blob/master/map함수.md))

nums = map(int(), input().split()))