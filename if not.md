## **if not**

  

 

```
if True:
    print('참') # True 는 참 
else:
    print('거짓')
    
if False:
    print('참')
else:
    print('거짓') # False 는 거짓

if None:
    print('참')
else:
    print('거짓') # None 은 거짓
```

![img](https://blog.kakaocdn.net/dn/bGXwiV/btqPTEHYdOn/3qkeuXd1kCPGUJ7GytUKgK/img.png)

값 자체가 있으면 if는 동작

반대로 0, None, ' '은 False로 취급하므로 else가 동작

 

```
if not 0:
    print('참')
    
if not None:
    print('참')

if not '':
    print('참')
```

참

참

참



출처: https://sikaleo.tistory.com/100 [SIKALEO]

if not 