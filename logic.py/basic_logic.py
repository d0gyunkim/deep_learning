import numpy as np


# AND 논리회로
def AND(x):
    w = np.array([1,1],int)
    b = 1.1
    y = np.dot(x,w)-b
    if y > 0:
        return 1
    else:
        return 0

# OR 논리회로
def OR(x):
    w = np.array([1,1],int)
    b = 0.5
    y = np.dot(x,w)-b
    if y > 0:
        return 1
    else:
        return 0

# NAND 논리회로
def NAND(x):
    w = np.array([-1,-1],int)
    b = -1.1
    y = np.dot(x,w)-b
    if y > 0:
        return 1
    else:
        return 0
