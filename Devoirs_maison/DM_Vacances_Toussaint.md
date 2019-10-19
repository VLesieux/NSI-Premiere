# DM n°1 Vacances de Toussaint

Pour faire ce DM, on trouvera ici l'algorithme de conversion en base 2 que l'on pourra éventuellement adapter à une autre base : [Algorithme de conversion](https://github.com/VLesieux/NSI/blob/master/Projet_1_Conversions_Bases/Conversions_Thonny.md)


## Exercice 1 : codage d'un entier relatif en binaire sur _p_ bits

Écrire une fonction _conversion_relatif(a,p)_ accompagnée de sa docstring qui prend en paramètres un entier relatif _a_ exprimé en base dix et un entier naturel non nul p et renvoie le codage de l'entier relatif _a_ sur _p_ bits. Le résultat renvoyé est de type str.     

Exemples:    

conversion_relatif(18,6)='010010'         
conversion_relatif(-18,6)='101110'         
conversion_relatif(-17,5)='entier négatif trop faible'      
conversion_relatif(16,5)='entier positif trop grand'

Indications :
- Commencer par réaliser la fonction de conversion pour les entiers naturels puis adapter cette fonction pour qu'elle réalise également la conversion des entiers relatifs ; on rappelle qu'une méthode pour coder un entier négatif consiste à coder l'entier 2<sup>p</sup>-abs(n) ou 2<sup>p</sup>+ n    
- Ajouter ensuite au début de votre fonction les conditions pour que l'écriture sur _p_ bits de l'entier entré en paramètre soit possible en retournant "entier positif trop grand" ou "entier négatif trop faible" dans le cas contraire ; on rappelle que sur _p_ bits (voir [le cours 3](https://github.com/VLesieux/NSI/blob/master/Cours_3_Representation_des_donn%C3%A9es/Cours_representation_des_donnees.md)) ne peuvent être codés que les entiers relatifs compris entre - 2<sup>p-1</sup> (10000...0) et 2<sup>p-1</sup>-1 (01000...0).


## Exercice 2 : codage d'un flottant suivant la norme IEEE 754

Écrire une fonction _codage_ accompagnée de sa docstring qui détermine et renvoie le codage binaire d'un flottant exprimé en base dix. L'entrée en paramètre est de type float et la sortie de type str. On utilise le codage sur 64 bits de la norme IEEE 754.   
Voici les différentes étapes :
1. Le paramètre de la fonction, de typle float, représente un nombre x.
2. Le signe de x est déterminé et stocké dans une variable s='0' ou s='1' puis x est changé en |x|
3. Calcul de l'exposant et de la mantisse. Pour cela, si x≥2, effectuer des divisions successives par 2, si x<1 effectuer des multiplications successives par 2, en remplaçant à chaque fois la valeur de x par le résultat obtenu, et dans les deux cas jusqu'à obtenir un nombre x tel que 1≤x<2. L'exposant est alors, au signe près, le nombre de divisions ou de multiplications effectuées et la mantisse est le nombre x final.
4. Calcul de l'exposant décalé qui est codé en binaire sur 11 bits (utiliser l'exercice précédent). Le résultat est stocké dans une chaîne e.
5. Calcul de la mantisse tronquée x=x-1 qui doit être écrite en binaire sur 52 bits et stockée dans une chaîne m. Pour cela, multiplier x par 2 ; si x≥1, ajouter '1' à m et retrancher 1 à x, sinon ajouter '0' à m ; reproduire ce schéma 52 fois.
6. La chaîne concaténée s+e+m est renvoyée.

Par exemple, codons manuellement le réel - 0,375. On note que 0,375=1,5×2<sup>-2</sup>. On réalise donc la concaténation de '1' pour le signe, du code de -2 + 1023 = 1021 soit '011 1111 1101', la mantisse 1,5 s'écrit 1,1 en binaire et on ne garde que la partie décimale 1 et on complète avec des 0. Au final, le codage de - 0,375 est 1 011 1111 1101 1000.......0

Exemples:
```  
>>>codage(1.025)
'00111111100000110011001100110011'
>>>codage(-11.0252)
'11000001001100000110011100111000'
```  

## Exercice 3 : conversion décimal-hexadécimal

Écrire un programme de conversion décimal-hexadécimal (base 16) utilisant les notations suivantes 10 = "A"; 11 = "B" ; 12 = "C" ; 13 = "D" ; 14 = "E" ; 15 = "F".     
Le programme demande à l'utilisateur d'entrer un nombre décimal et il lui renvoie le code hexadécimal de ce nombre.

Exemple de conversion en hexadécimal : 

170<sub>10</sub>=AA<sub>16</sub>
