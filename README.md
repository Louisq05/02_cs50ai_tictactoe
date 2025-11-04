# ❌⭕ Tic-Tac-Toe — AI with Minimax

> Build an unbeatable Tic-Tac-Toe AI using the **Minimax algorithm**.

Ce projet implémente une intelligence artificielle capable de jouer au Tic-Tac-Toe de manière optimale. L'IA utilise l'algorithme **Minimax**, garantissant une partie parfaite — l’utilisateur ne peut jamais gagner si les deux joueurs jouent parfaitement.

---

## 🧠 Objectif du projet

- Implémenter tous les mécanismes d’un jeu Tic-Tac-Toe
- Déterminer automatiquement le joueur courant
- Calculer tous les coups possibles
- Simuler les actions et retourner un nouvel état du plateau
- Détecter victoire / égalité / fin de partie
- Utiliser **Minimax** pour choisir la décision optimale

---

## 🎮 Démonstration

Une fois le projet complété, lance le jeu :
`python runner.py`
Vous pourrez jouer via l'interface graphique Pygame contre une IA **imbattable**.

---

## 📦 Exemple de gameplay

✅ Vous pouvez jouer contre l’IA  
❌ Vous ne pouvez pas la battre si vous jouez optimalement  
🤖 L’IA peut vous battre si vous faites une erreur

---

## 🗂️ Structure du projet

```bash
tictactoe/ 
│── tictactoe.py     # logique du jeu + IA Minimax (à compléter) 
│── runner.py        # interface graphique Pygame (déjà fournie) 
│── requirements.txt # dépendances (pygame) 
│── README.md        # ce fichier``
```
---

## ⚙️ Installation

### 1️⃣ Cloner le projet

`git clone https://github.com/<your-username>/tictactoe-ai.git cd tictactoe-ai`

### 2️⃣ Installer les dépendances

> Python recommandé : **3.12**

`pip3 install -r requirements.txt`

### 3️⃣ Lancer

`python runner.py`

---

## 📋 Spécifications Implémentées

|Fonction|Rôle|
|---|---|
|`player(board)`|Détermine à qui le tour|
|`actions(board)`|Liste des coups possibles|
|`result(board, action)`|Retourne un nouvel état après un coup|
|`winner(board)`|Détecte un gagnant|
|`terminal(board)`|Teste si la partie est finie|
|`utility(board)`|Score (+1 X, -1 O, 0 égalité)|
|`minimax(board)`|Retourne le coup optimal|

Plateau représenté par une liste 3×3 contenant `X`, `O`, ou `EMPTY`.

---

## 🧪 Tests

`check50 ai50/projects/2024/x/tictactoe`

### Style

`style50 tictactoe.py`

---

## 🤖 Minimax

L’algorithme explore toutes les configurations possibles :

- ✅ Maximiser le score pour `X`
- ✅ Minimiser le score pour `O`
- ✅ Choisir la meilleure option selon le tour

> Résultat : l'IA ne perd jamais.

---

## 🎓 À propos

Projet réalisé dans le cadre du cours  
**CS50’s Introduction to Artificial Intelligence with Python**.

---

## 🙌 Remerciements

- Harvard CS50 AI team
- Pygame community