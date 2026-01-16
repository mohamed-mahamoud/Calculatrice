import pickle
import tkinter
from tkinter import *
import os

list_num = []
expression=""
lst_button=[
    "C","(",")","//","%",   
    "7","8","9","/","q",
    "4","5","6","*","^",
    "1","2","3","-","V",
    "0",".","=","+","!",
    "<"
    ]

#====== Opérations ========#
def add(a,b) :
    return a + b

def sous (a,b) :
    return a-b

def multiple (a,b) :
    return a*b

def div (a,b):
    if b == 0 :
        raise ValueError(" Division par zéro")
    else:
        return a/b

def modulo (a,b) :
    if b == 0 :
        raise ValueError(" Division par zéro")
    else:
        print(a%b)
        return a%b

def div_euclidienne(a,b) :
    if b == 0 :
        raise ValueError(" Division par zéro")
    else:
        return a//b

def puissance(a,b) :
    return a**b

def carre (a) :
    return a**2

def racine_carre (a) :
    return a**0.5

def racine (a,b) :
    return a**(1/b)

def factoriel(a) :
    a = int(a)
    if a < 0 :
        raise ValueError(" Factorielle d'un nombre negatif")
    if a == 0 or a == 1 :
        return 1
    resultat = 1
    for i in range(2, a + 1) :
        resultat *= i
    return resultat

#======== Reconnaisance de calcul =========#

def input_calcul(calcul=None, pos=0, niveau='input') :
    # Niveau input : demander le calcul
        invalide = False
        calcul = expression     
        i = 0
        while i < len(calcul) :
            c = calcul[i]
            if c.isdigit() or c in '+-()*^.% V!q' :
                i += 1
                continue
            if c == '/' :
                if i + 1 < len(calcul) and calcul[i + 1] == '/' :
                    i += 2
                    continue
                i += 1  
                continue
            if c.isspace() :
                i += 1
                continue
            print("Caractère non autorisé détecté.")
            invalide = True
            break
        if invalide:
            raise ValueError("Caractère non autorisé détecté.")

            
        if calcul.count('(') != calcul.count(')') :
            print("Parenthèses non équilibrées.")
            raise ValueError("Parenthèses non équilibrées.")
        calcul=calcul.replace(' ','')
        return calcul
    
def orgarniser_calcul(calcul, pos=0, niveau='add') :             
    # Niveau add : addition/soustraction
    if niveau == 'add' :
        g, pos = orgarniser_calcul(calcul, pos, 'mult')
        while pos < len(calcul) and calcul[pos] in '+-' :
            o = calcul[pos]
            pos += 1
            d, pos = orgarniser_calcul(calcul, pos, 'mult')
            g = (o, g, d)
        return g, pos
    
    # Niveau mult : multiplication/division
    elif niveau == 'mult' :
        g, pos = orgarniser_calcul(calcul, pos, 'puis')
        while pos < len(calcul):
            if calcul.startswith('//', pos) :
                o = '//'
                pos += 2
            elif calcul[pos] in '*/%':
                o = calcul[pos]
                pos += 1
            else:
                break
            d, pos = orgarniser_calcul(calcul, pos, 'puis')
            g = (o, g, d)
        return g, pos
    
    # Niveau postfix : factorielle (postfixe unaire)
    elif niveau == 'postfix' :
        g, pos = orgarniser_calcul(calcul, pos, 'base')
        while pos < len(calcul) and calcul[pos] in '!q' :
            g = (calcul[pos], g)
            pos += 1
        return g, pos
    
    # Niveau puis : puissance
    elif niveau == 'puis':
        g, pos = orgarniser_calcul(calcul, pos, 'postfix')
        if pos < len(calcul) and calcul[pos] in '^V' :
            o = calcul[pos]
            pos += 1
            d, pos = orgarniser_calcul(calcul, pos, 'puis')
            g = (o, g, d)
        return g, pos
    
    # Niveau base : nombres et parenthèses
    elif niveau == 'base' :
        if pos < len(calcul) and calcul[pos] == '-' :
            pos += 1
            v, pos = orgarniser_calcul(calcul, pos, 'base')
            return ('*', -1.0, v), pos
        if pos < len(calcul) and calcul[pos] == '+' :
            pos += 1
            return orgarniser_calcul(calcul, pos, 'base')
        if pos < len(calcul) and calcul[pos] == '(' :
            pos += 1
            v, pos = orgarniser_calcul(calcul, pos, 'add')
            pos += 1
            return v, pos
        d = pos
        if pos < len(calcul) and (calcul[pos].isdigit() or calcul[pos] == '.') :
            while pos < len(calcul) and (calcul[pos].isdigit() or calcul[pos] == '.') :
                pos += 1
            return float(calcul[d:pos]), pos
        raise ValueError(f"Erreur position {pos}")
    


def calcul() :
        try :
            arbre = input_calcul()
            arbre, _ = orgarniser_calcul(arbre)
            
            def evaluer(a) :
                if isinstance(a, tuple):
                    if len(a) == 2:
                        # Operateur unaire (postfixe)
                        operateur, operande = a
                        op = evaluer(operande)
                        
                        match operateur :
                            case '!':
                                calc = factoriel(op)
                            case 'q':
                                calc = carre(op)
                            case _:
                                calc = op
                        return calc
                    else:
                        # Operateur binaire
                        operateur, gauche, droit = a
                        g = evaluer(gauche)
                        d = evaluer(droit)
                        match operateur :
                            case '*' :
                                calc = (multiple(g, d))
                            case '/' :
                                calc = (div(g, d))
                            case '+' :
                                calc = (add(g, d))
                            case '-' :
                                calc = (sous(g, d))
                            case '%' : 
                                calc = (modulo(g, d))
                            case '//' : 
                                calc = (div_euclidienne(g, d))
                            case '^' :
                                calc = (puissance(g, d))
                            case 'V' :
                                calc = (racine(g, d))
                        
                        return calc
                else:
                    return a
            
            resultat = evaluer(arbre)
            if isinstance(resultat, float) and resultat.is_integer():
                return int(resultat)
            return resultat
        except ValueError as e:
            print(f"Erreur : {e}")
            return e

#======HISTORIQUE======#

calculs=expression

if list_num :
    results = list_num[-1]
else:
    print("La liste est vide")

def historique(calculs,resultats) :
    try:
        with open("data.pkl", "rb") as f :
            historik = pickle.load(f)  
        if not isinstance(historik, list) :
            print("Erreur : le fichier ne contient pas une liste. Réinitialisation...")
            historik = []
    except (FileNotFoundError, EOFError) :
        historik = [] 
    historik.append({calculs:resultats})
    with open("data.pkl", "wb") as f :
        pickle.dump(historik, f)
    return "derniers resultats", calculs, resultats

def afficher_historique() :
    try:
        with open("data.pkl", "rb") as f :
            donnees_chargees = pickle.load(f)
        return donnees_chargees
    except (FileNotFoundError, EOFError) :
        return []
    
def reset_historique() :
    historik=[]
    with open("data.pkl", "wb") as f :
        pickle.dump(historik,f)
    display_historique.config(state="normal")
    display_historique.delete("1.0", tkinter.END)
    display_historique.insert("1.0","Historique vide")
    display_historique.config(state="disabled")

def update_historique() :
    hist = afficher_historique()
    display_historique.config(state="normal")
    display_historique.delete("1.0", tkinter.END)
    
    if hist :
        for item in hist:
            for calcul, resultat in item.items() :
                display_historique.insert("end", f"{calcul} = {resultat}\n")
    else:
        display_historique.insert("1.0", "Historique vide")

    display_historique.config(state="disabled")

#========FONCTIONALITÉ DES BOUTONS========#

def clique(button) :
    global expression
    global resultats

    if button == "C" :
        del list_num[0:len(list_num)]
        expression = ""
        display.config(font=('Arial', 20)) 
        display.delete(0,tkinter.END)

    elif button == "=" :
        try :
            resultats=(calcul())
            if not isinstance(resultats, (ValueError, Exception, str)) :
                display.config(font=('Arial', 20))
                display.delete(0,tkinter.END)
                display.insert(0,resultats)
                historique(expression,resultats)
                update_historique()
                expression=str(resultats)
            else :
                display.config(font=('Arial', 10)) 
                display.delete(0,tkinter.END)
                display.insert(0,f"Erreur: {resultats}")
                expression = ""
        except Exception as e :
            display.config(font=('Arial', 10)) 
            display.delete(0,tkinter.END)
            display.insert(0,f"Erreur: {e}")
            expression=""   
    
    elif button == "<":
        display.delete(0,tkinter.END)
        expression = expression[:-1]
        display.insert(0,expression)
    
    else:
        expression += str(button)
        display.delete(0,tkinter.END)
        display.insert(0,expression)

#clavier
def clav_press (event):
    global expression
    touche=event.char
    touchy=event.keysym

    if touche == "=":
        try :
            resultats=(calcul())
            if not isinstance(resultats, (ValueError, Exception, str)):
                display.config(font=('Arial', 20))
                display.delete(0,tkinter.END)
                display.insert(0,resultats)
                historique(expression,resultats)
                update_historique()
                expression = str(resultats)

            else:
                display.config(font=('Arial', 10)) 
                display.delete(0,tkinter.END)
                display.insert(0,f"Erreur: {resultats}")
                expression = ""

        except Exception as e:
            display.config(font=('Arial', 10)) 
            display.delete(0,tkinter.END)
            display.insert(0,f"Erreur: {e}")
            expression = ""

    elif touchy == "Delete":
        reset_historique()

    elif touche == "c":
        display.delete(0,tkinter.END)
        expression = ""
        display.insert(0,expression)

    elif touchy == "BackSpace":

        if len(expression)>0:
            display.delete(0,tkinter.END)
            expression=expression[:-1]
            display.insert(0,expression)

        else:
            display.insert(0,"Il n'y a rien a supprimer")

    elif touche in lst_button:
        expression+=str(touche)
        display.delete(0,tkinter.END)
        display.insert(0,expression)

    else:
        display.delete(0,tkinter.END)
        expression = "Erreur!"
        display.insert(0,expression)


chaine=expression
resultats=None

app = tkinter.Tk()
app.geometry("720x560")
app.title("Calculator")

# Frame de la calculatrice
calcul_area = tkinter.Frame(app, relief='solid', bd=2, bg='lightgray')
calcul_area.place(x=40, y=40, width=260, height=510)

#display area
display = tkinter.Entry(calcul_area, borderwidth=3, justify="right", font=('Arial', 20), relief='groove', bg='white', fg='black',width=15)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=15, ipady=20, sticky="ew")

# Historique
label_historique = tkinter.Label(app, text="Historique :", font=('Arial', 12, 'bold'))
label_historique.place(x=375, y=35) 
display_historique = tkinter.Text(app, height=5, width=40)
display_historique.place(x=375, y=60)
# crée le fichier d'historique si besoin
if not os.path.exists("data.pkl"):
    historik = []
    with open("data.pkl", "wb") as f:
        pickle.dump(historik, f) 
if resultats is not None:
    display_historique.insert("end", historique(expression,resultats))
display_historique.config(state="disabled")

update_historique()

# affichage des boutons
row=2
column=0
for button in lst_button:
    cmd = lambda x=button: clique(x)
    if not button.isdigit() and button != '.':

        if button == "C" or button == "<":
            btn = tkinter.Button(calcul_area, text=button, width=3, height=2, font=('Arial', 12, 'bold'), relief='ridge', command=cmd, background="#B34D4D")
        elif button == "=" :
            btn = tkinter.Button(calcul_area, text=button, width=3, height=2, font=('Arial', 12, 'bold'), relief='ridge', command=cmd, background="#68B34D")
        else :
            btn = tkinter.Button(calcul_area, text=button, width=3, height=2, font=('Arial', 12, 'bold'), relief='ridge', command=cmd, background="#4D73B3")

    else :
        btn = tkinter.Button(calcul_area, text=button, width=3, height=2, font=('Arial', 12, 'bold'), relief='ridge', command=cmd)
    btn.grid(row=row, column=column, pady=5, padx=5)
    column += 1

    if column > 4:
        column = 0
        row += 1

# Bouton historique
btn_historique = tkinter.Button(app, text="Reset Historique", command=reset_historique)
btn_historique.place(x=600, y=150)

app.bind("<Key>",clav_press)
app.mainloop()
