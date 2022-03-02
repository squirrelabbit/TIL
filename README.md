# TIL

## 멀티캠퍼스 정규과정(12/13~)

### 1. 파이썬 기본 문법

- 리스트

- 문자열

- 딕셔너리

### 2. 웹크롤링 

- EDA

  - [matplolib](https://github.com/squirrelabbit/TIL/blob/master/matplolib.md)
  - seaborn
  - [상관관계](https://github.com/squirrelabbit/TIL/blob/master/%EC%83%81%EA%B4%80%EA%B4%80%EA%B3%84%20EDA.md)

### 3. 머신러닝
- 1. 넘파이 사이킷런

  2. 표본추출

  3. 데이터 전처리

  4. [평가(evaluation)](https://github.com/squirrelabbit/TIL/blob/master/2.%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/3.%20%ED%8F%89%EA%B0%80(evaluation).md)

  5. [회귀분석(regression)](https://github.com/squirrelabbit/TIL/blob/master/2.%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/5.%20%ED%9A%8C%EA%B7%80(regression).md)

  6. [분류(classification)](https://github.com/squirrelabbit/TIL/blob/master/2.%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/4.%20%EB%B6%84%EB%A5%98(classification).md)
  
     

### 4. 추천 알고리즘

  - [CBF](https://github.com/squirrelabbit/TIL/blob/master/3.%EC%B6%94%EC%B2%9C%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/CBF.md)

  - [KNN(CF)](https://github.com/squirrelabbit/TIL/blob/master/3.%EC%B6%94%EC%B2%9C%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/CF_KNN.md))

  - [MF(CF)](https://github.com/squirrelabbit/TIL/blob/master/3.%EC%B6%94%EC%B2%9C%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/CF_MF.md)

  - Surprise 기반

    

### 5. 딥러닝

  - [딥러닝 프로세스](https://github.com/squirrelabbit/TIL/blob/master/5.deeplearning/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4.md)
    - 딥러닝 프로세스
    
    - XOR문제(다층퍼셉트론/오차역전파/시그모이드)
    
    - 기울기소실문제(시그모이드외 활성화함수도입)
    
    - 확률적경사하강법(아담)
    
    - 다중분류문제해결(소프트맥스 활성화함수)
    
    - 과적합(train_set,test_set분류)-early stopping
    
      
    
- [딥러닝 keras 코드](https://github.com/squirrelabbit/TIL/blob/master/5.deeplearning/%EB%94%A5%EB%9F%AC%EB%8B%9D%20keras%20%EC%BD%94%EB%93%9C.md)
  
  - ThoraricSurgery(dense =2)
  - Pima_Indian (dense=3)
  - sonar (overfitting)

### 6. 자연어처리(NLP)

- [자연어 처리](https://github.com/squirrelabbit/TIL/blob/master/4.%EC%9E%90%EC%97%B0%EC%96%B4%20%EC%B2%98%EB%A6%AC/%EC%9E%90%EC%97%B0%EC%96%B4%20%EC%B2%98%EB%A6%AC%20(NLP).md)

  - 토큰화(text_to_word_sequence() )

  - Tokenizer()

      token = Tokenizer()             # 토큰화 함수 지정
      token.fit_on_texts(docs)        # 토큰화 함수에 문장 적용

  - #각 단어 빈도수 : .word_counts
     token.word_counts

  - #총 문장 수 : .document_count
    token.document_count
    
  - #각 단어가 몇개의 문장에 포함되어 있는가 : .word_docs
     token.word_docs
     
  - #각 단어에 매겨진 인덱스 값 : .word_index
     token.word_index)
     
  - embeded()
    ```
    Embedding(16, 4, input_length=2) : 총 입력되는 단어 수는 16개, 임베딩 후 출력되는 벡터 크기는 4, 단어를 매번 2개씩 집어 넣겠다는 뜻model.add(Embedding(26, 10, input_length=4))


  - pad_sequence()
  - 토큰화->token.

- [if \_\_name\_\_ == \_\_main\_\_](https://github.com/squirrelabbit/TIL/blob/master/4.%EC%9E%90%EC%97%B0%EC%96%B4%20%EC%B2%98%EB%A6%AC/if%20__name__%20%3D%3D%20__main__.md)

- [정규식을 통한 noise 제거](https://github.com/squirrelabbit/TIL/blob/master/4.%EC%9E%90%EC%97%B0%EC%96%B4%20%EC%B2%98%EB%A6%AC/%EC%A0%95%EA%B7%9C%EC%8B%9D.md)

## 특강

- [깃허브특강](https://github.com/squirrelabbit/TIL/blob/master/%EA%B9%83/%EA%B9%83%ED%97%88%EB%B8%8C%ED%8A%B9%EA%B0%95.md)
  - [마크다운 문법](https://github.com/squirrelabbit/TIL/blob/master/%EA%B9%83/markdown-basic.md)
- [취업특강](https://github.com/squirrelabbit/TIL/blob/master/%EC%B7%A8%EC%A4%80%ED%8A%B9%EA%B0%95.md) 



## 알고리즘 스터디
### 알고리즘 과정중 정리 문법

  - 비트연산자

  - 딕셔너리 구조화

  - formatting

  - input함수

  - map함수

  - 파이썬 슬라이싱

  - 행렬 좌표배치

    

### SW
- 4828 min_max
- [4834 숫자카드](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4834%20%EC%88%AB%EC%9E%90%EC%B9%B4%EB%93%9C.md)
- 4835 구간합
- [4836 색칠하기](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4836_coloring.md)
- [4837 부분집합 합](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4837_%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9%EC%9D%98%20%ED%95%A9.md)(#어렵#비트연산)

  - 이론(비트)

  - 부분집합 만들기

  - 부분집합 합하기
- [4839 이진탐색](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4839_binarysearch.md)
- [4843_특별한정렬](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4839_binarysearch.md)
- [4861 회문](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4861%20%ED%9A%8C%EB%AC%B8.md)(2차원배열)
- [4865 글자수](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/4865%20%EA%B8%80%EC%9E%90%EC%88%98.md)

### 백준
- [BJ2935_noise](https://github.com/squirrelabbit/TIL/blob/master/algorithm/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8B%A4%EC%A0%84%EB%AC%B8%EC%A0%9C/BJ2935_noise.md)



## Kaggle code 공부

## 1. 코로나 바이러스

- Omicron vs Delta

- omicron daily analysis(EDA)

- Omicron 3rd wave

- visualizing-covid-trends-with-animations

  

------



# 개인 프로젝트

 1. 워크넷 웹크롤링
 2. 네이버 지도 크롤링/ 최소거리찾기
 3. 영화 평점 예측(머신러닝)
 4. 아이허브 추천알고리즘
 5. 강서구 공모전
