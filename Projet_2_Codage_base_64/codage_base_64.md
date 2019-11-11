**Objectifs :** 

* découvrir un moyen de transmission de documents binaire
* l'un de ces moyens est l'usage de la base 64
* comprendre le principe du codage en base 64
* le programmer
* utiliser les dictionnaires

**[Rappels sur les dictionnaires](dictionnaire.py)**

# Scénario de la séance

* la veille envoyer un courrier électronique à tous les participants avec une pièce jointe 
  (non textuelle), par exemple une image
* en début de séance inviter tous les participants à lire ce courrier à l'aide d'un webmail ou 
  autre logiciel de lecture de courriers
* enregistrer le courrier dans un fichier
* lire le contenu de ce fichier avec un simple éditeur de textes : **[le consulter](texte_image.txt)** ; observer que le texte est constitué de lignes de longueur identique (76 caractères par ligne) sauf éventuellement la dernière. L'enregistrer dans un dossier intitulé Codage_base_64 en le nommant texte_image.txt.
* s'apercevoir que la pièce-jointe est représentée sous forme textuelle, (le mail ne peut transporter
  que des caractères ASCII, d'ailleurs on peut remarquer l'encodage des caractères accentués
  du message)
* seuls 64 symboles apparaissent (les 26 lettres de l'alphabet latin non accentué en versions
  majuscules et minuscules, les 10 chiffres, le `+` et le `/`)
* utiliser dans un shell la commande base64 pour coder/décoder (en se plaçant d'abord dans le dossier de l'image grâce aux commandes `ls` et `ld` sous Linux) : 

Exemples   
```shell
base64 --decode texte_image.txt > image_originale.png
base64 image_originale.png > texte_image2.txt
```

Sous Windows, accéder aux commandes avec Windows R cmd, puis dir au lieu de ls et écrire certutil -decode image.txt image.png

* présenter le principe du codage en base 64 : 3 octets, donc 24 bits, consécutifs de la donnée 
  binaire à encoder
  sont découpés en 4 paquets de 6 bits, chaque paquet de 6 bits étant associé à l'un des 64 symboles (2<sup>6</sup>=64).
* la question du bourrage : que faire si la taille en octets de la donnée binaire n'est pas multiple 
  de 3 ? on complète avec un ou 2 `=`.
* on programme un codeur puis un décodeur base 64. Un module avec des opérations de lecture/écriture 
  dans un fichier binaire est fourni.
  
  
# Description du codage en base 64

Le codage Base64 permet de transformer toute donnée binaire en une suite de symboles d'un alphabet 
de 64 symboles données dans la table ci-dessous.

| Sextet (déc.) | Code | Sextet (déc.) | Code | Sextet (déc.) | Code | Sextet (déc.) | Code |
|:-------------:|:----:|:-------------:|:----:|:-------------:|:----:|:-------------:|:----:|
| `000000` (`0`)| `A`  | `000001` (`1`)| `B`  | `000010` (`2`)| `C`  | `000011` (`3`)| `D`  |
| `000100` (`4`)| `E` | `000101` (`5`)  | `F` | `000110` (`6`)  | `G` | `000111` (`7`)  | `H` |
| `001000` (`8`)  | `I` | `001001` (`9`)  | `J` | `001010` (`10`) | `K` | `001011` (`11`) | `L` |
| `001100` (`12`) | `M` | `001101` (`13`) | `N` | `001110` (`14`) | `O` | `001111` (`15`) | `P` |
| `010000` (`16`) | `Q` | `010001` (`17`) | `R` | `010010` (`18`) | `S` | `010011` (`19`) | `T` |
| `010100` (`20`) | `U` | `010101` (`21`) | `V` | `010110` (`22`) | `W` | `010111` (`23`) | `X` |
| `011000` (`24`) | `Y` | `011001` (`25`) | `Z` | `011010` (`26`) | `a` | `011011` (`27`) | `b` |
| `011100` (`28`) | `c` | `011101` (`29`) | `d` | `011110` (`30`) | `e` | `011111` (`31`) | `f` |
| `100000` (`32`) | `g` | `100001` (`33`) | `h` | `100010` (`34`) | `i` | `100011` (`35`) | `j` |
| `100100` (`36`) | `k` | `100101` (`37`) | `l` | `100110` (`38`) | `m` | `100111` (`39`) | `n` |
| `101000` (`40`) | `o` | `101001` (`41`) | `p` | `101010` (`42`) | `q` | `101011` (`43`) | `r` |
| `101100` (`44`) | `s` | `101101` (`45`) | `t` | `101110` (`46`) | `u` | `101111` (`47`) | `v` |
| `110000` (`48`) | `w` | `110001` (`49`) | `x` | `110010` (`50`) | `y` | `110011` (`51`) | `z` |
| `110100` (`52`) | `0` | `110101` (`53`) | `1` | `110110` (`54`) | `2` | `110111` (`55`) | `3` |
| `111000` (`56`) | `4` | `111001` (`57`) | `5` | `111010` (`58`) | `6` | `111011` (`59`) | `7` |
| `111100` (`60`) | `8` | `111101` (`61`) | `9` | `111110` (`62`) | `+` | `111111` (`63`) | `/` |



## Coder trois octets en quatre symboles
Trois octets correspondent à 24 bits. Chaque symbole est numéroté par un entier compris entre 0 
et 63, et donc peut-être codé sur 6 bits (sextet). 

La façon de procéder à ce codage est très simple : on découpe les 24 bits qui forment les trois
octets en quatre paquets de six bits. Chaque paquet de six bits correspond à un symbole.
Voici un exemple du codage en base 64 du triplet d'octets (18, 184, 156) :

	   18       184      156
	 00010010 10111000 10011100
	 000100 101011 100010 011100
	   E      r      i      c
Ainsi le triplet d'octets (18, 184, 156) est encodé par les quatre symboles `Eric`.

Coder un fichier binaire en base64 consiste donc à coder chaque bloc de trois octets consécutifs par ce 
procédé.

## Codage de blocs incomplets
Que faire si la taille du fichier binaire n'est pas multiple de trois octets ?    
Le dernier bloc peut ne contenir qu'un ou deux octets. Voyons les deux cas de figure.

1. **Cas d'un bloc de deux octets :** on a 16 bits de données. On rajoute 2 bits fictifs nuls : c'est le *bourrage* ou *remplissage* (*padding* en anglais). Cela permet d'avoir 18 bits soit 3 sextets codés par trois symboles. Pour le signifier, on ajoute un symbole particulier, le symbole `=` qui signale qu'il y a deux bits fictifs ajoutés. Voici un exemple avec le couple d'octets (18, 184) :

		  18       184
	    00010010 10111000
		000100 101011 1000|00
		  E      r      g
		  
	Ainsi le couple d'octets (18, 184) est encodé par les quatre symboles `Erg=`, le dernier symbole signalant qu'un bourrage de deux bits a été effectué.
	
1. **Cas d'un bloc d'un seul octet :** il manque alors deux octets, et les huit bits doivent être complétés par quatre bits fictifs nuls pour pouvoir former deux sextets codés par deux symboles. On ajoute deux symboles `=` pour signaler la présence de quatre bits fictifs. Voici un exemple avec l'octet singleton 18 :

		  18
		00010010
		000100 10|0000
		  E      g
		  
	  Ainsi l'octet 18 est encodé par les quatre symboles `Eg==`.
	  
## Exercices à faire manuellement

1. Codez la séquence d'octets (12, 133, 4, 32, 178, 200, 44, 177).
2. Décodez la chaîne de caractères `Hyk7Ag==`.
3. Quels sont les symboles possibles précédent un simple symbole `=` ? Même question pour un double.
4. Si on code une donnée constituée de `n` octets, exprimez en fonction de `n` la longueur de la chaîne de caractères obtenue en incluant les éventuels symboles `=`.

# Programmation en Python

## Entiers littéraux

* écriture usuelle décimale
* possibilité d'écrire 
  
  * en binaire (base 2) en préfixant par les littéraux par `0b`
  
    ```python
	>>> 0b10100
	20
	>>> -0b11 * 0b10100
	-60
	```

  * en octal (base 8) en préfixant par les littéraux par `0o`
  
    ```python
	>>> 0o24
	20
	>>> -0o3 * 0o24
	-60
	```
	
  * en hexadécimal (base 16) en préfixant par les littéraux par `0x`
  
    ```python
	>>> 0x14
	20
	>>> -0x3 * 0x14
	-60
	```
	

## Opérations logiques sur les entiers
Python dispose d'opérateurs logiques sur les entiers : les opérations booléennes classiques sont étendues aux bits de l'écriture binaire des entiers, avec la convention que le bit `0` correspond à la valeur booléenne `False`, et le bit `1` à `True`.

1. **Et :** 

	```python
	>>> 131 & 19
	3
	>>> 0b10000011 & 0b10011
	3
	```
	
2. **Ou :**

	```python
	>>> 131 | 19
	147
	>>> 0b10000011 | 0b10011
	147
	```


3. **Ou exclusif :**

	```python
	>>> 131 ^ 19
	144
	>>> 0b10000011 ^ 0b10011
	144
	```

En plus de ces opérations logiques, Python propose deux opérateurs de décalage

1. **Décalage à gauche (multiplication par deux):**

	```python
	>>> 131 << 1
	262
	>>> 131 << 2
	524
	```
2. **Décalage à droite (division par deux) :**

	```python
	>>> 131 >> 1
	65
	>>> 131 >> 2
	32
	```

## Base 64 programmée en Python

On se munit d'une table définissant les 64 symboles de la base 64.

```python
BASE64_SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z', '0', '1', '2', '3',
                  '4', '5', '6', '7', '8', '9', '+', '/']
```

Armé de cette table et des opérations logiques présentées ci-dessus, il est facile de programmer l'encodage d'un tuple d'octets (donnés chacun de façon décimale) en une chaîne de symboles de la base 64, ainsi que l'opération inverse de décodage.

```python
def to_base64(n_uplet):
    '''
	convertit le tuple d'octets en une chaîne de symboles
	
	:param n_uplet:  tuple : une séquence d'octets
	:return: str : la chaîne de symboles de la base 64 représentant le tuple d'octets
	:CU: les entiers du tuple tous compris entre 0 et 255
	:Exemples:
	>>> to_base64((18, 184, 156))
	'Eric'
	>>> to_base64((18, 184))
	'Erg='
	>>> to_base64((18,))
	'Eg=='
	'''
```


```python
def from_base64(b64_string):
    '''
	convertit une chaîne de symboles en un tuple d'octets
	
	:param : b64_string: (str) une chaîne de symboles de la base 64
	:return: (tuple) un tuple d'octets dont b64_string est la représentation en base 64
	:CU: les caractères de b64_string sont dans la table ou le symbole =
	:Exemple:
	
	>>> from_base64('Eric')
	(18, 184, 156)
	>>> from_base64('Erg=')
	(18, 184)
	>>> from_base64('Eg==')
	(18,)
	'''
```

Code pour la vérification des docstring
```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

1. Réalisez la fonction _to_base64(n_uplet)_ dont la docstring est donnée plus haut

Indications :

 
a) Créer une fonction _conversion_binaire_decimal(mot_binaire)_ qui retourne la valeur décimale d'un mot binaire.     

Exemple:
```python
>>> conversion_binaire_decimal("00101")
5
``` 

Remarque: Il peut être utile de renverser une chaîne de caractère.  
Pour cela on peut utiliser l'écriture [::-1].

```python
>>> chaine="exemple"
>>> chaine[::-1]
'elpmexe'
``` 

b) Créer une fonction _conversion_decimal_binaire_6bits(dec)_ qui retourne un mot binaire écrit sur 6 bits à partir de la valeur décimale de celui-ci. Il faut envisager d'ajouter des 0 pour aller jusque 6 bits.

Exemple: 
```python
>>> conversion_decimal_binaire_6bits(3)
'000011'
``` 

c) Créer une fonction _conversion_decimal_binaire_8bits(dec)_ qui retourne un mot binaire écrit sur 8 bits à partir de la valeur décimale de celui-ci.

Exemple: 
```python
>>> conversion_decimal_binaire_8bits(3)
'00000011'
``` 

d) Créer un dictionnaire appelé _equivalence_ qui associe aux 64 symboles leur code binaire écrit sur 6 bits. Pour gagner du temps, on pourra utiliser la liste   
lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"] 
et reprendre la fonction précédente _conversion_decimal_binaire_6bits(dec)_.
  
Exemple: 
```python
>>> equivalence['B']
'000001'
```

e) Créer la fonction _get_in_dictionary(sixtet)_ qui renvoie la clé du dictionnaire _equivalence_ à partir de la donnée du sixtet.  
Rappel: 

```for cle,val in equivalence.items():#on peut parcourir ainsi les items du dictionnaire equivalence en dissociant clé et valeur```

f) Créer une fonction _sequence_binaire(n_uplet)_ qui renvoie un mot binaire à partir d'un tuple constitué d'octets (on obtient ainsi un mot de 24 bits à partir d'un triplet de nombres).   
Utiliser la fonction précédente _conversion_decimal_binaire_8bits(dec)_.     
Exemple :      
```python
>>> sequence_binaire((105,86,66))
'011010010101011001000010'
```
g) Pour réaliser la fonction _to_base64(n_uplet)_ dont la docstring est donnée plus haut, une première méthode consiste à réaliser un découpage dans la chaîne de caractères appelée _sequence_ en utilisant le slicing d'une chaîne de caractères. Cette fonction sera appelée : _to_base64_slice(n_uplet)_    
Exemple : 
```python
>>> s="parapluie"
>>> s[4:9]
'pluie'
```
h) Proposer une autre méthode pour écrire la fonction _to_base64(n_uplet)_ en utilisant les opérateurs logiques présentés plus haut. Cette fonction sera appelée : _to_base64_binaire(n_uplet)_   

Exemple:      
Admettons que le tuple ou n_uplet soit (105,86,66) et que la sequence_binaire obtenue soit '011010010101011001000010', soit en faisant apparaître les sextets en insérant des points : '011010.010101.011001.000010'.      
On souhaite extraire ici la deuxième découpe de 6 bits en partant de la droite soit 011001.

```python
>>> 0b011010010101011001000010#on va travailler avec les valeurs décimales
6903362
>>> 0b111111
63
>>> bin(63<<6)
'0b111111000000'# cette opération permet de décaler de 6 bits vers la gauche le mot binaire 111111  de valeur décimale 63.       
>>> bin(6903362 & (63<<6))# l'opération logique ET appliquée sur la sequence_binaire permet de ne garder que les 6 bits qui nous intéressent
'0b11001000000'# il ne reste plus maintenant qu'à éliminer les six 0 de droite
>>> bin((6903362 & (63<<6))>>6)# on décale pour cela de 6 bits vers la droite
'0b11001'# on est parvenu ainsi à extraire notre découpe de 6 bits recherchée 
```

2. Réalisez la fonction _from_base64(b64_string)_ dont la docstring est donnée plus haut. On pourra envisager de créer une liste que l'on transformera en tuple pour renvoyer un tuple. On reproduira la méthode des opérateurs logiques utilisée à la question 1.h).

Exemple : 
```python
>>> liste=[3,4,5]
>>> n_uplet=tuple(liste)
>>> n_uplet
(3, 4, 5)
```

 Pour aller plus loin...

3. Réalisez la fonction `base64_encode` qui encode en base64 le contenu du fichier dont le nom est 
   passé en paramètre. Pour cela vous pourrez utiliser le module [binary_IO](binary_IO.py) qui définit
   deux classes nommées `Reader` et `Writer` dont les objets permettent de lire et écrire des données
   binaires dans des fichiers.
   
   ```python
   def  base64_encode(source):
        '''
		Encode a file in base64 and outputs the result on standard output.

		:param source: (str) the source filename
		:return: None
		:side effect: print on the standard output the base64 encoded version of the content 
                      of source file
		'''
   ```
   
   Améliorez cette fonction de sorte que la sortie ne soit constituée que de lignes de longueur 76
   sauf éventuellement la dernière.


4. Utilisez votre script pour coder/décoder les fichiers de votre choix.
