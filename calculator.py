import pickle
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

def sort_list(chaine) :
    global list_num, list_calc
    sorted_list = []
    for i in range(len(list_calc)) :
        op = list_calc[i]
        #if list_calc[i] in ["*", "/"] and list_calc[i+1] in ["+", "-"] :


def add_list_fini(list_index, num) :
    for index in list_index :
        list_num[index] = num 

def calcul(chaine) :
    global list_calc, list_num
    index_num_actu = 0
    list_index_fini = []
    calc_in_list(chaine)
    print(list_num)
    for op in list_op :
        for i in range(len(list_calc)) :
            if list_calc[i] == op :
                list_index_fini.append(i)
                list_index_fini.append(i+1)
                match list_calc[i] :
                    case '*' :
                        #list_num[i+1] = multiple(list_num[i], list_num[i+1])
                        #list_num[i] = list_num[i+1]
                        calc = multiple(list_num[i], list_num[i+1])
                        add_list_fini(list_index_fini, calc)
                        print(list_num)
                    case '/' :
                        #list_num[i+1] = div(list_num[i], list_num[i+1])
                        calc = div(list_num[i], list_num[i+1])
                        add_list_fini(list_index_fini, calc)
                        print(list_num)
                    case '+' :
                        #list_num[i+1] = add(list_num[i], list_num[i+1])
                        calc = add(list_num[i], list_num[i+1])
                        add_list_fini(list_index_fini, calc)
                        print(list_num)
                    case '-' :
                        #list_num[i+1] = sous(list_num[i], list_num[i+1])
                        calc = sous(list_num[i], list_num[i+1])
                        add_list_fini(list_index_fini, calc)
                        print(list_num)

    return list_num[-1]


#======== MAIN ==========#
chaine = input("Entrez l'opération : ")
print(calcul(chaine))
#in_list_calc(chaine)
print("\n",list_num, list_calc)

#======HISTORIQUE======#
calculs=chaine
resultats=list_num[-1]

def historique(calculs,resultats):
    
    try:
        with open("data.pkl", "rb") as f:
            historik = pickle.load(f)  
    except FileNotFoundError:
        historik = [] 
    historik.append({calculs:resultats})
    with open("data.pkl", "wb") as f:
        pickle.dump(historik, f)
    return "derniers resultats", calculs, resultats

def afficher_historique():
    with open("data.pkl", "rb") as f:
        donnees_chargees = pickle.load(f)
    return donnees_chargees

def reset_historique():
    historik=[]
    with open("data.pkl", "wb") as f:
        pickle.dump(historik,f)

print(historique(calculs,resultats))
print(afficher_historique())
print(reset_historique())
print(afficher_historique())