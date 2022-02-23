# 자연어 처리 (NLP)

자연어 처리(NLP, Natural Language Processing) - 음성이나 텍스트를 컴퓨터가 인식하고 처리하는 것

딥러닝이 등장하면서 자연어처리 연구가 활발해짐 (대용량 데이터를 학습할 수 있는 딥러닝의 속성 때문

컴퓨터는 수치 데이터만 이해할 수 있기 때문에, 자연어처리는 **텍스트 전처리 과정**이 필수

## 텍스트의 토큰화

텍스트(문장)를 잘게 나누는 것

토큰(token) : 텍스트(문장)를 단어별, 문장별, 형태소별로 나눌 수 있는데, 나누어져서 의미가 있는 단위

토큰화(tokenization) : 입력된 텍스트를 잘게 나누는 과정

### text_to_word_sequence() 

```python
import numpy as np
import tensorflow as tf
from numpy import array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten, Embedding

# 케라스의 텍스트 전처리와 관련한 함수중 text_to_word_sequence 함수를 불러 옵니다.
from tensorflow.keras.preprocessing.text import text_to_word_sequence
 
# 전처리할 텍스트를 정합니다.
text = '해보지 않으면 해낼 수 없다'

# 해당 텍스트를 토큰화 합니다.
result = text_to_word_sequence(text)

```

### 1. bag of words (토큰 전처리): 단어 빈도 확인 (tokenizer)

 **Tokenizer()**

같은 단어끼리 따로 따로 가방에 담은 뒤 각 가방에 몇 개의 단어가 들어있는지를 세는 기법

```
# 세 개의 문장을 정의합니다.
docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 합니다.',
       '텍스트의 단어로 토큰화 해야 딥러닝에서 토큰화 인식됩니다.',
       '토큰화 한 결과는 딥러닝에서 사용 할 수 있습니다.',
       ]

# 토큰화 함수를 이용해 전처리 하는 과정
from tensorflow.keras.preprocessing.text import Tokenizer

token = Tokenizer()             # 토큰화 함수 지정
token.fit_on_texts(docs)        # 토큰화 함수에 문장 적용

# 각 단어 빈도수 : .word_counts
print("\n단어 카운트:\n", token.word_counts) 
# Tokenizer()의 word_counts 함수는 순서를 기억하는 OrderedDict클래스를 사용합니다.

# 총 문장 수 : .document_count
print("\n문장 카운트: ", token.document_count)

# 각 단어가 몇개의 문장에 포함되어 있는가 : .word_docs
# 출력되는 순서는 랜덤
print("\n각 단어가 몇개의 문장에 포함되어 있는가:\n", token.word_docs)

# 각 단어에 매겨진 인덱스 값 : .word_index
print("\n각 단어에 매겨진 인덱스 값:\n",  token.word_index)

```



### 2. 단어의 원핫인코딩:중요 단어 파악 (to_categorical)

단어가 문장의 다른 요소와 어떤 관계를 가지고 있는지를 알아보는 방법

![image-20220223172321944](자연어 처리 (NLP).assets/image-20220223172321944.png)

![image-20220223173153282](자연어 처리 (NLP).assets/image-20220223173153282.png)

원-핫 인코딩을 그대로 사용하면 벡터의 길이가 너무 길어진다는 단점

공간적 낭비를 해결하기 위해 등장한 것이 단어 임베딩(word embedding)

주어진 배열을 정해진 길이로 압축

## 단어 임베딩(embedding()함수)

워드 임베딩으로 얻은 결과는 밀집된 정보를 가지고 있음

워드 임베딩을 이용해서 각 단어 간의 유사도를 계산

단어 간 유사도 계산은 오차 역전파를 이용 적절한 크기로 배열을 바꾸어 주기 위해 최적의 유사도를 계산

- Embedding( ) 함수는 최소 2개의 매개변수를 필요로 하는데, 바로 ‘입력’과 ‘출력’의 크기 

- Embedding(16, 4) : 입력될 총 단어 수는 16, 임베딩 후 출력되는 벡터 크기는 4

- Embedding(16, 4, input_length=2) : 총 입력되는 단어 수는 16개, 임베딩 후 출력되는 벡터 크기는 4, 단어를 매번 2개씩 집어 넣겠다는 뜻

### 패딩(padding): pad_sequnce( ) 

   문장의 단어 수를 똑같이 맞춰 주는 작업

  ** 문장최대길이로 맞춰줌

![image-20220223173655699](자연어 처리 (NLP).assets/image-20220223173655699.png)

  ![image-20220223174444427](자연어 처리 (NLP).assets/image-20220223174444427.png)

## 텍스트 감성분석

```python
# 임베딩에 입력될 단어의 수를 지정합니다.(패딩 0까지 단어로 포함하기 위해 1을 더한다.)
word_size = len(token_test.word_index) + 1
word_size
```

```python
# 단어 임베딩을 포함하여 딥러닝 모델을 만들고 결과를 출력합니다.
model = Sequential()

# (임베딩 층) 입력 벡터 크기: 단어 인덱스 수(26), 출력 벡터 크기: 10(수정 가능), 텍스트 패딩 결과인 4개씩 단어 입력
model.add(Embedding(26, 10, input_length=4))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))  # 이진 분류(긍정/부정)

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

```python
# 모델 학습 : 데이터로 패딩된 피처(padded_x)와 클래스를 넣어준다.
model.fit(padded_x, classes, epochs=20)
```

