# -*- coding: utf-8 -*-
lst_button=[
    "*","+","-","%","!",   
    "7","8","9",".","q",
    "4","5","6","^","/",
    "1", "2","3","(","V",
    "0","=","C",")", "//",
    "<"
    ]

#import

import re
import pickle
import tkinter
from tkinter import *

#screen
app = tkinter.Tk()
app.geometry("720x500")
app.title("Calculator")

#functions

val_symbole = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
symboles = ['+', '-', '*', '/', '(', ')', '^', '.', '%', '//', 'V', '!', 'q']
list_calc = []
list_num = []

#labels

expression=""

#====== Opérations ========#
def add(a,b):
    return a + b

def sous (a,b):
    return a-b

def multiple (a,b):
    return a*b

def div (a,b):
    if b == 0:
        raise ValueError("Erreur : Division par zéro")
    else:
        return a/b

def modulo (a,b):
    if b == 0:
        raise ValueError("Erreur : Division par zéro")
    else:
        print(a%b)
        return a%b

def div_euclidienne(a,b):
    if b == 0:
        raise ValueError("Erreur : Division par zéro")
    else:
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
    a = int(a)
    if a < 0:
        raise ValueError("Factorielle d'un nombre negatif")
    if a == 0 or a == 1:
        return 1
    resultat = 1
    for i in range(2, a + 1):
        resultat *= i
    return resultat

#======== Reconnaisance de calcul =========#

def input_calcul(calcul=None, pos=0, niveau='input'):
    # Niveau input : demander le calcul
        invalide = False
        calcul = expression     
        i = 0
        while i < len(calcul):
            c = calcul[i]
            if c.isdigit() or c in '+-()*^.% V!q':
                i += 1
                continue
            if c == '/':
                if i + 1 < len(calcul) and calcul[i + 1] == '/':
                    i += 2
                    continue
                i += 1  
                continue
            if c.isspace():
                i += 1
                continue
            print("Caractère non autorisé détecté.")
            invalide = True
            break
        if invalide:
            raise ValueError("Caractère non autorisé détecté.")

            
        if calcul.count('(') != calcul.count(')'):
            print("Parenthèses non équilibrées.")
            raise ValueError("Parenthèses non équilibrées.")
        calcul=calcul.replace(' ','')
        return calcul
    
def orgarniser_calcul(calcul, pos=0, niveau='add'):             
    # Niveau add : addition/soustraction
    if niveau == 'add':
        g, pos = orgarniser_calcul(calcul, pos, 'mult')
        while pos < len(calcul) and calcul[pos] in '+-':
            o = calcul[pos]
            pos += 1
            d, pos = orgarniser_calcul(calcul, pos, 'mult')
            g = (o, g, d)
        return g, pos
    
    # Niveau mult : multiplication/division
    elif niveau == 'mult':
        g, pos = orgarniser_calcul(calcul, pos, 'puis')
        while pos < len(calcul):
            if calcul.startswith('//', pos):
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
    elif niveau == 'postfix':
        g, pos = orgarniser_calcul(calcul, pos, 'base')
        while pos < len(calcul) and calcul[pos] in '!q':
            g = (calcul[pos], g)
            pos += 1
        return g, pos
    
    # Niveau puis : puissance
    elif niveau == 'puis':
        g, pos = orgarniser_calcul(calcul, pos, 'postfix')
        if pos < len(calcul) and calcul[pos] in '^V':
            o = calcul[pos]
            pos += 1
            d, pos = orgarniser_calcul(calcul, pos, 'puis')
            g = (o, g, d)
        return g, pos
    
    # Niveau base : nombres et parenthèses
    elif niveau == 'base':
        if pos < len(calcul) and calcul[pos] == '-':
            pos += 1
            v, pos = orgarniser_calcul(calcul, pos, 'base')
            return ('*', -1.0, v), pos
        if pos < len(calcul) and calcul[pos] == '+':
            pos += 1
            return orgarniser_calcul(calcul, pos, 'base')
        if pos < len(calcul) and calcul[pos] == '(':
            pos += 1
            v, pos = orgarniser_calcul(calcul, pos, 'add')
            pos += 1
            return v, pos
        d = pos
        if pos < len(calcul) and (calcul[pos].isdigit() or calcul[pos] == '.'):
            while pos < len(calcul) and (calcul[pos].isdigit() or calcul[pos] == '.'):
                pos += 1
            return float(calcul[d:pos]), pos
        raise ValueError(f"Erreur position {pos}")
    


def calcul():
        try:
            arbre = input_calcul()
            arbre, _ = orgarniser_calcul(arbre)
            
            def evaluer(a):
                if isinstance(a, tuple):
                    if len(a) == 2:
                        # Operateur unaire (postfixe)
                        operateur, operande = a
                        op = evaluer(operande)
                        
                        match operateur:
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
                        match operateur:
                            case '*':
                                calc = (multiple(g, d))
                            case '/':
                                calc = (div(g, d))
                            case '+':
                                calc = (add(g, d))
                            case '-':
                                calc = (sous(g, d))
                            case '%': 
                                calc = (modulo(g, d))
                            case '//': 
                                calc = (div_euclidienne(g, d))
                            case '^':
                                calc = (puissance(g, d))
                            case 'V':
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

if list_num:
    results = list_num[-1]
else:
    print("La liste est vide")

def historique(calculs,resultats):
    try:
        with open("data.pkl", "rb") as f:
            historik = pickle.load(f)  
        if not isinstance(historik, list):#nv
            print("Erreur : le fichier ne contient pas une liste. Réinitialisation...")#nv
            historik = []#nv
    except (FileNotFoundError, EOFError):#modif
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
    display_historique.config(state="normal")#nv
    display_historique.delete("1.0", tkinter.END)#nv
    display_historique.insert("1.0","Historique vide")#nv
    display_historique.config(state="disabled")#nv

def update_historique():#nv
    hist = afficher_historique()#nv
    display_historique.config(state="normal")#nv
    display_historique.delete("1.0", tkinter.END)#nv
    
    if hist:#nv
        for item in hist:#nv
            for calcul, resultat in item.items():#nv
                display_historique.insert("end", f"{calcul} = {resultat}\n")#nv
    else:#nv
        display_historique.insert("1.0", "Historique vide")#nv

    display_historique.config(state="disabled")#nv    

#========FONCTIONALITÉ DES BOUTONS========#

def clique(button):
    global expression
    global resultats
    if button=="C":
        del list_num[0:len(list_num)]
        expression=""
        display.delete(0,tkinter.END)
    elif button=="=":
        try :
            resultats=(calcul())
            display.delete(0,tkinter.END)
            display.insert(0,resultats)
            historique(expression,resultats)
            update_historique()
            expression=str(resultats)
        except Exception as e:
            display.delete(0,tkinter.END)
            display.insert(0,"Erreur")
            expression=""
    elif button=="<":
        display.delete(0,tkinter.END)
        expression=expression.rstrip(expression[-1])
        display.insert(0,expression)
    else:
        expression+=str(button)
        display.delete(0,tkinter.END)
        display.insert(0,expression)
#nouvelle fonction
def clav_press (event):
    global expression
    touche=event.char
    if touche=="=":
        try :
            resultats=(calcul())
            display.delete(0,tkinter.END)
            display.insert(0,resultats)
            historique(expression,resultats)
            update_historique()
            expression=str(resultats)
        except Exception as e:
            display.delete(0,tkinter.END)
            display.insert(0,"Erreur")
            expression=""
    elif touche=="c":
        display.delete(0,tkinter.END)
        expression=""
        display.insert(0,expression)
    elif touche=="BackSpace":
        if len(expression)>0:
            display.delete(0,tkinter.END)
            expression=expression.rstrip(expression[-1])
            display.insert(0,expression)
        else:
            display.insert(0,"Il n'y a rien a supprimer")
    elif touche in lst_button:
        expression+=str(touche)
        display.delete(0,tkinter.END)
        display.insert(0,expression)
    else:
        display.delete(0,tkinter.END)
        expression="Erreur!"
        display.insert(0,expression)       
        
chaine=expression
resultats=0

#display area

display = tkinter.Entry(app,borderwidth=2,justify="right")
display.grid(row=0, column=0, columnspan=5,padx=10,pady=20,ipady=10)
display_historique = tkinter.Text(app, height=5, width=40)
display_historique.grid(row=0, column=5, columnspan=5, padx=50, pady=20)
display_historique.insert("end",historique(expression,resultats))
display_historique.config(state="disabled")

update_historique()

row=2
column=0

for button in lst_button:
    cmd=lambda x=button : clique(x)
    btn=tkinter.Button(app, text=button, width=5, height=2, command=cmd)
    btn.grid(row=row, column=column, pady=5, padx=5)
    column+=1
    if column>4:
        column=0
        row+=1


btn_historique = Button (app, text="Reset Historique", command = reset_historique )
btn_historique.grid(row=row, column=column+5)

app.bind("<Key>",clav_press) #NOUVEAU

app.mainloop()