## ** 맷플롯립(Matplotlib)**

맷플롯립(Matplotlib)은 데이터를 차트(chart)나 플롯(plot)으로 시각화하는 패키지입니다. 데이터 분석에서 Matplotlib은 데이터 분석 이전에 데이터 이해를 위한 시각화나, 데이터 분석 후에 결과를 시각화하기 위해서 사용됩니다. 아나콘다를 설치하지 않았다면 아래의 커맨드로 Matplotlib를 별도 설치할 수 있습니다.

```
pip install matplotlib
> ipython
...
In [1]: import matplotlib as mpl
In [2]: mpl.__version__
Out[2]: '2.2.3'
```

Matplotlib을 다 설치하였다면 Matplotlib의 주요 모듈인 pyplot를 관례상 plt라는 명칭으로 임포트해봅시다.

```
import matplotlib.pyplot as plt
```

### **1) 라인 플롯 그리기**

plot()은 라인 플롯을 그리는 기능을 수행합니다. plot()에 x축과 y축의 값을 기재하고 그림을 표시하는 show()를 통해서 시각화해봅시다. 그래프에는 title('제목')을 사용하여 제목을 지정할 수 있습니다. 여기서는 그래프에 'test'라는 제목을 넣어봅시다. 주피터 노트북에서는 show()를 사용하지 않더라도 그래프가 자동으로 렌더링 되므로 그래프가 시각화가 되지만 다른 개발 환경에서 사용할 때를 가정하여 show()를 코드에 삽입하였습니다.

```
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.show()
```

![img](https://wikidocs.net/images/page/32829/matplotlib1.PNG)

### **2) 축 레이블 삽입하기**

x축과 y축 각각에 축이름을 삽입하고 싶다면 xlabel('넣고 싶은 축이름')과 ylabel('넣고 싶은 축이름')을 사용합니다. 위의 그래프에 hours와 score라는 축이름을 각각 추가해봅시다.

```
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.xlabel('hours')
plt.ylabel('score')
plt.show()
```

![img](https://wikidocs.net/images/page/32829/matplotlib2.PNG)

### **3) 라인 추가와 범례 삽입하기**

다수의 plot()을 하나의 그래프에 나타낼 수 있습니다. 여러개의 라인 플롯을 동시에 사용할 경우에는 각 선이 어떤 데이터를 나타내는지를 보여주기 위해 범례(legend)를 사용할 수 있습니다.

```
plt.title('students')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) # 라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student']) # 범례 삽입
plt.show()
```

![img](https://wikidocs.net/images/page/32829/matplotlib3.PNG)

좀 더 다양한 형태의 그래프를 그리는 실습은 딥 러닝 챕터의 인공 신경망 훑어보기 실습에서 확인할 수 있습니다.