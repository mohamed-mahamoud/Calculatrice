list_op = ["!", "%", "/", "//", "*", "-", "+", "²"] #list des opérateur rangé par ordre de priorité
list_calc = []
list_num = []
index_parenthese = None

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
    concat = ""
    if chaine[0] == "(" :
        i = 1
        for i in range(len(chaine)-1) :
            concat += chaine[i+1]
        return concat
    elif chaine[-1] == ")" :
        for i in range(len(chaine)-1) :
            concat += chaine[i]
        return concat
    return chaine

def is_perenthese() : 
    for num in list_num :
        if "(" in num or ")" in num :
            return True
        
def parenthese_string(chaine) :
    str_par = chaine
    #r_par_erased = False
    #l_par_erased = False
    #for i in range(len(chaine)) :
        # efface que les parenthese aux extrémité
        # if  (chaine[i] != '(' and l_par_erased) and (chaine[i] != ')' and r_par_erased):
        #     str_par += chaine[i]
        # elif chaine[i] == '(' and not l_par_erased :
        #     l_par_erased = True
        # elif chaine[i] == ')' and not r_par_erased :
        #     r_par_erased = True
    if '(' in chaine :
         str_par = str_par.split('(')[1]
    if ')' in chaine :
         str_par = str_par.split(')')[0]
    print(str_par)
    return str_par


def calc_in_list(chaine) :
    global list_calc, list_num
    concat = ""
    in_par = False
    list_calcul = []
    list_number = []
    for i in range(len(chaine)) :
        # Cas des parenthèses
        if chaine[i] == '(' or chaine[i] == ')' or in_par : #si entre parenthese
            in_par = True
            concat += chaine[i]
            if chaine[i] == ')' : #si fin de parenthese
                in_par = False
                list_number.append(parenthese_string(concat))
                print("concat : ", concat)
                concat = ""
        # Cas normal
        else :
            if not chaine[i] in list_op and i == len(chaine)-1 :
                concat += chaine[i]
                if concat != '' :
                    list_number.append(concat)
                concat = ""
            elif not chaine[i] in list_op :
                concat += chaine[i]
            else :
                list_calcul.append(chaine[i])
                list_number.append(concat)
                concat = ""
    return [list_number, list_calcul]


def add_list_fini(list_index, num) :
    for index in list_index :
        list_num[index] = str(num)

def calcul(chaine):
    global list_calc, list_num
    list_info = calc_in_list(chaine)
    list_number = list_info[0]
    list_calcul = list_info[1]
    print(list_number, list_calcul)
    
    for op in list_op:
        i = 0
        while i < len(list_calcul):
            # Cas des parenthèses
            if any(operator in list_number[i] for operator in list_op):
                print(f"list_i : {list_number[i]} parenthese : {calc_in_list(list_number[i])}")
                calc = calcul((list_number[i]))
                list_number[i] = str(calc)
                list_number.pop(i+1)
            # Cas normal
            elif list_calcul[i] == op:
                a = float(list_number[i])
                b = float(list_number[i+1])
                
                match list_calcul[i]:
                    case '*':
                        calc = str(multiple(a, b))
                    case '/':
                        calc = str(div(a, b))
                    case '+':
                        calc = str(add(a, b))
                    case '-':
                        calc = str(sous(a, b))
                    case '%': 
                        calc = str(modulo(a, b))
                    case '//': 
                        calc = str(div_euclidienne(a, b))
                
                # Mise à jour les listes
                list_number[i] = calc
                list_number.pop(i+1)
                list_calcul.pop(i)
                print(list_number, list_calcul)
            else:
                i += 1  
    
    return list_number[0]


#======== MAIN ==========#
chaine = input("Entrez l'opération : ")
print(calcul(chaine))
#print(parenthese_string('(1+5*8*(4+2)-6)'))
