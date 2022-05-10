#LSTM

###  모델 저장[Permalink](https://076923.github.io/posts/Python-pytorch-10/?msclkid=67d3dafccfb511ecb3458090cd7f780f#모델-저장)

```
torch.save(model, f'./model.pt')
```

`모델 저장 함수(torch.save)`를 활용해 모델을 저장합니다.

`torch.save(model, path)`는 `모델(model)`의 정보를 `경로(path)`에 저장합니다.



### 모델 불러오기[Permalink](https://076923.github.io/posts/Python-pytorch-10/?msclkid=67d3dafccfb511ecb3458090cd7f780f#모델-불러오기)

```
import torch
from torch import nn


class CustomModel(nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.layer = nn.Linear(2, 1)

    def forward(self, x):
        x = self.layer(x)
        return x

device = "cuda" if torch.cuda.is_available() else "cpu"
model = torch.load("model.pt", map_location=device)
print(model)

with torch.no_grad():
    model.eval()
    inputs = torch.FloatTensor([[1 ** 2, 1], [5 **2, 5], [11**2, 11]]).to(device)
    outputs = model(inputs)
    print(outputs)
```





## **파이썬 list to array와 numpy array to list 방법**

파이썬의 리스트 자료형을 넘파이 배열로 바꾸거나

numpy array에서 list 자료형으로 바꾸는 방법에 대해서

간단히 정리해보도록 하겠습니다.

 

### **파이썬 list를 numpy array로 바꾸기 : np.array 함수**

리스트를 넘파이 어레이로 만드는 방법은 np.array 함수를 이용하면 됩니다.

 

단, 다차원 array에서는 내부 배열 간 원소 개수가 같아야 하기에,

**해당 조건이 위배되는 경우에는 내부 원소는 list 형태로 잔류**하게 됩니다.

```
import numpy as np

a = [1.5, 3.7, 4.4, 9.2]
b = [[1, 3, 5], [2, 4, 6]]
c = [[1], [2, 3], [4, 5, 6]]

np.array(a) # array([1.5, 3.7, 4.4, 9.2])

np.array(b)
'''array([[1, 3, 5],
          [2, 4, 6]])'''

np.array(c) # array([list([1]), list([2, 3]), list([4, 5, 6])], dtype=object)
```

**b는** **내부 리스트 내 원소가 3, 3개로 개수가 같아** 2차원 array로 정상 변환되었지만,

**c는** **내부 리스트 원소 개수가 1, 2, 3개로 일치하지 않아**

2차원 array로 정상 변환되지 못하고 내부 원소들이 list 형태로 남았습니다.

 

 

### **파이썬 numpy array를 list로 바꾸기 : tolist 함수**

numpy array를 반대로 list로 바꾸는 방법도 tolist 함수로 쉽게 수행이 가능합니다.

 

list 메소드도 사용이 가능하긴 하지만,

다차원 배열에서는 **내부 배열이 array 형태로 잔류**한다는 점이 다릅니다.

```
a = np.array([1.2, 3.4, 5.6, 7.8])
b = np.array([[1, 3], [5, 7]])

list(a) # [1.2, 3.4, 5.6, 7.8]
a.tolist() # [1.2, 3.4, 5.6, 7.8]

list(b) # [array([1, 3]), array([5, 7])]
b.tolist() # [[1, 3], [5, 7]]
```

1차원 배열인 a는 list 메소드로도 리스트 정상 변환이 가능했지만,

**2차원 배열인 b는 tolist 메소드**를 이용해야 다차원 리스트로 변환이 가능했습니다.