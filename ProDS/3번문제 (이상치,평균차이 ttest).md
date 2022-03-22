```
import pandas as pd
import numpy as np

data3 = pd.read_csv('Dataset_03.csv')
data3.columns
#['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide','nose_long', 'lips_thin', 'distance_nose_to_lip_long', 'gender']
```





# 1-1. 비율(forehead_ratio) 생성
```
q1 = data3.copy()
q1['forehead_ratio'] = q1['forehead_width_cm']/q1['forehead_height_cm']
```



# 1-2. 이상치데이터

## (1) 평균, 표준편차

> 비율 기준 평균으로부터 3 표준편차밖의경우: 

```
UB = xbar + 3*std, LB = xbar - 3*std

xbar = q1['forehead_ratio'].mean() 
std = q1['forehead_ratio'].std()

LB = xbar - (3*std)
UB = xbar + (3*std)

(q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] >UB)
for i in np.arange(len(q1)):
    (q1['forehead_ratio'][i] < LB) or (q1['forehead_ratio'] >UB)
```



## (2) 이상치 데이터
```
((q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] >UB)).sum()
```

>답: 3



# 2. 평균차이 검정

대응 t검정: 데이터가 쌍이되어야=> 순서/ 수가같아야만 가능 =>단일:평균으로

독립: 각그룹별평균=>모집단평균과 비교=>순서/수 관계X

이분산t검정: 등분산t검정 제외

>2표본 평균차이 검정: ttest
>
>- ttest_ind: 독립인 이표본 t 검정, 등분산 검정 수행 후 등분산 여부를 반영
>
>- ttest_rel: 대응인 이표본 t 검정, 데이터 수와 순서 고려
## (1) 등분산 검정을 수행
```python
from scipy.stats import ttest_ind, bartlett, levene


bartlett_out = bartlett(q1[q1.gender == 'Male']['forehead_ratio'],
                        q1[q1.gender == 'Female']['forehead_ratio'])

# BartlettResult(statistic=213.42228096491922, pvalue=2.4617792693952707e-48)
```


>H0: 등분산이다
>H1: 등분산이 아니다(이분산이다)
>
>bartlett_out.pvalue<0.05 =>등분산이다




## (2) 평균 차이 검정
```python
ttest_out = ttest_ind(q1[q1.gender == 'Male']['forehead_ratio'],
                      q1[q1.gender == 'Female']['forehead_ratio'],
                      equal_var=False) # 이분산:False(가정)
```

## (3) 검정통계량의 추정치

dir(ttest_out)
round(abs(ttest_out.statistic),3)

> 답 :2.999

## (4) 신뢰수준 99%

> 양측 검정을 수행(기본)하고 결과는 귀무가설 기각의 경우 Y로, 그렇지 않을 경우 N으로 답하시오.
  유의수준= 0.01

ttest_out.pvalue < 0.01

> 답 : 2.999, Y(True=>기각)



# 3. 로지스틱 회귀

## (1) 데이터셋선정

```python
from sklearn.model_selection import train_test_split

train, test = train_test_split(data3, test_size=0.3, random_state=123)
```



## (2) 변수선정
>원 데이터에 있는 7개의 변수만 Feature로 사용하고 gender를 label로 사용

```python
var_list = data3.columns.drop('gender')
len(var_list)
```



## (3) [train_dataset 이용] 로지스틱 회귀분석 예측함수
```python
from sklearn.linear_model import LogisticRegression

logit = LogisticRegression().fit(train[var_list],train['gender'])

pred_class = logit.predict(test[var_list])
```

```
# 만약 임계값 0.7인경우
pred_pr = logit.predict_proba(test[var_list])
pred_class2 = np.where(pred_pr[:1] >=0.7, 'Male','Female')
```

> 알파벳순으로 negative0/positive1로 지정됨 지정하려면 np.where
확률높은것을=>파시티브

## (4) Test dataset 사용 예측수행하고 정확도 평가
>이 때 임계값은 0.5를 사용한다.
Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술

```python
from sklearn.metrics import precision_score, classification_report

round(precision_score(test['gender'], pred_class, pos_label = 'Male'),2)

#[참고] 종합적으로 결과보기
print(classification_report(test['gender'],pred_class))

# 카테고리 지정하기
y = pd.Categorical(train['gender'],categories = ['Male','Female'])
male: 0 female :1
logit2 = LogisticRegression().fit(train[var_list],y)

pred_pr2 = logit2.predict_proba(test[var_list])
pred_class3 = logit2.predict(test[var_list])

y.value_counts()
```

>

