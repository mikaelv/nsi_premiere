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


def create_task():
    result = request.form
    title = result['title']
    tasks.append({'title': title, 'done': False})
    return get_tasks()


def init():
    app = Flask(__name__)
    app.add_url_rule('/tasks', view_func=get_tasks)
    app.add_url_rule('/tasks', view_func=create_task, methods=["POST"])
    app.run(debug=True)


if __name__ == '__main__':
    app = init()