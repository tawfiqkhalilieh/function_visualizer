import numpy as np
import matplotlib.pyplot as plt
from functions.polynomial import f
from uuid import uuid4

def fun(a:float, b:float, c: float):
    xlist = np.linspace(-10,11,num=500)
    ylist = f(xlist,a,b,c)
    plt.figure(num=0,dpi=120)
    plt.plot(xlist,ylist)
    _ = str(uuid4())
    plt.savefig(f"plots/{_}")
    plt.close()
    return _+".png"
