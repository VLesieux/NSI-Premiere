import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np
################### entrée de la vergence donnée par le constructeur ######################
vergence_theo=float(input("Entrez la vergence en ẟ de la lentille donnée par le constructeur : "))
#################### valeurs expérimentales : A et B sont deux points conjugués###################################
#exemples pour une lentille de 8 ẟ
#val_alg_OA=[-1.07,-0.75,-0.58,-0.4,-0.165]
#val_alg_OB=[0.155,0.160,0.179,0.190,0.515]
val_alg_OA=[]
val_alg_OB=[]
i=1
while i<=5:
    entree=input("Entrez un couple de distances algébriques OA(m) , OA'(m) : ")
    couple=entree.split(",")
    val_alg_OA.append(float(couple[0]))
    val_alg_OB.append(float(couple[1]))
    i+=1       
######################  calcul des inverses ##################################
inv_val_alg_OA=[1/element for element in val_alg_OA]
inv_val_alg_OB=[1/element for element in val_alg_OB]
########################  choix des axes et représentation   ####################################
plt.axis([-20, 0, 0, 20])
plt.plot(inv_val_alg_OA,inv_val_alg_OB,'+',markersize=10,color="blue")
plt.xlabel("1/OA (en m) : valeurs algébriques")
plt.ylabel("1/OA' (en m) : valeurs algébriques")
plt.title("Lentille mince convergente de vergence : "+str(vergence_theo)+" ẟ")
########################   modélisation linéaire et représentation  ##################################################
droite=sc.linregress(inv_val_alg_OA,inv_val_alg_OB)
coefficient=droite.slope
print("Coefficient directeur de la droite modèle : ",coefficient)
oorigine=droite.intercept
print("Ordonnée à l'origine de la droite modèle : ",oorigine)
erreur_relative=100*abs(oorigine-vergence_theo)/vergence_theo
print("Erreur relative : ",erreur_relative)
x = np.linspace(-20, 0 , 200)#200 est le nombre de points
y=coefficient * x + oorigine
titre="modélisation : y ="+str(coefficient)+" *x +"+str(oorigine)
plt.plot(x,y,"r,-",label=titre)
plt.legend(loc='upper center')
################################################################################
plt.show()
plt.close()