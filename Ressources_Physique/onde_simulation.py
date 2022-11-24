import numpy as np
import matplotlib.pyplot as plt

v=2#célérité de l'onde
f=5#fréquence de l'onde
T=1/f#calcul de la période temporelle
λ=v*T#calcul de la période spatiale ou longueur d'onde à partir de la période
dt = 0.01

x = np.linspace(0, 3, 150)


for i in range(2500):
    t = i * dt
    y = np.cos((2*np.pi/λ)*x - (2*np.pi/T)*t)
    if i == 0:
        line, = plt.plot(x, y)
    else:
        line.set_data(x, y)
    plt.pause(0.01) # pause avec duree en secondes
    plt.title("Simulation de la propagation d'une onde dans l'espace")
    plt.xlabel("x")
    plt.ylabel("s")

plt.show()

