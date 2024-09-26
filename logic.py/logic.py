
# 다층으로 게이트를 만들면 비선형으로 만들 수 있다.
import numpy as np
import basic_logic as bl
x = np.array([0,1],int)
s = np.zeros_like(x)

for x1 in x:
    for x2 in x:
        s1 = bl.NAND([x1,x2])
        s2 = bl.OR([x1,x2])
        y = bl.AND([s1,s2])
        print(f'{x1}, {x2} -> {y}')


        