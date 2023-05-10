import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np
#################### valeurs expérimentales : A et B sont deux points conjugués###################################
val_alg_OA=[-1.07,-0.75,-0.58,-0.4,-0.165]
val_alg_OB=[0.155,0.160,0.179,0.190,0.515]
######################  calcul des inverses ##################################
inv_val_alg_OA=[1/element for element in val_alg_OA]
inv_val_alg_OB=[1/element for element in val_alg_OB]
########################  choix des axes et représentation   ####################################
plt.axis([-20, 0, 0, 20])
plt.plot(inv_val_alg_OA,inv_val_alg_OB,'+',markersize=10,color="blue")
plt.xlabel("1/OA (en m) : valeurs algébriques")
plt.ylabel("1/OA' (en m) : valeurs algébriques")
plt.title("Lentille mince convergente de vergence : 8 ẟ")
########################   modélisation linéaire et représentation  ##################################################
droite=sc.linregress(inv_val_alg_OA,inv_val_alg_OB)
coefficient=droite.slope
print("coefficient directeur : ",coefficient)
oorigine=droite.intercept
print("ordonnée à l'origine : ",oorigine)
x = np.linspace(-20, 0 , 200)#200 est le nombre de points
y=coefficient * x + oorigine
titre="modélisation : y ="+str(coefficient)+" *x +"+str(oorigine)
plt.plot(x,y,"r,-",label=titre)
plt.legend(loc='upper center')
################################################################################
plt.show()
plt.close()