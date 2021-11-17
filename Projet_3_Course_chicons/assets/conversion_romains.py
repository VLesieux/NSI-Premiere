valeur_romain={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

def romain_to_arabe(s):
    
    if len(s)==1:
        return valeur_romain[s]

    else:
    
        if valeur_romain[(s[-1])]>=valeur_romain[(s[-2])]:
            return romain_to_arabe(s[0:-2])+valeur_romain[(s[-1])]+valeur_romain[(s[-2])]
        else:
            return romain_to_arabe(s[0:-2])+valeur_romain[(s[-1])]-valeur_romain[(s[-2])]
    
    
romain_to_arabe('MMXIX')
