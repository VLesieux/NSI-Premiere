from tkinter import*

fenetre=Tk()
canvas1=Canvas(fenetre,width=400,height=40)
canvas1.grid(row=1, column=0)

class Bouton(object):
    def __init__(self,canvas,x,y,number):
        self.x=x
        self.y=y
        self.number=number
        self.canvas1=canvas1    
    def represente(self):
        self.canvas1.create_rectangle(self.x-20, self.y-20,self.x,self.y)
        self.canvas1.create_text(self.x-10, self.y-10,text=self.number)

boutons=[(i,(40*i+50,40)) for i in range(1,8)]

Boutons=[]

for i in range(len(boutons)):
    Boutons.append(Bouton(canvas1,boutons[i][1][0],boutons[i][1][1],i+1))
    Boutons[i].represente()
    
limites=[(i,(40*i+30,40*i+50)) for i in range(1,8)]


def detec_clic(event):
    global choix_colonne
    x , y = event.x, event.y
    if y>=20 and y<=40:
        for valeurs in range(len(limites)):
            if x>=limites[valeurs][1][0] and x<=limites[valeurs][1][1]:                
                print(limites[valeurs][0])

    
canvas1.bind("<Button-1>", detec_clic)

canvas2=Canvas(fenetre,width=400,height=500,bg="green")
canvas2.grid(row=2, column=0)

class Jeton(object):
    def __init__(self,canvas,x,y,couleur):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.canvas2=canvas2
    def represente(self):
        self.canvas2.create_oval(self.x-15,self.y-15,self.x+15,self.y+15,width=1,fill=self.couleur)


Jetons=[]


def afficher_config(config):
    for ligne in range(6):
        for colonne in range(7):
            if config[ligne][colonne]==0:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"white"))
            elif config[ligne][colonne]==1:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"red"))
            else:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"blue"))                
    for i in range(len(Jetons)):
        Jetons[i].represente() 
    
config = [[0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 1, 1]]
afficher_config(config)

fenetre.mainloop()