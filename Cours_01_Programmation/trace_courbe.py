# import math
# import matplotlib.pyplot as plt
# T=5730
# constante=math.log(2)/T
# end=T*math.log(50)/math.log(2)
# N0=50
# def trace(a,b,n):
#     N=N0
#     x=[a+k*(b-a)/n for k in range(n)]
#     y=[]
#     for k in range(n):
#         N=N-constante*N*(b-a)/n 
#         y.append(N)
#     plt.plot(x,y)#représente y en fonction de x
#     plt.grid()
#     plt.show()
#  
# trace(0,end,100)

# import math
# import matplotlib.pyplot as plt
# 
# # Paramètres
# T = 5730  # Période de demi-vie du carbone 14 en années
# constante = math.log(2) / T  # Constante de décroissance radioactive
# N0 = 50  # Quantité initiale de carbone 14
# end = T * math.log(50) / math.log(2)  # Calcul du temps final approximatif
# 
# # Fonction pour tracer la décroissance radioactive
# def trace(a, b, n):
#     x = [a + k * (b - a) / n for k in range(n)]  # Temps
#     y = [N0 * math.exp(-constante * t) for t in x]  # Quantité restante à chaque instant t
#     
#     # Tracé du graphe
#     plt.plot(x, y)
#     plt.grid()
#     plt.xlabel("Temps (années)")
#     plt.ylabel("Quantité de carbone 14")
#     plt.title("Décroissance radioactive du carbone 14")
#     plt.show()
# 
# # Tracé de la décroissance entre 0 et 'end' avec 100 points
# trace(0, end, 100)


import math
import matplotlib.pyplot as plt

# Paramètres
T = 5730  # Période de demi-vie du carbone 14 en années
constante = math.log(2) / T  # Constante de décroissance radioactive
N0 = 50  # Quantité initiale de carbone 14
end = T * math.log(50) / math.log(2)  # Calcul du temps final approximatif

# Fonction pour tracer la décroissance radioactive
def trace(a, b, n):
    x = [a + k * (b - a) / n for k in range(n)]  # Temps
    y = [N0 * math.exp(-constante * t) for t in x]  # Quantité restante à chaque instant t
    
    # Tracé du graphe
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    # Déplacer les axes au centre (origine)
    ax.spines['left'].set_position('zero')   # Déplacer l'axe des ordonnées à x = 0
    ax.spines['bottom'].set_position('zero') # Déplacer l'axe des abscisses à y = 0

    # Masquer les autres spines
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Ajuster les graduations des axes
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Grille et légendes
    plt.grid()
    plt.xlabel("Temps (années)")
    plt.ylabel("Quantité de carbone 14")
    plt.title("Décroissance radioactive du carbone 14")

    # Afficher le graphique
    plt.show()

# Tracé de la décroissance entre 0 et 'end' avec 100 points
trace(0, end, 100)
