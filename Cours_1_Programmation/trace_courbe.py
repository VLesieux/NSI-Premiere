import matplotlib.pyplot as plt
def f(x):
    return x**2
constante=2
N0=50
def trace(a,b,n):
    N=N0
    x=[a+k*(b-a)/n for k in range(n)]
    y=[N-constante*N*(b-a)/n for k in range(n)]
    plt.plot(x,y)#représente y en fonction de x
    plt.grid()
    plt.show()
 
trace(-5,5,100)