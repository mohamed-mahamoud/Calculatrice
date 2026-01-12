import re

symboles = ['+', '-', '*', '/', '(', ')', '^', '.'] 
def input_calcul():
   while True:
        invalide = False
        calcule=input("Entrez le calcul à effectuer : ")
        for i in calcule:
            if i not in '0123456789+-*/()^.% ':
                print("Caractère non autorisé détecté.")
                invalide = True
                break
        if invalide:
            continue    
        n=0
        for i in calcule:
            if i in symboles:
                    globals()[f'symbole_{n}']=i
                    n+=1                    
        calculeN=re.split(r'(\+|\-|\*|\/|\(|\)|\^|\.)', calcule)
        return calculeN
        
        
                    
        
          