import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def step_func(x):
    return np.array(x > 0, dtype=int)

def ReLU(x):
    return np.maximum(0, x)

# 입력 범위
x = np.linspace(-5, 5, 100)

# 출력 값 계산
y_sig = sigmoid(x)
y_step = step_func(x)
y_relu = ReLU(x)

# 시각화
plt.plot(x, y_sig, 'b-', label='Sigmoid')
plt.plot(x, y_step, 'g-', label='Step')
plt.plot(x, y_relu, 'r-', label='ReLU')

plt.xlabel('x', fontsize=12)
plt.ylabel('h(x)', fontsize=12)
plt.legend()
plt.show()
