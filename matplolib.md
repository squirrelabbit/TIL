# matplolib

```python
import matplotlib.pyplot as plt
# 그래프로 나타내 봅니다.
plt.scatter(x_data, y_data, color='r')
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

# 실제값
plt.scatter(x_data, y_data, color='r')
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

# 모델로 예측한 예측값
x_range = (np.arange(0, 15, 0.1)) # 그래프로 나타낼 x값의 범위를 정합니다.
plt.plot(np.arange(0, 15, 0.1), np.array([sigmoid(a*x + b) for x in x_range]))
plt.show()

```

