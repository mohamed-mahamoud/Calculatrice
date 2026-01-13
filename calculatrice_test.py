import re

val_symbole = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
symboles = ['+', '-', '*', '/', '(', ')', '^', '.']

def input_calcul(calcul=None, pos=0, niveau='input'):
    # Niveau input : demander le calcul
    if niveau == 'input':
        while True:
            invalide = False
            calcul = input("Entrez le calcul à effectuer : ")
            
            for i in calcul:
                if i not in '0123456789+-*/()^.% ':
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
                arbre = input_calcul(calcul, 0, 'add')[0]
                n, op = input_calcul(arbre, 0, 'extraire')
                return (n, op)
            except Exception as e:
                print(f"Erreur dans l'expression : {e}")
                continue
    
    # Niveau extraire : extraire n et op de l'arbre
    elif niveau == 'extraire':
        n = []
        op = []
        def ex(a):
            if isinstance(a, tuple):
                ex(a[1])
                ex(a[2])
                op.append(a[0])
            else:
                n.append(a)
        ex(calcul)
        return n, op
    
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
        while pos < len(calcul) and calcul[pos] in '*/':
            o = calcul[pos]
            pos += 1
            d, pos = input_calcul(calcul, pos, 'puis')
            g = (o, g, d)
        return g, pos
    
    # Niveau puis : puissance
    elif niveau == 'puis':
        g, pos = input_calcul(calcul, pos, 'base')
        if pos < len(calcul) and calcul[pos] == '^':
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
    return a**(1/b)

def factoriel(a):
    resultat=0
    for i in range(a):
        if i==0:
            resultat+=a
        else:
            resultat*=a-i
    return resultat

#======== Reconnaisance de calcul =========#


def calcul() :
    n, op = input_calcul()
    index_num_actu = 0
    list_index_fini = []
    print(n)
    for operateur in op :
        for i in range(len(op)) :
            if op[i] == operateur :
                list_index_fini.append(i)
                list_index_fini.append(i+1)
                match op[i] :
                    case '*' :
                        calc = multiple(n[i], n[i+1])
                        for index in list_index_fini :
                            n[index] = calc
                        print(n)
                    case '/' :
                        calc = div(n[i], n[i+1])
                        for index in list_index_fini :
                            n[index] = calc
                        print(n)
                    case '+' :
                        calc = add(n[i], n[i+1])
                        for index in list_index_fini :
                            n[index] = calc
                        print(n)
                    case '-' :
                        calc = sous(n[i], n[i+1])
                        for index in list_index_fini :
                            n[index] = calc
                        print(n)

    return n[-1]


#======== MAIN ==========#
print(calcul())
#in_list_calc(chaine)
