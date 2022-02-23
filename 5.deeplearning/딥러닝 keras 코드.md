# 덴스 2개(폐암수술)
```python
import tensorflow
print(tensorflow.__version__)
import keras
print(keras.__version__)
```

```python
# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

# 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 필요한 라이브러리를 불러옵니다.
import numpy as np
import tensorflow as tf

# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
np.random.seed(3) #시드숫자 확정
tf.random.set_seed(3)

# 준비된 수술 환자 데이터를 불러들입니다.
Data_set = np.loadtxt("dataset/ThoraricSurgery.csv", delimiter=",")
```

```python
# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장합니다.
X = Data_set[:, 0:17]
Y = Data_set[:, 17]
```

```python
# 딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다).
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))  # 입력층 노드 17개
                                                       # 은닉층1 노드 30개
model.add(Dense(1, activation='sigmoid'))              # 출력층 노드 1개
```

```python
# 딥러닝을 실행합니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 학습
model.fit(X, Y, epochs=100, batch_size=10) 
```



binary_crossentropy: 이진분류

optimizer = 'adam' :오차 줄이는법 거의 경사강법

# 덴스 3개(당뇨데이터)
```python
# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

# pandas 라이브러리를 불러옵니다.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 피마 인디언 당뇨병 데이터셋을 불러옵니다. 불러올 때 각 컬럼에 해당하는 이름을 지정합니다.
df = pd.read_csv('dataset/pima-indians-diabetes.csv',
               names = ["pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"])
```

```python
# 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 필요한 라이브러리를 불러옵니다.
import numpy
import tensorflow as tf

# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
numpy.random.seed(3)
tf.random.set_seed(3)

# 데이터를 불러 옵니다.
dataset = numpy.loadtxt("dataset/pima-indians-diabetes.csv", delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]

# 모델을 설정합니다.
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델을 컴파일합니다.
model.compile(loss='binary_crossentropy',
              optimizer='adam', 
              metrics=['accuracy'])
```

```python
# 모델을 실행합니다.
model.fit(X, Y, epochs=200, batch_size=10)

# 결과를 출력합니다.
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))
```

# 테스트 셋 split(음파데이터)

```python
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 데이터 로드 및 확인
df = pd.read_csv('dataset/sonar.csv', header=None)



dataset = df.values
# 피처 데이터, 타깃 데이터 분리
X = dataset[:, 0:60]
Y_obj = dataset[:, 60]

# 원핫 인코딩
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

# 학습 셋과 테스트 셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

# X_train 피처는 'float32' 타입으로 만들어줘야 학습이 가능
X_train = np.asarray(X_train).astype('float32')


# X_test 피처도 'float32' 타입으로 만들어준다.
X_test = np.asarray(X_test).astype('float32')


print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


# 모델 정의
model = Sequential()                                    
model.add(Dense(24,  input_dim=60, activation='relu'))  # 입력층 노드 수 60개(relu) / # 은닉층1 노드 수 24개(relu)
model.add(Dense(10, activation='relu'))                 # 은닉층2 노드 수 10개(relu)
model.add(Dense(1, activation='sigmoid'))               # 출력층 노드 수 1개(sigmoid로 이진 분류)

model.compile(loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

# 모델 학습
model.fit(X_train, Y_train, epochs=130, batch_size=5)

# 테스트셋에 모델 적용
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))

-> 정확도가 0.8571이 나온다. (앞 예제에서 학습셋으로 테스트 했더니 1.0 정확도(과적합)가 나왔던 것과 비교)

```

