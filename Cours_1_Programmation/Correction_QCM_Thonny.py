#Question 1

#n = 6
#s = 0
#while n >= 0:
#    s = s + n
#    n = n -1

#Question 2

#from random import randint
#
#print((randint(0,4) - 2) * 2)

#Question 3

#def f(x,y):
#    x = x + y
#    y = x - y
#    x = x - y
#    return (x,y)
#
#print(f(2019,2020))

#Question 4

#def mystere(T):
#    s = 0
#    for k in T:
#        if k % 2 == 0:
#            s = s+k
#    return s
#
#print(mystere([2,13,5,6]))

#Question 5

#def calcul(a,b):
#    a = a + 2
#    b = b + 5
#    c = a + b
#    return c
#
#a,b = 3,5
#calcul(a,b)
#print(calcul(a,b))

#Question 6
#
#def ranger(a, b, c):
#    if a > b :
#        a, b = b, a
#    if b > c:
#        b, c = c, b
#    return a, b, c

#print(ranger(1,2,3))
#print(ranger(3,4,1))
#print(ranger(1,3,2))
#print(ranger(4,2,3))


#Question 7

#if x < 4:
#    x = x + 3
#else:
#    x = x - 3
    
#Question 8  
#def comparaison(a,b):
#    if a < b:
#        return a
#    else:
#        return b
#print(comparaison(3,7))

#Question 9
#def ajoute(n,p):
#    somme = 0
#    for i in range(n,p+1):
#        somme = somme + i
#    return somme
#
#print(ajoute(2,4))

#Question 10
#L=[2,8,19,1,3]
#m = L[0]
#for j in range(len(L)):
#    if m < L[j]:
#        m = L[j]
#print(m)