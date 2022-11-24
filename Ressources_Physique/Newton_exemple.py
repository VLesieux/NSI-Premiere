conversion_doc_reel=5/4.6
########################################################################################################
def delta_vecteurs_sur_dt(vecteur1,vecteur2):
    """
    renvoie pour tous types de vecteurs (position ou vitesse) les coordonnées du vecteur Δ(vecteurs)/Δt grâce à l'expression vectorielle Δ(vecteurs)=vecteur2-vecteur1
    """
    return ((vecteur2[0]-vecteur1[0])/0.08,(vecteur2[1]-vecteur1[1])/0.08)
########################################################################################################
vecteurs_positions=[(-0.007,0.062),(0.008,0.074),(0.024,0.082),(0.041,0.085),(0.06,0.085)]
"""
ce sont les coordonnées cartésiennes des vecteurs positions des 5 points Gi-2,Gi-1,Gi,Gi+1,Gi+2 dans le repère (O,Ox,Oy) lues sur le document
"""
########################################################################################################
vecteurs_vitesse=[]
for i in range(1,4):#i varie de 1 à 3
    """
    calcule les 3 vecteurs vitesses aux points Gi-1, Gi, Gi+1 et les ajoute à la liste initialement vide des vecteurs_vitesse
    """
    vecteurs_vitesse.append(delta_vecteurs_sur_dt(vecteurs_positions[i-1],vecteurs_positions[i+1]))
########################################################################################################    
vecteur_acceleration=delta_vecteurs_sur_dt(vecteurs_vitesse[0],vecteurs_vitesse[2])
"""
calcule le vecteur accélération au point Gi en utilisant les vecteurs vitesse v(Gi+1) et v(Gi-1) donnés aux indices 2 et 0 dans la liste précédente
"""
########################################################################################################
print("coordonnées du vecteur accélérarion en Gi : ",vecteur_acceleration)
print("vecteur OA portant cette direction",(vecteur_acceleration[0]*5,vecteur_acceleration[1]*5))
"""
On peut ainsi reproduire exactement le vecteur accélération grâce à ses coordonnées à partir de Gi et vérifier le parallélisme avec la tension du ressort
"""
########################################################################################################
norme_vecteur_acceleration=((vecteur_acceleration[0]**2+vecteur_acceleration[1]**2)**0.5)*conversion_doc_reel

print("norme de l'accélération en Gi déterminée expérimentatement : ",norme_vecteur_acceleration)
########################################################################################################
norme_vecteur_acceleration_theorique=(6.73*(0.409-0.135)/0.64)

"""
La norme du vecteur accélération est donnée par a=T/m=k*(l-l0)/m
"""
########################################################################################################
print("valeur théorique de la norme del'accélération : ",norme_vecteur_acceleration_theorique)
print("erreur relative",((norme_vecteur_acceleration-norme_vecteur_acceleration_theorique)/norme_vecteur_acceleration_theorique)*100,"%")

##################################################  Représentation de la courbe et des vecteurs   ######################################################

import matplotlib.pyplot as plt
x=[vecteurs_positions[i][0] for i in range(len(vecteurs_positions))]
y=[vecteurs_positions[i][1] for i in range(len(vecteurs_positions))]
plt.axis([-0.1, 0.1, 0, 0.1 ])
plt.plot(x,y,'+',markersize=5)

#####################################################     Représentation des vecteurs vitesse    ###################################################

vecteurs_vitesse=[(0,0)]+vecteurs_vitesse+[(0,0)]#pour que les listes des coordonnées et des vitesses soient de même taille
for i in range(1,4):
    plt.quiver(x[i],y[i],vecteurs_vitesse[i][0],vecteurs_vitesse[i][1],angles="xy",scale_units="xy",scale=20,color='red',width=0.003)
    
#####################################################     Représentation des points    ###################################################    
for i in range(len(x)):
    plt.text(x[i],y[i],'G'+str(i))        
##################################################  Représentation du vecteur accélération en G2           ######################################################    
#Représentation du vecteur accélération au point G2   
plt.quiver(x[2],y[2],vecteur_acceleration[0],vecteur_acceleration[1],angles="xy",scale_units="xy",scale=100,color='blue',width=0.003)

plt.xlabel("x (en m)")
plt.ylabel("y (en m)")
plt.title ("Chronophotographie du mouvement")

plt.show()
plt.close()


