
# Sujet : Comprendre et implémenter l’algorithme de Huffman

## 🎯 Objectif

Implémenter l'algorithme de Huffman, utilisé pour compresser un texte en construisant un code binaire optimal en fonction de la fréquence des lettres.

## 🗂️ Enjeu de l’algorithme

Lorsqu’on compresse des données (comme du texte, des images ou des sons), on cherche à réduire leur taille sans perdre d'information.
L'algorithme de Huffman est utilisé dans de nombreux formats de compression (ZIP, JPEG, MP3).

- Plus un caractère est fréquent, plus son code binaire doit être **court**.
- À l’inverse, les caractères rares peuvent avoir des codes plus longs.
- On construit un **arbre binaire** en fusionnant les caractères les moins fréquents petit à petit.

## 📦 Code Python

```python
import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    return heap[0]

def build_codes(node, prefix="", code_dict=None):
    if code_dict is None:
        code_dict = {}
    if node.char is not None:
        code_dict[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", code_dict)
        build_codes(node.right, prefix + "1", code_dict)
    return code_dict

def encode(text, codes):
    return ''.join(codes[char] for char in text)

def decode(encoded_text, tree):
    result = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            result.append(node.char)
            node = tree
    return ''.join(result)
```

## ✍️ Questions

1. **Compréhension du texte**
   - À quoi sert l’algorithme de Huffman ?
   - Pourquoi les caractères fréquents ont-ils des codes plus courts ?

2. **Analyse du code**
   - Que fait la fonction `build_huffman_tree` ?
   - Quel est le rôle de `heapq` ?
   - Pourquoi surcharge-t-on l’opérateur `<` dans la classe `Node` ?

3. **Expérimentation**
   - Essayez de compresser un mot comme `mississippi` avec ce code.
   - Vérifiez si le texte encodé est plus court en bits que le texte original (en supposant 8 bits par lettre).

## 🧪 Aller plus loin

- Compter le nombre de bits économisés par Huffman par rapport à l’encodage ASCII (8 bits/lettre).
- Modifier le code pour afficher l’arbre de Huffman de manière textuelle.
