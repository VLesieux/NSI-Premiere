
# Sujet : Comprendre et implémenter l’algorithme de Huffman

## 🎯 Objectif

Implémenter l'algorithme de Huffman, utilisé pour compresser un texte en construisant un code binaire optimal en fonction de la fréquence des lettres.

## 🗂️ Enjeu de l’algorithme

Lorsqu’on compresse des données (comme du texte, des images ou des sons), on cherche à réduire leur taille sans perdre d'information.
L'algorithme de Huffman est utilisé dans de nombreux formats de compression (ZIP, JPEG, MP3).

- Plus un caractère est fréquent, plus son code binaire doit être **court**.
- À l’inverse, les caractères rares peuvent avoir des codes plus longs.
- On construit un **arbre binaire** en fusionnant les caractères les moins fréquents petit à petit.


Étapes du Codage de Huffman 

1.	Calcul des Fréquences des Symboles : comptez la fréquence d'apparition de chaque symbole dans le texte à compresser. 
2.	Construction de l'Arbre de Huffman : 

Créez un nœud feuille pour chaque symbole avec sa fréquence associée.  

Ajoutez tous les nœuds dans une file de priorité (ou un tas), ordonnée par fréquence croissante  (les nœuds avec les fréquences les plus basses sont en tête).   

Répétez les étapes suivantes jusqu'à ce qu'il ne reste plus qu'un seul nœud dans la file :

 	- Retirez les deux nœuds avec les plus basses fréquences de la file.

  	- Créez un nouveau nœud interne avec ces deux nœuds comme enfants et une fréquence égale à la somme de leurs fréquences.

	- Ajoutez ce nouveau nœud dans la file. 

	- Le dernier nœud restant est la racine ou root de l'arbre de Huffman. 

3.	Génération des Codes de Huffman : 

Parcourez l'arbre de Huffman à partir de la racine pour assigner des codes binaires à chaque symbole. 

À chaque nœud interne, assignez "0" à la branche gauche et "1" à la branche droite (ou vice versa). 

Les codes binaires pour chaque symbole sont obtenus en suivant les branches de la racine aux feuilles.


4.	Exemple.

<img src="assets/arbre.jpg">


5.	Encodage des Données : 

Remplacez chaque symbole du texte par son code binaire correspondant pour obtenir la séquence compressée. 
Supposons que nous voulons compresser la chaîne "ABRACADABRA". 
Remplacez chaque symbole par son code : 
"ABRACADABRA" devient "0111101011001100011110010"

## 📦 Code Python

```python
class Noeud:
    """
    Définition d'une classe pour représenter chaque nœud de l'arbre de Huffman
    """
    def __init__(self, caractere, frequence):#initialisation des attributs de la classe à partir de deux paramètres caractere et fréquence
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = None
        self.droite = None

    def est_feuille(self):#définition d'une méthode pour les objets noeuds qui dérivent de la classe Noeud
        return self.gauche is None and self.droite is None


def creer_arbre_huffman(frequences):
    """
    Fonction pour construire l'arbre de Huffman à partir des fréquences
    """
    liste_noeuds = [Noeud(c, f) for c, f in frequences]

    while len(liste_noeuds) > 1:
        liste_noeuds.sort(key=lambda n: n.frequence)#classement par fréquence croissante 
        gauche = liste_noeuds.pop(0)# la méthode pop() des listes retire l'élément à l'indice spécifié, ici 0.
        droite = liste_noeuds.pop(0)

        nouveau_noeud = Noeud(None, gauche.frequence + droite.frequence)
        nouveau_noeud.gauche = gauche
        nouveau_noeud.droite = droite

        liste_noeuds.append(nouveau_noeud)

    return liste_noeuds[0]

def arbre_en_texte(noeud, prefixe="", est_gauche=True):
    """
    Retourne une représentation textuelle ASCII de l’arbre de Huffman.
    
    >>> n1 = Noeud('A', 1)
    >>> n2 = Noeud('B', 2)
    >>> racine = Noeud(None, 3)
    >>> racine.gauche = n1
    >>> racine.droite = n2
    >>> print(arbre_en_texte(racine))
    └── 3
        └── 1 'A'
        ├── 2 'B'
    """
    lignes = []
    if noeud is not None:
        branche = "└── " if est_gauche else "├── "
        if noeud.est_feuille():
            lignes.append(prefixe + branche + f"{noeud.frequence} '{noeud.caractere}'")
        else:
            lignes.append(prefixe + branche + f"{noeud.frequence}")
        nouveau_prefixe = prefixe + ("    " if est_gauche else "│   ")
        lignes += arbre_en_texte(noeud.gauche, nouveau_prefixe, True).splitlines()
        lignes += arbre_en_texte(noeud.droite, nouveau_prefixe, False).splitlines()
    return "\n".join(lignes)

def afficher_arbre_huffman(noeud):
    """
    Affiche l’arbre de Huffman dans la console.
    """
    print(arbre_en_texte(noeud))


def generer_codes(noeud, code_actuel="", codes={}):
    """
    Fonction pour générer les codes de Huffman à partir de l'arbre
    """
    if noeud is not None:
        if noeud.est_feuille():
            codes[noeud.caractere] = code_actuel
        else:
            generer_codes(noeud.gauche, code_actuel + "0", codes)
            generer_codes(noeud.droite, code_actuel + "1", codes)
    return codes


def encoder_message(message, codes):
    """
    Fonction pour encoder un message en utilisant les codes de Huffman
    >>> codes = {'A': '0', 'B': '10', 'C': '11'}
    >>> encoder_message('ABAC', codes)
    '010011'
    """
    message_code = ""
    for caractere in message:
        message_code += codes[caractere]
    return message_code


def decoder_message(message_code, arbre):
    """
    Fonction pour décoder un message binaire à l'aide de l'arbre de Huffman
    >>> frequences = [('A', 5), ('B', 2), ('C', 1)]
    >>> arbre = creer_arbre_huffman(frequences)
    >>> codes = generer_codes(arbre)
    >>> message = encoder_message("ABAC", codes)
    >>> decoder_message(message, arbre)
    'ABAC'
    """
    message_decode = ""
    noeud_actuel = arbre
    for bit in message_code:
        if bit == '0':
            noeud_actuel = noeud_actuel.gauche
        else:
            noeud_actuel = noeud_actuel.droite

        # Si on atteint une feuille, on ajoute le caractère et on repart de la racine
        if noeud_actuel.est_feuille():
            message_decode += noeud_actuel.caractere
            noeud_actuel = arbre
    return message_decode

_last_arbre = None

def affichage_du_code(texte):
    """
    Affiche le message codé à partir de message
    >>> sorted(set("HELLO"))
    ['E', 'H', 'L', 'O']
    >>> affichage_du_code("HELLO")
    '0100111110'
    """
    frequences = [(c, texte.count(c)) for c in sorted(set(texte))]
    global _last_arbre
    _last_arbre = creer_arbre_huffman(frequences)
    codes = generer_codes(_last_arbre)
    message_code = encoder_message(texte, codes)
    return message_code
    
def decodage_du_message(message,_last_arbre):
    """
    Affiche le texte auquel correspond le message codé
    >>> decodage_du_message('0100111110',_last_arbre)
    HELLO
    """
    texte = decoder_message(message,_last_arbre)
    print(texte)
    
def economie(texte):
    """
    Compte l'économie entre le code de Hufmann et le code ASCII (8 bits par caractère)
    >>> economie("HELLO")
    30
    """
	pass

texte = "HELLO"
message_code, arbre = affichage_du_code(texte), _last_arbre
print("Message encodé :", message_code)
print("Message décodé :", decodage_du_message(message_code, arbre))
print("\nArbre de Huffman :")
afficher_arbre_huffman(arbre)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

```


## ✍️ Questions

1. **Compréhension du texte et du code**

   	1) À quoi sert l’algorithme de Huffman ?
   	2) Pourquoi les caractères fréquents ont-ils des codes plus courts ?
	3) À quoi sert la classe Noeud ?
	4) Que retourne la méthode est_feuille ?
	5) Qu’y-a-t-il de particulier dans la fonction generer_codes ? Que fait-elle, comment fonctionne-t-elle ?
	6) Réaliser l'arbre à la main pour le mot "mississippi"
	7) Calculer le taux de compression sur cet exemple par rapport à l’encodage ASCII (8 bits/lettre), défini par :    taux = ((taille_initiale - taille_compressee) / taille_initiale) * 100.
	8) Comment le code 1101110010 peut-il être décodé en HELLO ? Représenter l'arbre correspondant.
	9) Expliquer pourquoi le code ne peut pas être équivoque ? (il ne peut être interprété que d’une seule manière).
	10) Compléter le code de la fonction économie.


2. **Aller plus loin**

Réaliser une application qui réalise la compression de Huffman sur un texte entré.

