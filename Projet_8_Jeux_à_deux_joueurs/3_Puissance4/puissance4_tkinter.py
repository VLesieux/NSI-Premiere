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

bouton1=Bouton(canvas1,30,40,1)
bouton1.represente()

def detec_clic(event):
    x , y = event.x, event.y
    print(x,y)
    
canvas1.bind("<Button-1>", detec_clic)

canvas2=Canvas(fenetre,width=400,height=40,bg="green")
canvas2.grid(row=2, column=0)

class Jeton(object):
    def __init__(self,canvas,x,y,couleur):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.canvas2=canvas2
    def represente(self):
        self.canvas2.create_oval(self.x-15,self.y-15,self.x+15,self.y+15,width=1,fill=self.couleur)


jeton1=Jeton(canvas2,20,20,"red")
jeton1.represente()

fenetre.mainloop()