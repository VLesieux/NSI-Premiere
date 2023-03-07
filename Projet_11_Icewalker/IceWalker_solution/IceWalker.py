class Plateau_de_jeu(object):

    def __init__(self):
        self.dimension_x=0
        self.dimension_y=0
        self.final_cell_x=0
        self.final_cell_y=0
        self.number_of_player=0
        self.cases = None
   
    def largeur_plateau(self):
        return self.dimension_x
    def hauteur_plateau(self):
        return self.dimension_y
    def construire_plateau_vide(self,largeur,hauteur):
        self.dimension_x=largeur
        self.dimension_y=hauteur
        #construction de toutes les cases du plateau
        self.cases = [ [0]*self.dimension_x for k in range(self.dimension_y)]
        for y in range(self.dimension_y):
            for x in range(self.dimension_x):
                self.cases[y][x] = case(x,y,'green')
    def placer_joueurs(self,liste_tuples):
            num=0
            for x,y in liste_tuples:
                self.cases[y][x].mettre_un_joueur(  num )
                num = num + 1
                self.number_of_player = self.number_of_player+1
    
    def placer_un_mur(self, triplet_infos):
        x,y, direction = int(triplet_infos[0]) , int(triplet_infos[1]) , triplet_infos[2]
        if direction == 'E':
            self.cases[y][x].mettre_un_mur_est()
        if direction == 'S':
            self.cases[y][x].mettre_un_mur_sud()
    
    def placer_case_finale(self, couple):
        x,y = couple
        self.cases[y][x].mettre_la_case_finale()
        
    def obtenir_coordonnees_case_finale(self):
        for y in range(self.dimension_y):
            for x in range(self.dimension_x):
                if (self.cases[y][x].contient_la_case_finale()):
                    return (x,y)

        
        
    def construire_plateau_a_partir_du_texte(self,text):
                f=open(text,"r")
                self.table=[tuple(ligne.rstrip().split(',')) for ligne in f]
                f.close()
                self.dimension_x=int(self.table[0][0])
                self.dimension_y=int(self.table[0][1])
                self.final_cell_x=int(self.table[1][0])
                self.final_cell_y=int(self.table[1][1])
                nombre_de_joueurs=int(self.table[2][0])
                #construction de toutes les cases du plateau
                self.cases = [ [0]*self.dimension_x for k in range(self.dimension_y)]
                for y in range(self.dimension_y):
                    for x in range(self.dimension_x):
                        self.cases[y][x] = case(x,y,'red')
                # Les joueurs
                L=[]
                for i in range(nombre_de_joueurs):
                    #on récupère les coordonnées des joueurs
                    x,y = int(self.table[3+i][0]) , int(self.table[3+i][1])
                    L.append( (x,y) )
                
                self.placer_joueurs(tuple(L))
                print( "nbre de joueur" + str(self.number_of_player) ) 
                #Les murs  
                for i in range(3+self.number_of_player,len(self.table)):
                    #on récupère les coordonnées et orientation des murs
                    x,y , direction = int(self.table[i][0]) , int(self.table[i][1] ),  self.table[i][2]
                    self.placer_un_mur((x,y , direction))
                #La case finale
                x = self.final_cell_x
                y = self.final_cell_y
                self.placer_case_finale((x,y))
       

    def recherche_coordonnees_joueurs(self):
            liste=[]
            for i in range(self.number_of_player):
                for y in range(self.dimension_y):
                    for x in range(self.dimension_x):
                    
                        if self.cases[y][x].numero_joueur==i and self.cases[y][x].contient_un_joueur:
                            liste.append((x,y))
            return tuple(liste)          

    def afficher_elements_plateau(self):
        for y in range(self.dimension_y):
            for x in range(self.dimension_x):
                
                if self.cases[y][x].contient_un_joueur():
                    print(x,y,"joueur")
                if self.cases[y][x].contient_un_mur_est():
                    print(x,y,"mur est")
                if self.cases[y][x].contient_un_mur_sud():
                    print(x,y,"mur sud")
                if self.cases[y][x].contient_la_case_finale():
                    print(x,y,"case finale")
    
    def __str__(self):
        #ligne du dessus
        for x in range(self.dimension_x+1):
            print('+-',end='')
        print()
        
        for y in range(self.dimension_y):
            print('|',end='')
            for x in range(self.dimension_x):
                joueur = self.cases[y][x].contient_un_joueur()
                num_joueur = str(self.cases[y][x].recuperer_numero_joueur())
                mur_est = self.cases[y][x].contient_un_mur_est()
                mur_sud = self.cases[y][x].contient_un_mur_sud()
                case_finale = self.cases[y][x].contient_la_case_finale()
                if case_finale and not joueur:
                    print(' F')
                elif case_finale and joueur:
                    print(num_joueur+'F',end='')    
                elif joueur and not mur_est:
                    print(num_joueur+' ',end='')
                elif mur_est and not joueur:
                    print(' |',end='')
                elif mur_est and joueur:
                    print(num_joueur+'|',end='')
                else:
                    print('  ',end='')
            print('|')
            
            print('|',end='')
            for x in range(self.dimension_x):
                mur_sud = self.cases[y][x].contient_un_mur_sud()
                if mur_sud:
                        print('+-',end='')
                else:
                    print('  ',end='')
            print('|')

    #ligne du dessous
        for x in range(self.dimension_x+1):
            print('+-',end='')
        print()



class case(object):
    def __init__(self,x,y,couleur):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.contient_joueur = False
        self.contient_mur_est = False
        self.contient_mur_sud = False
        self.contient_case_finale= False
        self.numero_joueur=None       
    
    def mettre_un_joueur(self,numero):
        self.contient_joueur = True
        self.numero_joueur=numero
    def enlever_un_joueur(self):
        self.contient_joueur = False
        self.numero_joueur=None
    def mettre_un_mur_est(self):
        self.contient_mur_est = True
    def mettre_un_mur_sud(self):
        self.contient_mur_sud = True
    def mettre_la_case_finale(self):
        self.contient_case_finale = True
    def contient_un_joueur(self):
        return self.contient_joueur 
    def contient_un_mur_est(self):
        return self.contient_mur_est 
    def contient_un_mur_sud(self):
        return self.contient_mur_sud
    def contient_la_case_finale(self):
        return self.contient_case_finale
    def recuperer_numero_joueur(self):
        return self.numero_joueur
    
    
    
class Partie(object):
    
    def __init__(self,plateau):
        self.historique=[]
        self.score=0
        self.nom_joueur='Vous'
        self.positions_joueurs=[]
        self.nombre_coups=0
        self.nombre_retours=0
    
    def est_dans_le_plateau(self,x,y,plateau):
            if x in range(plateau.largeur_plateau() ) and y in range(plateau.hauteur_plateau()):
                return True
            else:
                return False
    
    def rencontre_un_obstacle(self,x,y,direction,plateau):
        
        if direction == 'E':
            if not self.est_dans_le_plateau(x+1,y,plateau) :
                return True
            mur_est = plateau.cases[y][x].contient_un_mur_est()
            joueur_est = plateau.cases[y][x+1].contient_un_joueur()
            if mur_est  or joueur_est:
                return True
            else:
                return False
            
        if direction == "W":
            if not self.est_dans_le_plateau(x-1,y,plateau) :
                return True
            mur_west = plateau.cases[y][x-1].contient_un_mur_est()
            joueur_west = plateau.cases[y][x-1].contient_un_joueur()
            if mur_west  or joueur_west:
                return True
            else:
                return False
        
        if direction == 'N':
            if not self.est_dans_le_plateau(x,y-1,plateau):
                return True
            mur_nord = plateau.cases[y-1][x].contient_un_mur_sud()
            joueur_nord = plateau.cases[y-1][x].contient_un_joueur()
            if mur_nord  or joueur_nord:
                return True
            else:
                return False
        if direction == 'S':
            if not self.est_dans_le_plateau(x,y+1,plateau):
                return True
            mur_sud = plateau.cases[y][x].contient_un_mur_sud()
            joueur_sud = plateau.cases[y+1][x].contient_un_joueur()
            if mur_sud  or joueur_sud:
                return True
            else:
                return False
               
 
    def case_finale_atteinte(self,x,y,plateau): 
        return plateau.cases[y][x].contient_la_case_finale()
        
    def deplacement_joueur(self,numero,direction,plateau):
        (x0,y0)=plateau.recherche_coordonnees_joueurs()[numero]
        resultat_partie=False
        coord= {}
        coord['W'] = (x0-1,y0)
        coord['E'] = (x0+1,y0)
        coord['N'] = (x0,y0-1)
        coord['S'] = (x0,y0+1)
        (x1,y1) = coord[direction]
        if self.case_finale_atteinte(x0,y0,plateau):
#            plateau.cases[y0][x0].enlever_un_joueur()
#            plateau.cases[y1][x1].mettre_un_joueur(numero)
            resultat_partie=True
        if (numero==0):
            while self.est_dans_le_plateau(x1,y1,plateau) and not self.rencontre_un_obstacle(x0,y0,direction,plateau):
                plateau.cases[y0][x0].enlever_un_joueur()
                plateau.cases[y1][x1].mettre_un_joueur(numero)
                (x0,y0) = (x1,y1)
                coord['W'] = (x0-1,y0)
                coord['E'] = (x0+1,y0)
                coord['N'] = (x0,y0-1)
                coord['S'] = (x0,y0+1)
                (x1,y1) = coord[direction]
        else:
            
            while self.est_dans_le_plateau(x1,y1,plateau) and not self.rencontre_un_obstacle(x0,y0,direction,plateau):
                plateau.cases[y0][x0].enlever_un_joueur()
                plateau.cases[y1][x1].mettre_un_joueur(numero)
                (x0,y0) = (x1,y1)
                coord['W'] = (x0-1,y0)
                coord['E'] = (x0+1,y0)
                coord['N'] = (x0,y0-1)
                coord['S'] = (x0,y0+1)
                (x1,y1) = coord[direction]
        return resultat_partie
    
    def demande_le_nom(self):
        self.nom_joueur = input("Entrer votre prénom: ")
        
    def enregistrement_historique(self,plateau):
        self.historique.append(plateau.recherche_coordonnees_joueurs())
        
    def retire_joueurs_plateau(self,plateau):
        for y in range(plateau.dimension_y):
            for x in range(plateau.dimension_x):
                plateau.cases[y][x].enlever_un_joueur()
                    
    def jouer(self,plateau):
        self.demande_le_nom()
        plateau.__str__()
        x_joueur_principal ,  y_joueur_principal = plateau.recherche_coordonnees_joueurs()[0]
        partie_terminee=False
        while not partie_terminee:
#        self.case_finale_atteinte(x_joueur_principal,y_joueur_principal,plateau):
            entree=input(self.nom_joueur+" ,entrez votre mouvement 'num,direction','undo' ou 'q' (quit)")
            if entree !='undo' and entree !='q':
                couple = tuple(entree)               
                (numero,direction)=(int(couple[0]), couple[2] )
                partie_terminee=self.deplacement_joueur(numero,direction,plateau)
                print(partie_terminee)
                liste_de_tuple = plateau.recherche_coordonnees_joueurs()
                x_joueur_principal = liste_de_tuple[0][0]
                y_joueur_principal = liste_de_tuple[0][1]
                plateau.__str__()
                self.enregistrement_historique(plateau)
#                print(self.historique)
                self.nombre_coups+=1
            if entree=='undo' and len(self.historique)>=2:
                self.retire_joueurs_plateau(plateau)
                self.historique.pop()
                plateau.placer_joueurs(self.historique[-1])
                plateau.__str__()
#                print(self.historique)
                self.nombre_retours+=1
            if entree=='q':
                import sys
                sys.exit(1)
        print("Bravo "+self.nom_joueur+", vous avez réussi en "+str(self.nombre_coups)+" coups et "+str(self.nombre_retours)+ " retour en arrière.")
        


    def plateau_apres_coup(self,plateau,position_joueurs,coup):

        self.retire_joueurs_plateau(plateau)
        plateau.placer_joueurs(position_joueurs)
        x_joueur_principal ,  y_joueur_principal = plateau.recherche_coordonnees_joueurs()[0]
                      
        (numero,direction)=(coup[0], coup[1] )
        self.deplacement_joueur(numero,direction,plateau)
        liste_de_tuple = plateau.recherche_coordonnees_joueurs()
        
        return liste_de_tuple


    def resolution_automatique(self,plateau):
        parents={}
        liste_coups_possible=[(k,dir) for k in range(plateau.number_of_player) for dir in ['W','E','N','S']]
        (xf,yf)=plateau.obtenir_coordonnees_case_finale()
        source=plateau.recherche_coordonnees_joueurs()
        liste_candidats=[source]
        parents[source]=None
        print(liste_candidats)
        courant=plateau.recherche_coordonnees_joueurs()
        print(courant)
        n=0
        while liste_candidats!=[] and courant[0]!=(xf,yf) and n<20**8:
            n+=1
            courant=liste_candidats[0]
            liste_candidats.pop(0)
            prochains=[self.plateau_apres_coup(plateau,courant,coup) for coup in liste_coups_possible]
            for fils in prochains:
                if fils[0]==(xf,yf):
                    parents[fils]=courant
                    return True
                elif fils not in liste_candidats and fils not in parents:
                    parents[fils]=courant
                    liste_candidats.append(fils)
            print(liste_candidats)
            print()
                    
        


        
        




plateau = Plateau_de_jeu()
plateau.construire_plateau_a_partir_du_texte("datas/grid01.txt")

partie=Partie(plateau)
#print(partie.plateau_apres_coup(plateau,(0,'E')))
#partie.resolution_automatique(plateau)
partie.jouer(plateau)


#Plateau.construire_plateau_vide(5,5)
#Plateau.placer_un_mur( (2,3,'E') )
#Plateau.placer_un_mur( (4,3,'S') )
#Plateau.placer_joueurs(((3,4),(1,4),(3,2)))
#Plateau.placer_case_finale((4,4))




