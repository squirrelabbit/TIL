# 상관관계

```python
df.corr()
```

![image-20220222115135480](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220222115135480.png)

```python
# 데이터 간의 상관관계를 그래프로 표현해 봅니다.

colormap = plt.cm.gist_heat   #그래프의 색상 구성을 정합니다.
plt.figure(figsize=(12,12))   #그래프의 크기를 정합니다.

# 그래프의 속성을 결정합니다. vmax의 값을 0.5로 지정해 0.5에 가까울 수록 밝은 색으로 표시되게 합니다.
sns.heatmap(df.corr(),linewidths=0.1,vmax=0.5, cmap=colormap, linecolor='white', annot=True)
plt.show()
```

![image-20220222115022640](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220222115022640.png)


```
grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma',  bins=10)
plt.show()
```

![image-20220222114919963](C:\Users\eunwon\AppData\Roaming\Typora\typora-user-images\image-20220222114919963.png)

