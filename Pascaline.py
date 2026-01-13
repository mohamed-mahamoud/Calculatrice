import re

val_symbole={'+':3, '-':3, '*':2, '/':2, '^':2, '(': '1', ')':'1'}


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
        tokens = [t for t in re.split(r'(\+|\-|\*|\/|\(|\)|\^)', calcule) if t and t.strip()]
        
        # Shunting-yard pour obtenir ordre d'exécution (RPN)
        pile = []
        sortie = []
        prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
        
        for t in tokens:
            if t in prec:
                while pile and pile[-1] in prec and prec[pile[-1]] >= prec[t]:
                    sortie.append(pile.pop())
                pile.append(t)
            elif t == '(':
                pile.append(t)
            elif t == ')':
                while pile and pile[-1] != '(':
                    sortie.append(pile.pop())
                if pile:
                    pile.pop()
            else:
                sortie.append(float(t))
        
        while pile:
            sortie.append(pile.pop())
        
        # Extraire nombres et opérateurs dans l'ordre de la RPN
        n = [x for x in sortie if isinstance(x, float)]
        op = [x for x in sortie if isinstance(x, str)]
        
        return (n,op)            
                    
calcul=input_calcul()
print(calcul)      
                   
        
          