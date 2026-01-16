# Calculatrice avec Interface Graphique

## Description

Calculatrice graphique développée en Python avec Tkinter. Elle permet d'effectuer des calculs mathématiques avec une interface simple et un historique des opérations.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/73c14033-d330-4315-ab2d-06eadc1a5470" />


## Fonctionnalités

- Interface graphique intuitive avec boutons cliquables
- Affichage en temps réel des calculs
- Entrée des calculs par boutons ou clavier
- Historique automatique des opérations
- Support des opérations mathématiques avancées
- Gestion des erreurs (division par zéro, parenthèses mal équilibrées)
- Sauvegarde de l'historique entre les sessions

## Opérations disponibles

| Opération | Symbole | Exemple |
|-----------|---------|---------|
| Addition | + | 5 + 3 |
| Soustraction | - | 10 - 4 |
| Multiplication | * | 6 × 7 |
| Division | / | 20 ÷ 4 |
| Division euclidienne | // | 17 // 5 |
| Modulo | % | 17 % 5 |
| Puissance | ^ | 2^3 |
| Racine | V | 8V3 (racine cubique de 8) |
| Factorielle | ! | 5! |
| Carré | q | 5q |

## Installation

### Prérequis
- Python 3.6 ou supérieur
- Tkinter (inclus par défaut avec Python)

### Étapes d'installation

1. Téléchargez le fichier `calculatrice.py`

2. Vérifiez que Python est installé :
```bash
python --version
```

3. Lancez la calculatrice :
```bash
python calculatrice.py
```

## Utilisation

### Interface

La calculatrice se compose de trois zones :

1. **Zone de calcul** (gauche) :
   - Écran d'affichage en haut
   - Boutons numériques et opérateurs
   - Boutons spéciaux (C, <, =)

2. **Zone historique** (droite) :
   - Affiche tous les calculs précédents
   - Sauvegardé automatiquement

3. **Boutons de contrôle** :
   - **C** : Effacer l'écran
   - **<** : Supprimer le dernier caractère
   - **=** : Calculer le résultat
   - **Reset Historique** : Vider l'historique

### Raccourcis clavier
Quelques raccourcis clavier :
   - **C** : Bouton C de l'interface (effacer l'écran)
   - **suppr** : bouton Reset Historique de l'interface
   - **=** : bouton = de l'interface (calculer le résultat)

### Exemples d'utilisation

**Calcul simple :**
```
2 + 3 × 4
Résultat : 14
```

**Avec parenthèses :**
```
(10 + 5) / 3
Résultat : 5
```

**Puissance :**
```
2^10
Résultat : 1024
```

**Factorielle :**
```
5!
Résultat : 120
```

**Racine cubique :**
```
27V3
Résultat : 3
```

**Carré :**
```
5q
Résultat : 25
```

## Structure du programme

### Fonctions principales

- `clique(button)` : Gère les clics sur les boutons
- `calcul()` : Effectue le calcul de l'expression
- `input_calcul()` : Valide l'expression entrée
- `orgarniser_calcul()` : Analyse et organise le calcul selon les priorités
- `historique()` : Sauvegarde le calcul dans l'historique
- `update_historique()` : Met à jour l'affichage de l'historique

### Priorités des opérateurs

1. Parenthèses `( )`
2. Factorielle `!` et Carré `q`
3. Puissance `^` et Racine `V`
4. Multiplication `*`, Division `/`, Division euclidienne `//`, Modulo `%`
5. Addition `+` et Soustraction `-`

## Fichiers générés

- `data.pkl` : Fichier contenant l'historique des calculs (créé automatiquement)

## Couleurs des boutons

- **Bleu** (#4D73B3) : Opérateurs mathématiques
- **Rouge** (#B34D4D) : Boutons C et <
- **Vert** (#68B34D) : Bouton =
- **Gris** : Chiffres et point décimal

## Gestion des erreurs

Le programme gère automatiquement :
- Division par zéro
- Parenthèses non équilibrées
- Caractères non autorisés
- Factorielle de nombres négatifs

Les erreurs sont affichées directement sur l'écran de la calculatrice.

## Limitations

- La factorielle fonctionne uniquement avec des entiers positifs
- Pas de support pour les fonctions trigonométriques
- La racine carrée doit être écrite avec V (ex: 16V2)

## Améliorations possibles

- [ ] Ajouter des fonctions trigonométriques
- [ ] Exporter l'historique en fichier texte
- [ ] Thème sombre/clair
- [ ] Calculatrice scientifique étendue

## Auteur

Mohamed Mahamoud

Logann Grange

Clément Koch

---
