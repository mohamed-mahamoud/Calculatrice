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
        calculeN=re.split(r'(\+|\-|\*|\/|\(|\)|\^)', calcule)
        n1=n2=r1=None
        op=[]
        n=[]
        for i in calculeN:
            if i in symboles:
                op.append(i)
            else:
                n.append(float(i))
        for i in range(len(op)):
            for j in range(len(op)):
                if val_symbole[op[i]]<val_symbole[op[j]]:
                    op[i],op[j]=op[j],op[i]
                    n[j],n[i+1]=n[i+1],n[j]
        return (n,op)            
                    
calcul=input_calcul()
print(calcul)      
                   
        
          