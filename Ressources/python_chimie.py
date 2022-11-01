import matplotlib.pyplot as plt

n1=float(input("Quantité de matière de diiode : "))
n2=float(input("Quantité de matière d'ion thiosulfate : "))

x=0
valeurs_x=[]
valeurs_n1=[]
valeurs_n2=[]

while (n1-x)>0 and (n2-2*x)>0:
    valeurs_n1.append(n1-x)
    valeurs_n2.append(n2-2*x)
    valeurs_x.append(x)
    x+=0.1

if round(valeurs_n1[-1],2)==0:
    print("Le réactif limitant est le diiode")
else:
    print("Le réactif limitant est l'ion thiosulfate")
    
plt.plot(valeurs_x,valeurs_n1,label='I2')
plt.plot(valeurs_x,valeurs_n2,label='S2O32-')

plt.xlabel("x")
plt.legend()
plt.grid()#représente la grille
plt.show()#montre le graphe 