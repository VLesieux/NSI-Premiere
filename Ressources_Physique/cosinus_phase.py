import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Effet de la Phase sur cos(x)")

# Création de la figure Matplotlib
fig, ax = plt.subplots(figsize=(5, 4))
x = np.linspace(0, 2*np.pi, 500)

# Tracé de cos(x) en bleu (référence)
ax.plot(x, np.cos(x), 'b', linestyle="dashed", label=r"$\cos(x)$ (référence)")

# Tracé de cos(x + phase) en rouge
phase = 0  # Phase initiale
line, = ax.plot(x, np.cos(x + phase), 'r', label=r"$\cos(x + \phi)$")

# Configuration du graphique
ax.legend()
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("Amplitude")
ax.set_title("Comparaison de cos(x) et cos(x + φ)")
ax.grid()

# Fonction de mise à jour du tracé
def update(val):
    phase = slider.get()  # Récupérer la valeur du slider
    line.set_ydata(np.cos(x + phase))  # Mettre à jour la courbe rouge
    fig.canvas.draw_idle()  # Rafraîchir le tracé

# Intégration de Matplotlib dans Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Création du slider pour contrôler la phase
slider = tk.Scale(root, from_=0, to=2*np.pi, resolution=0.01,
                  orient="horizontal", length=400,
                  label="Phase φ (radians)", command=lambda v: update(float(v)))
slider.pack()

# Lancement de l'application
root.mainloop()
