nb_ope=0
nb=[]
ope=[]
operateur=["+","-","*","/","%","//","**","**2","V2","V","!"]
tab_cal=[]
cal=input("saisissez un calcul: ")
for i in range (len(cal)):
    tab_cal.append(cal[i])
for j in range(len(tab_cal)):
    if tab_cal[j] not in operateur:
        print(tab_cal[j])
        nb.append(tab_cal[j])
        
    else:
        print(*nb)
        print(tab_cal[j],"est l'operateur calcul")
        for h in range(len(operateur)):
            if tab_cal[j]==operateur[h]:
                nb_ope+=1
                print("utilise la fontion n",h)
        nb=[]
print(*nb)