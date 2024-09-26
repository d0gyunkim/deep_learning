import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

def step_func(x):
    return np.array(x>0)

x = np.linspace(-5,5,100)
y_sig = sigmoid(x)
y_step = step_func(x)

# 시각화
import matplotlib.pyplot as plt
plt.plot(x,y_sig,'b-',label='sigmoid')
plt.plot(x,y_step,'b-',label='step')
plt.xlabel('x',fontsize=12)
plt.ylabel('h(x)',fontsize=12)
plt.legend()
plt.show()






