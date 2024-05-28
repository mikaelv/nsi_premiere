from flask import Flask, render_template, request

tasks = [
    {'title': 'préparer le TP client/serveur', 'done': True},
    {'title': 'commander le robinet', 'done': False},
    {'title': 'faire les courses', 'done': False},
]


def hello():
    return 'Hello World!'


def get_tasks():
    return render_template('tasks.html', tasks=tasks)


if __name__ == '__main__':
    app = Flask(__name__)
    app.add_url_rule('/hello', view_func=hello)
    app.add_url_rule('/tasks', view_func=get_tasks)
    app.run(debug=True)
