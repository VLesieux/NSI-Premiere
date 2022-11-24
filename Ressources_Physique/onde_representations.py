import matplotlib.pyplot as plt
import numpy as np

###################################Caractéristiques de l'onde
T=5#période de l'onde
A=10#amplitude de l'onde
v=8#célérité de l'onde dans le milieu
φ=0#phase : condition à l'origine
###################################Représentation temporelle de l'onde
t = np.arange(0.0, 20.0, 0.01)
s = A*np.sin(2*np.pi*t/T+φ)

plt.subplot(1, 2, 1)
plt.plot(t, s)

plt.title("Représentation temporelle de l'onde pour une position x donnée")
plt.xlabel("t")
plt.ylabel("s")
plt.grid()
###################################Représentation spatiale de l'onde
λ=v*T#calcul de la longueur d'onde 

x = np.arange(0.0, 20.0*v, 0.01)
s = A*np.sin(2*np.pi*x/λ+φ)

plt.subplot(1, 2, 2)
plt.plot(x, s)

plt.title("Représentation spatiale de l'onde pour une date t donnée")
plt.xlabel("x")
plt.ylabel("s")
plt.grid()
###############################################
plt.show()