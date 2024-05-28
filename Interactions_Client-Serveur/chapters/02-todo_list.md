__TOC__

# TP: Application TO DO list

Nous allons créer une application client/serveur permettant de gérer une liste de tâches.

Dans notre TP, le client et le serveur seront tous les deux sur votre ordinateur.
- Le client sera un navigateur web
- Le serveur sera un programme Python utilisant le *framework* **Flask**
  - un framework est un ensemble de composants logiciels qui sert à créer les fondations d'un autre logiciel
- Le client communiquera avec le serveur en utilisant le protocole HTTP.
   
  
## Créer un serveur web minimal
1. créer un dossier `todo_server` sur votre bureau
2. ouvrir l'éditeur Python et copier/coller le code suivant dans un fichier `todo.py`:
```python
from flask import Flask # 1


def hello(): # 2
    return "Hello World!"


def init():
    app = Flask(__name__) # 3
    app.add_url_rule('/hello', view_func=hello) # 4
    app.run(debug=True) # 5    

if __name__ == '__main__':
    init()
```
3. Lancer le programme
4. ouvrir un navigateur et appeler l'URL http://127.0.0.1:5000/hello


### Analyse du code
1. importe l'objet `Flask` dans le module `flask`
2. la fonction `hello()` sera appelée lorsque le serveur recevra une requête HTTP
3. crée un objet `app` qui permet de paramétrer l'application Flask
4. Nous ajoutons une règle d'URL: lorsque le chemin demandé est `/hello`, Flask saura qu'il doit appeler la fonction `hello`.
5. Démarre l'application Flask, en mode debug. 
   Le mode debug permet entre autre de recharger automatiquement les fichiers `.py` lorsque nous les modifions.

### Exercices
- regardez l'adresse IP de votre voisin, et connectez-vous à son serveur. Sous Windows, utilisez la commande `ipconfig`
- dans le navigateur, ouvrir les outils développeur (`ctrl-shift-I`), onglet "Network". 
  Observez les requêtes HTTP. Essayez d'autres URL. Quels sont les codes de retour du serveur ? 

## Afficher la liste de taches
Pour notre application TO DO List, nous allons coder une première fonction qui va renvoyer une page HTML avec une liste de tâches.

1. Ajouter le code suivant au fichier `todo.py`:
```python
tasks = [ # 1
    {'title': 'préparer le TP client/serveur', 'done': True},
    {'title': 'commander le robinet', 'done': False},
    {'title': 'faire les courses', 'done': False},
]


def get_tasks():
    html = '<!DOCTYPE html>\n' # 2
           '<html><body>\n'
           '<h1>TO DO list</h1>\n'
           '<table>\n'

    for task in tasks: # 3
        title = task['title']
        style = ''
        task_html = f'<div style="{style}"> - {title}</div>' # 4
        html += '    <tr><td>' + task_html + '</td></tr>\n'
    html += '</table> \n'
            '</body></html>'
    return html # 5
```

2. Modifier la fonction `init()`:
```python
def init():
    app = Flask(__name__)
    app.add_url_rule('/hello', view_func=hello)
    app.add_url_rule('/tasks', view_func=get_tasks) # 6
    app.run(debug=True)
```

3. Sauvegarder. Le mode debug devrait recharger le nouveau code
4. Ouvrir l'URL http://127.0.0.1:5000/tasks

### Analyse du code
1. Déclare une variable globale `tasks` qui contient la liste des tâches à afficher.
2. Déclare une variable `html` avec l'en-tête HTML, contenant un tableau.
3. La boucle ajoute des lignes de tableau avec les balises `<tr><td>` pour chaque tâche 
4. la fonction renvoie le code HTML à renvoyer au navigateur
5. nous ajoutons une `url_rule` pour pouvoir appeler notre fonction

### Exercices
1. Dans le navigateur, observez le code HTML généré.
2. Ajoutez une condition pour changer le style si la tâche a la valeur `done=True`.
3. Modifiez la variable `tasks` pour ajouter une tâche.

