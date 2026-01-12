list_op = ["/", "*", "+", "-"]
list_calc = []

def cut_chaine(chaine) :
    for op in list_op :
        # cut à droite
        try :
            chaine = chaine.split(op)[0]
        finally :
            chaine = chaine
    return chaine


def calcul(chaine) :
    res = None
    for op in list_op :
        if op in chaine :
            a = int(chaine.split(op)[0])
            b = int(cut_chaine(chaine.split(op)[1]))
            match op :
                case '*' :
                    res = a * b # à modifier par la fonction correspondantes
                case '/' :
                    res = a / b # à modifier par la fonction correspondantes
                case '+' :
                    res = a + b # à modifier par la fonction correspondantes
                case '-' :
                    res = a - b # à modifier par la fonction correspondantes
                #opérations à rajouter
        #try :
        #    calcul(chaine.split("a")[])
    return res
    

#print(cut_chaine("1+5"))
#print(calcul("3-5"))

chaine = input("Entrez l'opération : ")
print(calcul(chaine))