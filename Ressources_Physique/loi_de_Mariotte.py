import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np
val_p=[]
val_V=[]
##################exemple de valeurs
# 1110,60
# 1315,50
# 1625,40
# 1833,35
# 1445,45
i=1
while i<=5:
    entree=input("Entrez un couple P(hPa), V(cm3): ")
    couple=entree.split(",")
    val_p.append(float(couple[0]))
    val_V.append(float(couple[1]))
    i+=1
val_inverse_V=[1/element for element in val_V]
plt.axis([0, 0.2, 0, 2000])
plt.plot(val_inverse_V,val_p,'+',markersize=10,color="blue")
plt.xlabel("1/V(cm3)")
plt.ylabel("P(hPa)")
plt.title("Loi de Mariotte")
########################   modélisation linéaire et représentation  ##################################################
droite=sc.linregress(val_inverse_V,val_p)
coefficient=droite.slope
print("Coefficient directeur de la droite modèle : ",coefficient)
oorigine=droite.intercept
print("Ordonnée à l'origine de la droite modèle : ",oorigine)
x = np.linspace(0, 0.03 , 200)#200 est le nombre de points
y=coefficient * x
#titre="modélisation : y ="+str(coefficient)+" *x +"+str(oorigine)
#plt.plot(x,y,"r,-",label=titre)
plt.plot(x,y,"r,-")
#plt.legend(loc='upper center')
################################################################################
plt.show()
plt.close()