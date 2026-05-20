###########Exemple de fonction récursive

def factorielle(n):
    if n==1:#point d'arrêt
        return 1
    else:
        return n*factorielle(n-1)
