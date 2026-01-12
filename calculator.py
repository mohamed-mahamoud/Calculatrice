def add(a,b):
    return a + b

def sous (a,b):
    return a-b

def multiple (a,b):
    return a*b

def div (a,b):
    if b==0:
        return "Erreur, il est impossible de diviser par 0"
    return a/b

def modulo (a,b):
    return a%b

def div_euclidienne(a,b):
    return a//b

def puissance(a,b):
    return a**b

def carre (a):
    return a**2

def racine_carre (a):
    return a**0.5

def racine (a,b):
    if a<0 and b%2==0:
        return "Erreur, il est impossible de calculer une racine négative"
    return a**(1/b)

def factoriel(a):
    if a==0:
        return 1
    else:
        resultat=0
        for i in range(a):
            if i==0:
                resultat+=a
            else:
                resultat*=a-i
        return resultat