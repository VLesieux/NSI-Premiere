# création de dictionnaire
# vide
d = dict() # ou = {}

# avec initialisation de valeurs
boxoffice = {'Aladdin' : 569439,                   # France, semaine du 29/05/2019
             'Godzilla 2' : 342574,
             'Rocketman' : 277017}

#accès aux valeurs
boxoffice['Aladdin']
# nombre d'enregistrements 
len(boxoffice) == 3
# test appartenance d'une clef
'Rocketman' in boxoffice
# ajout d'une valeur
boxoffice['Avengers'] = 0
len(boxoffice) == 4
boxoffice['Avengers']
# les clefs sont uniques...
boxoffice['Avengers'] = 132260
len(boxoffice) == 4
boxoffice['Avengers']
# ... pas les valeurs
boxoffice['Mon Film'] = 132260
len(boxoffice) == 5
# suppression d'une valeur
del boxoffice['Mon Film']
len(boxoffice) == 4
'Mon Film' in boxoffice 

# itération sur les clefs
for film in boxoffice:
    print('{} => {} spectateurs'.format(film, boxoffice[film]))

# collection des clefs
boxoffice.keys()
# colletion des valeurs
boxoffice.values()
# collection des enregistrements
boxoffice.items()

# ces collections sont des itérables
spectateurs = 0
for entrees in boxoffice.values():
    spectateurs = spectateurs + entrees
spectateurs == 1321290


# transformation en liste :
type(boxoffice.keys())
l = list(boxoffice.keys())
type(l)

# les enregistrements sont des couples (clef, valeur)
cle,valeur = list(boxoffice.items())[0]
# itération sur les enregistrements
for (film, entrees) in boxoffice.items():
    print('{} => {} spectateurs'.format(film, entrees))



# accès à une valeur inexistante => exception KeyError
#boxoffice['Mon Film']

# exemple de capture d'exception
def nombre_entrees(titre_film):
    '''
    renvoie le nombre d'entrées du film selon boxoffice, 0 si nombre non connnu
    (boxoffice considéré ici comme global)
    '''
    try:
        return boxoffice[titre_film]
    except KeyError:
        return 0

nombre_entrees('Avengers')
nombre_entrees('Mon film')




# les clefs peuvent être de différents types (mais non mutables)
arabes_vers_romains = { 1 : 'I', 10 : 'X', 100 : 'C' }
arabes_vers_romains[10]

grille = { (0,0) : 'T', (0,1) : 'S', (1,0) : ' ', (1,1) : 'T' }
grille[(0,0)] == 'T'


# les valeurs aussi bien sûr
thon = { 'espece' : 'T', 'gestation' : 3 }
requin = { 'espece' : 'S', 'gestation' : 2, 'energie' : 2 }
mer = { (0,0) : thon, (0,1) : None, (1,0) : None, (1,1) : requin }
mer[(0,0)]['espece'] == 'T'

# y compris des fonctions (lambda-expression)
def add(x,y):
    return x+y
operateurs = {'+' : add,                     # lambda x,y : x + y ,
              '-' : lambda x,y : x - y ,
              '*' : lambda x,y : x * y ,
              '/' : lambda x,y : x // y}


def eval(expression):
    '''
    @param {string} expression est une expression arithmétique binaire de la forme "entier1 operateur entier2"
    @return {number} la valeur de l'évaluation de l'expression arithmétique fournie
    '''
    op1, op, op2 = expression.split(' ')
    operateur = operateurs[op]
    return operateur(int(op1), int(op2))


eval('3 * 4') == 12
#eval('3 / 0')
#eval('3 x 4')




import math
# exemple capture d'exception (2)
def eval2(expression):
    '''
    @param {string} expression est une expression arithmétique binaire de la forme "entier1 operateur entier2"
    @return {number} la valeur de l'évaluation de l'expression arithmétique fournie, +/-inf en cas de division par zéro
    '''
    try: 
        op1, op, op2 = expression.split(' ')
        operateur = operateurs[op]
        return operateur(int(op1), int(op2))
    except ZeroDivisionError :        
        return math.copysign(math.inf, int(op1))
    
eval2('3 * 4') == 12
eval2('3 / 0') == math.inf
#eval2('3 x 4')





# création de classe d'exception
class ExpressionInvalidError(Exception):
    def __init__(self, message):
        self.message = message

def eval3(expression):
    '''
    @param {string} expression est une expression arithmétique binaire de la forme "entier1 operateur entier2"
    @return {number} la valeur de l'évaluation de l'expression arithmétique fournie, +/-inf en cas de division par zéro
    @exception {ExceptionInvalidError} si l'expression est mal formée
    '''
    try: 
        op1, op, op2 = expression.split(' ')
        operateur = operateurs[op]
        return operateur(int(op1), int(op2))
    except ZeroDivisionError :
        return math.copysign(math.inf, int(op1))
        #raise ExpressionInvalidError('{} : division par zéro'.format(expression))
    except (KeyError, ValueError):
        raise ExpressionInvalidError('{} mal formée'.format(expression))


eval3('3 * 4') == 12
eval3('3 / 0') == math.inf
#eval3('3 x 4')
