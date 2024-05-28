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
    form = request.form
    title = form['title']
    tasks.append({'title': title, 'done': False})
    return get_tasks()

def update_task(id):
    form = request.form
    i = int(id) - 1
    print(form)
    task = tasks[i]
    if form.get('done'):
        task['done'] = True
    else:
        task['done'] = False

    return get_tasks()


if __name__ == '__main__':
    app = Flask(__name__)
    app.add_url_rule('/hello', view_func=hello)
    app.add_url_rule('/tasks', view_func=get_tasks)
    app.add_url_rule('/tasks', view_func=create_task, methods=["POST"])
    app.add_url_rule('/tasks/<id>', view_func=update_task, methods=["POST"])
    # 5: add "onClick", remove save button
    app.run(debug=True)
