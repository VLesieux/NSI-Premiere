import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Paramètres de l'onde
x = np.linspace(0, 4 * np.pi, 1000)
y1 = np.sin(x)  # Première onde (fixe)
initial_phase = 0
y2 = np.sin(x + initial_phase)  # Deuxième onde avec phase ajustable
y_sum = y1 + y2  # Somme des deux ondes

# Création de la figure et des axes
fig, ax = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
plt.subplots_adjust(bottom=0.25)  # Laisser de la place pour le slider

# Tracé des courbes
line1, = ax[0].plot(x, y1, label="Onde 1 (fixe)", color='b')
ax[0].legend()
line2, = ax[1].plot(x, y2, label="Onde 2 (phase ajustable)", color='r')
ax[1].legend()
line3, = ax[2].plot(x, y_sum, label="Somme des deux ondes", color='g')
ax[2].legend()

# Mise en forme des axes
for axis in ax:
    axis.set_ylim([-2, 2])
    axis.grid(True)

ax[2].set_xlabel("x")

# Ajout du slider pour contrôler la phase
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, "Phase", -np.pi, np.pi, valinit=initial_phase)

# Fonction de mise à jour lors du déplacement du slider
def update(val):
    phase = slider.val
    y2_updated = np.sin(x + phase)
    line2.set_ydata(y2_updated)
    line3.set_ydata(y1 + y2_updated)
    fig.canvas.draw_idle()

# Lier le slider à la fonction de mise à jour
slider.on_changed(update)

plt.show()
