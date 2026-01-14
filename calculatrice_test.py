import re


val_symbole = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
symboles = ['+', '-', '*', '/', '(', ')', '^', '.', '%', '//', 'V', '!']

def input_calcul(calcul=None, pos=0, niveau='input'):
    # Niveau input : demander le calcul
    if niveau == 'input':
        while True:
            invalide = False
            calcul = input("Entrez le calcul à effectuer : ")
            
            i = 0
            while i < len(calcul):
                c = calcul[i]
                if c.isdigit() or c in '+-()*^.% V!':
                    i += 1
                    continue
                if c == '/':
                    if i + 1 < len(calcul) and calcul[i + 1] == '/':
                        i += 2
                        continue
                    i += 1  # single '/'
                    continue
                if c.isspace():
                    i += 1
                    continue
                print("Caractère non autorisé détecté.")
                invalide = True
                break
            if invalide:
                continue
            
            if calcul.count('(') != calcul.count(')'):
                print("Parenthèses non équilibrées.")
                continue
            
            try:
                calcul = calcul.replace(' ', '')
                arbre, _ = input_calcul(calcul, 0, 'add')
                return arbre
            except Exception as e:
                print(f"Erreur dans l'expression : {e}")
                continue
    
    # Niveau add : addition/soustraction
    elif niveau == 'add':
        g, pos = input_calcul(calcul, pos, 'mult')
        while pos < len(calcul) and calcul[pos] in '+-':
            o = calcul[pos]
            pos += 1
            d, pos = input_calcul(calcul, pos, 'mult')
            g = (o, g, d)
        return g, pos
    
    # Niveau mult : multiplication/division
    elif niveau == 'mult':
        g, pos = input_calcul(calcul, pos, 'puis')
        while pos < len(calcul):
            if calcul.startswith('//', pos):
                o = '//'
                pos += 2
            elif calcul[pos] in '*/':
                o = calcul[pos]
                pos += 1
            else:
                break
            d, pos = input_calcul(calcul, pos, 'puis')
            g = (o, g, d)
        return g, pos
    
    # Niveau postfix : factorielle (postfixe unaire)
    elif niveau == 'postfix':
        g, pos = input_calcul(calcul, pos, 'base')
        while pos < len(calcul) and calcul[pos] == '!':
            g = ('!', g)
            pos += 1
        return g, pos
    
    # Niveau puis : puissance
    elif niveau == 'puis':
        g, pos = input_calcul(calcul, pos, 'postfix')
        if pos < len(calcul) and calcul[pos] in '^V':
            o = calcul[pos]
            pos += 1
            d, pos = input_calcul(calcul, pos, 'puis')
            g = (o, g, d)
        return g, pos
    
    # Niveau base : nombres et parenthèses
    elif niveau == 'base':
        if pos < len(calcul) and calcul[pos] == '-':
            pos += 1
            v, pos = input_calcul(calcul, pos, 'base')
            return ('*', -1.0, v), pos
        if pos < len(calcul) and calcul[pos] == '+':
            pos += 1
            return input_calcul(calcul, pos, 'base')
        if pos < len(calcul) and calcul[pos] == '(':
            pos += 1
            v, pos = input_calcul(calcul, pos, 'add')
            if pos >= len(calcul) or calcul[pos] != ')':
                raise ValueError("Parenthèse fermante manquante")
            pos += 1
            return v, pos
        d = pos
        if pos < len(calcul) and (calcul[pos].isdigit() or calcul[pos] == '.'):
            while pos < len(calcul) and (calcul[pos].isdigit() or calcul[pos] == '.'):
                pos += 1
            return float(calcul[d:pos]), pos
        raise ValueError(f"Erreur position {pos}")

#====== Opérations ========#
def add(a,b):
    return a + b

def sous (a,b):
    return a-b

def multiple (a,b):
    return a*b

def div (a,b):
    if b == 0:
        print("Erreur : Division par zéro")
        calcul()
    else:
        return a/b

def modulo (a,b):
    if b == 0:
        print("Erreur : Division par zéro")
        calcul()
    else:
        return a%b

def div_euclidienne(a,b):
    if b == 0:
        print("Erreur : Division par zéro")
        calcul()
    else:
        return a//b

def puissance(a,b):
    return a**b

def carre (a):
    return a**2

def racine_carre (a):
    return a**0.5

def racine (a,b):
    return a**(1/b)

def factoriel(a):
    a = int(a)
    if a < 0:
        raise ValueError("Factorielle d'un nombre negatif")
    if a == 0 or a == 1:
        return 1
    resultat = 1
    for i in range(2, a + 1):
        resultat *= i
    return resultat

#======== Reconnaisance de calcul =========#


def calcul():
    arbre = input_calcul()
    
    def evaluer(a):
        if isinstance(a, tuple):
            if len(a) == 2:
                # Operateur unaire (postfixe)
                operateur, operande = a
                op = evaluer(operande)
                
                match operateur:
                    case '!':
                        calc = factoriel(op)
                    case _:
                        calc = op
                return calc
            else:
                # Operateur binaire
                operateur, gauche, droit = a
                g = evaluer(gauche)
                d = evaluer(droit)
                
                match operateur:
                    case '*':
                        calc = (multiple(g, d))
                    case '/':
                        calc = (div(g, d))
                    case '+':
                        calc = (add(g, d))
                    case '-':
                        calc = (sous(g, d))
                    case '%': 
                        calc = (modulo(g, d))
                    case '//': 
                        calc = (div_euclidienne(g, d))
                    case '^':
                        calc = (puissance(g, d))
                    case 'V':
                        calc = (racine(g, d))
                
                return calc
        else:
            return a
    
    resultat = evaluer(arbre)
    if isinstance(resultat, float) and resultat.is_integer():
        return int(resultat)
    return resultat
#======== MAIN ==========#

resultat = calcul()
print(resultat)
#in_list_calc(chaine)
