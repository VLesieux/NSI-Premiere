import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np
#############exemples de mesures
# 101800,0
# 102600,0.08
# 103100,0.13
# 103600,0.21
# 104500,0.28
val_p=[]
val_h=[]
i=1
while i<=5:
    entree=input("Entrez un couple P(Pa), z(m): ")
    couple=entree.split(",")
    val_p.append(float(couple[0]))
    val_h.append(float(couple[1]))
    i+=1      
plt.axis([0, 0.3, 100000, 105000])
plt.plot(val_h,val_p,'+',markersize=10,color="blue")
plt.xlabel("h(m)")
plt.ylabel("P(Pa)")
plt.title("Loi de la statique des fluides")
########################   modélisation linéaire et représentation  ##################################################
droite=sc.linregress(val_h,val_p)
coefficient=droite.slope
print("Coefficient directeur de la droite modèle : ",coefficient)
oorigine=droite.intercept
print("Ordonnée à l'origine de la droite modèle : ",oorigine)
x = np.linspace(0, 0.3 , 200)#200 est le nombre de points
y=coefficient * x + oorigine
titre="modélisation : y ="+str(coefficient)+" *x +"+str(oorigine)
plt.plot(x,y,"r,-",label=titre)
plt.legend(loc='upper center')
################################################################################
plt.show()
plt.close()