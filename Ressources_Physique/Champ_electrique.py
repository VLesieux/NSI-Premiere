import matplotlib.pyplot as plt#importation d'une bibliothèque pour les tracés
points=[(i*0.5,j*0.5) for i in range(-10,10) for j in range(-10,10)]
#on créé une liste points par compréhension, abscisses et ordonnées varient entre -5 et +5
x=[points[i][0] for i in range(len(points))]#on récupère une liste x des abscisses de ses points
y=[points[i][1] for i in range(len(points))]#on récupère une liste y des ordonnées de ses points

plt.axis([ -5, 5, -5, 5 ])
plt.plot(x,y,'+',markersize=5)#on affiche ces points sur un graphe

def signe(x):
    if x>0:
        return 1
    else:
        return -1

def calcul_norme_champ(a,b,c,d,q):#calcul la norme du champ au point (c,d) créé par la charge q placée en (a,b)
    return (abs(q)/((a-c)**2+(b-d)**2))

c=2#abscisse de la charge placée dans l'espace
d=0#ordonnée de cette charge
q=1#valeur de la charge électrique positive placée au point (2,0)

for point in points:
    if point != (c,d):
        norme=calcul_norme_champ(point[0],point[1],c,d,q)
        plt.quiver(point[0],point[1],(point[0]-c)*norme*signe(q),(point[1]-d)*norme*signe(q),angles="xy",scale_units="xy",scale=1,color='blue',width=0.003)
# le vecteur champ électrique est représenté à partir du point considéré de coordonnées (point[0],point[1])
# la direction du vecteur champ électrique est colinéaire au vecteur qui joint la charge au point, ses coordonnées sont : (point[0]-c,point[1]-d)
# pour représenter le vecteur champ électrique, on multiplie ces coordonnées par norme*signe(q).
plt.xlabel("x (en m)")
plt.ylabel("y (en m)")
plt.title ("Spectre du champ créé par une charge positive placée au point (2,0)")
plt.grid()
plt.show()
plt.close()