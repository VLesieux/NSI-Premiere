from timeit import timeit
from listes import*
import pylab

def mesure_temps(max,mon_tri):
    l=[]
    for longueur in range(1,max):
    
        temps=timeit(setup='from tris import '+mon_tri+'; from listes import cree_liste_melangee',
                    stmt=mon_tri+'(cree_liste_melangee('+str(longueur)+'))',number=100)
        l.append(temps)
    return(l)
def tracer_courbe(l1,l2,l3,l4):
    n=len(l1)
    x1=[i for i in range (n)]
    y1=l1
    y2=l2
    y3=l3
    y4=l4
    pylab.plot(x1,y1,label="selection")
    pylab.plot(x1,y2,label="insertion")
    pylab.plot(x1,y3,label="rapide")
    pylab.plot(x1,y4,label="fusion")
    NBRE_ESSAIS=100
    pylab.title('Temps du tri (pour {:d} essais)'.format(NBRE_ESSAIS))
    pylab.xlabel('taille des listes')
    pylab.ylabel('temps en secondes')
    pylab.grid()
    pylab.legend()
    pylab.show()
l1=mesure_temps(150,"tri_select")
l2=mesure_temps(150,"tri_insert")
l3=mesure_temps(150,"tri_rapide")
l4=mesure_temps(150,"tri_fusion")
tracer_courbe(l1,l2,l3,l4)

    

    