# TP: Application TODO list

Nous allons créer une application client/serveur permettant de gérer une liste de tâches.

Dans notre TP, le client et le serveur seront tous les deux sur votre ordinateur.
- Le client sera un navigateur web
- Le serveur sera un programme Python utilisant le *framework* **Flask**
  - un framework est un ensemble de composants logiciels qui sert à créer les fondations d'un autre logiciel
 

## Créer un serveur web minimal
1. créer un dossier `todo_server` sur votre bureau
2. ouvrir l'éditeur Python et copier/coller le code suivant dans un fichier `todo.py`:
```python
from flask import Flask # 1
app = Flask(__name__) # 2


@app.route('/') # 3
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True) # 4
```
1. importe l'objet `Flask` dans le module `flask`
2. crée un objet `app` qui permet de paramétrer l'application Flask
3. Nous ajoutons un décorateur `@app.route` à la fonction `index`. 

- exercice: regarder l'adresse IP de votre voisin, et connectez-vous à son serveur.