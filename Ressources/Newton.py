conversion_doc_reel="à compléter"#rapport d'échelle permettant de passer des distances mesurées aux distances réelles
tau="à compléter"#durée entre deux étincelles donnée en s sans unité
########################################################################################################
def delta_vecteurs_sur_dt(vecteur1,vecteur2):
    """
    renvoie pour tous types de vecteurs (position ou vitesse) les coordonnées du vecteur Δ(vecteurs)/Δt grâce à l'expression vectorielle Δ(vecteurs)=vecteur2-vecteur1
    """
    return ((vecteur2[0]-vecteur1[0])/(2*tau),(vecteur2[1]-vecteur1[1])/(2*tau))
########################################################################################################
vecteurs_positions="à compléter"#liste de doublets séparés par des virgules, par exemple [(-0.007,0.062),(0.008,0.074),(0.024,0.082),(0.041,0.085),(0.06,0.085)], coordonnées en m
"""
ce sont les coordonnées cartésiennes des vecteurs positions des 5 points G3,G4,G5,G6,G7 dans le repère (O,Ox,Oy) lues sur le document
"""
########################################################################################################
vecteurs_vitesse=[]
for i in range(1,4):#i varie de 1 à 3
    """
    calcule les 3 vecteurs vitesses aux points G4, G5, G6 et les ajoute (avec la méthode append) à la liste initialement vide appelée vecteurs_vitesse
    """
    vecteurs_vitesse.append(delta_vecteurs_sur_dt(vecteurs_positions[i-1],vecteurs_positions[i+1]))
########################################################################################################    
vecteur_acceleration=delta_vecteurs_sur_dt(vecteurs_vitesse[0],vecteurs_vitesse[2])
"""
calcule le vecteur accélération au point G5 en utilisant les vecteurs vitesse v(G6) et v(G4) présents aux indices respectivement 2 et 0 dans la liste précédente
"""
norme_vecteur_acceleration=((vecteur_acceleration[0]**2+vecteur_acceleration[1]**2)**0.5)*conversion_doc_reel

print("norme de l'accélération en G5 déterminée expérimentatement : ",norme_vecteur_acceleration)
########################################################################################################
norme_vecteur_acceleration_theorique="à compléter"
########################################################################################################
print("valeur théorique de la norme del'accélération : ",norme_vecteur_acceleration_theorique)
print("erreur relative",((norme_vecteur_acceleration-norme_vecteur_acceleration_theorique)/norme_vecteur_acceleration_theorique)*100,"%")

##################################################  Représentation de la courbe  ######################################################

import matplotlib.pyplot as plt
x=[vecteurs_positions[i][0] for i in range(len(vecteurs_positions))]
y=[vecteurs_positions[i][1] for i in range(len(vecteurs_positions))]
plt.axis([0, 0.05, -0.1, 0.1 ])
plt.plot(x,y,'+',markersize=5)

#####################################################     Représentation des vecteurs vitesse    ###################################################

vecteurs_vitesse=[(0,0)]+vecteurs_vitesse+[(0,0)]#on ajoute de part et d'autre une valeur non représentée pour que les listes des coordonnées et des vitesses soient de même taille
for i in range(1,4):
    plt.quiver(x[i],y[i]-0.002*i,vecteurs_vitesse[i][0],vecteurs_vitesse[i][1],angles="xy",scale_units="xy",scale=20,color='red',width=0.003)
    
#####################################################     Représentation des points    ###################################################    
for i in range(len(x)):
    plt.text(x[i],y[i],'G'+str(i+3))        
##################################################  Représentation du vecteur accélération en G5    ######################################################      
plt.quiver(x[2],y[2]+.002,vecteur_acceleration[0],vecteur_acceleration[1],angles="xy",scale_units="xy",scale=100,color='blue',width=0.003)

plt.xlabel("x (en m)")
plt.ylabel("y (en m)")
plt.title ("Enregistrement du mouvement")

plt.show()
plt.close()

