![image-20220307144357178](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220307144357178.png)

![image-20220307144412302](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220307144412302.png)

![image-20220307144446937](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220307144446937.png)

![image-20220307144459083](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220307144459083.png)



# select

![image-20220307144535833](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220307144535833.png)

- 공백/ 줄바꾸기도 사용가능(무시됨)

● SELECT USER_NAME, GENDER FROM USER_INFO;

● SELECT * FROM USER_INFO;(전부)



## 정리

![image-20220307144748126](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220307144748126.png)

export / import가능

# 정렬(orderby)

![image-20220307152723977](sql 기초.assets/image-20220307152723977.png)

![image-20220307152746976](sql 기초.assets/image-20220307152746976.png)



# 중복제거(distinct, count)

## distinct

![image-20220307153244010](sql 기초.assets/image-20220307153244010.png)

## All

![image-20220307153315124](sql 기초.assets/image-20220307153315124.png)

## count:로우갯수

![image-20220307153343568](sql 기초.assets/image-20220307153343568.png)

![image-20220307153402998](sql 기초.assets/image-20220307153402998.png)

![image-20220307153421610](sql 기초.assets/image-20220307153421610.png)

## distinct + count

![image-20220307153448953](sql 기초.assets/image-20220307153448953.png)

# 별칭

![image-20220307153547112](sql 기초.assets/image-20220307153547112.png)

![image-20220307153610930](sql 기초.assets/image-20220307153610930.png)

# 조건절(where, limit)

## 조건절 연산자

![image-20220307153716552](sql 기초.assets/image-20220307153716552.png)

![image-20220307153727129](sql 기초.assets/image-20220307153727129.png)

## and &&

![image-20220307174735291](sql 기초.assets/image-20220307174735291.png)

## limit

![image-20220307174821966](sql 기초.assets/image-20220307174821966.png)

## isnull isnotnull

 MySQL에서 NULL은 가장 작은 값으로 정렬 됨(데이터베이스마다 다름)

-  아래 데이터에서 name이 South Korea가 아닌 나라의 수를 세려면?

![image-20220307175054036](sql 기초.assets/image-20220307175054036.png)

## if null

![image-20220307175325942](sql 기초.assets/image-20220307175325942.png)
