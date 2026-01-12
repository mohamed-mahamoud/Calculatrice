list_op = ["/", "*", "+", "-", "%", "!", "²"]
list_calc = []
list_num = []

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
def cut_chaine(chaine) :
    for op in list_op :
        # cut à droite
        try :
            chaine = chaine.split(op)[0]
        finally :
            chaine = chaine
    return chaine

def calc_in_list(chaine) :
    global list_calc, list_num
    concat = ""
    for i in range(len(chaine)) :
        if not chaine[i] in list_op and i == len(chaine)-1 :
            concat += chaine[i]
            list_num.append(int(concat))
            concat = ""
        elif not chaine[i] in list_op :
            concat += chaine[i]
        else :
            list_calc.append(chaine[i])
            list_num.append(int(concat))
            concat = ""



# def calcul(chaine) :
#     res = None
#     for op in list_op : # BOUCLER SUR CHAINE ?
#         if op in chaine :
#             a = int(chaine.split(op)[0])
#             b = int(cut_chaine(chaine.split(op)[1]))
#             match op :
#                 case '*' :
#                     res = multiple(a, b) 
#                 case '/' :
#                     res = div(a, b)
#                 case '+' :
#                     res = add(a, b)
#                 case '-' :
#                     res = sous(a, b)
#                 case '²' :
#                     res = carre(a) # 2 nombre min (enlever les fct qui en demande moins)
#                 #opérations à rajouter
#         #try :
#         #    calcul(chaine.split("a")[])
#     return res

def calcul(chaine) :
    global list_calc, list_num
    calc_in_list(chaine)
    for i in range(len(list_calc)) :
        match list_calc[i] :
            case '*' :
                list_num[i+1] = multiple(list_num[i], list_num[i+1])
            case '/' :
                list_num[i+1] = div(list_num[i], list_num[i+1])
            case '+' :
                list_num[i+1] = add(list_num[i], list_num[i+1])
            case '-' :
                list_num[i+1] = sous(list_num[i], list_num[i+1])

    return list_num[-1]


#======== MAIN ==========#
chaine = input("Entrez l'opération : ")
print(calcul(chaine))
#in_list_calc(chaine)
print(list_num, list_calc)