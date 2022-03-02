# if \_\_name\_\_ == "\_\_main\_\_"

## 필요성

hello 파일 안의 hello 함수만 가져다 쓰고 싶다면, hello.py 파일 안에 if\_\_name\_\_==“\_\_main\_\_” 이 필요

그글밑의 print()함수는 import된곳에서는 실행안되고 함수만 import됨

![image-20220302150807331.png](https://github.com/squirrelabbit/TIL/blob/master/4.%EC%9E%90%EC%97%B0%EC%96%B4%20%EC%B2%98%EB%A6%AC/if%20__name__%20==%20__main__.assets/image-20220302150807331.png?raw=true)



## 원리

파이썬 파일들은 모두 만들어지면 \_\_name\_\_이 생긴다 

파일 안에서 \_\_name\_\_ 은 “\_\_main\_\_” 으로 정의된다. 

하지만 다른 파일에서 import되어서 사용될 때는

 -> 파일명.\_\_name\_\_은 “파일명”이 된다 if문 false가 됨 

따라서 함수만 import