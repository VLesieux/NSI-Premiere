import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

val_alg_OA=[-1.07,-0.75,-0.58,-0.4,-0.165]
val_alg_OB=[0.155,0.160,0.179,0.190,0.515]

inv_val_alg_OA=[1/i for i in val_alg_OA]
inv_val_alg_OB=[1/i for i in val_alg_OB]

plt.axis([-20, 0, 0, 20])
plt.plot(inv_val_alg_OA,inv_val_alg_OB,'+',markersize=10,color="blue")

droite=sc.linregress(inv_val_alg_OA,inv_val_alg_OB)
coefficient=droite.slope
print("coefficient directeur : ",coefficient)
oorigine=droite.intercept
print("ordonnée à l'origine : ",oorigine)

x = np.linspace(-20, 0 , 200)
y=coefficient * x + oorigine
titre="modelisation : y ="+str(coefficient)+" *x +"+str(oorigine)
plt.plot(x,y,"r,-",label=titre)

plt.xlabel("1/OA (en m) : valeurs algébriques")
plt.ylabel("1/OA' (en m) : valeurs algébriques")
plt.title("Lentille mince convergente 8 ẟ")

plt.legend(loc='upper center')



plt.show()
plt.close()