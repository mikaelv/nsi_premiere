from flask import Flask, render_template, request

tasks = [
    {'title': 'préparer le TP client/serveur', 'done': True},
    {'title': 'commander le robinet', 'done': False},
    {'title': 'faire les courses', 'done': False},
]


def hello():
    return 'Hello World!'


def get_tasks():
    html = '<!DOCTYPE html>\n' \
           '<html><body>\n' \
           '<h1>TO DO list</h1>\n' \
           '<table>\n'

    for task in tasks:
        title = task['title']
        style = ''
        # exercice 1: strikethrough if done
        if task['done']:
            style = 'color: gray'
        task_html = f'<div style="{style}"> - {title}</div>'
        html += '    <tr><td>' + task_html + '</td></tr>\n'
    html += '</table> \n' \
            '</body></html>'
    return html


def get_tasks2():
    return render_template('tasks2.html', tasks=tasks)


def get_tasks3():
    return render_template('tasks3.html', tasks=tasks)


def create_task3():
    result = request.form
    title = result['title']
    tasks.append({'title': title, 'done': False})
    return get_tasks3()


def get_tasks4():
    return render_template('tasks4.html', tasks=tasks)


def create_task4():
    form = request.form
    title = form['title']
    tasks.append({'title': title, 'done': False})
    return get_tasks4()

def update_task4(id):
    form = request.form
    i = int(id) - 1
    print(form)
    task = tasks[i]
    if form.get('done'):
        task['done'] = True
    else:
        task['done'] = False

    return get_tasks4()



# TODO: filter, checkbox, css
# more tricky: add another field 'due date'
# traitement client: sort or filter. compare client vs serveur
# cookie session
# idees : bouton done per task, bouton "delete all done", CSS, refresh button: show problemm, use redirection
# objectifs: connaitre methodes GET/POST. Comprendre traitement client vs serveur


if __name__ == '__main__':
    app = Flask(__name__)
    app.add_url_rule('/hello', view_func=hello)
    app.add_url_rule('/tasks', view_func=get_tasks)

    app.add_url_rule('/tasks2', view_func=get_tasks2)

    app.add_url_rule('/tasks3', view_func=get_tasks3)
    app.add_url_rule('/tasks3', view_func=create_task3, methods=["POST"])

    app.add_url_rule('/tasks4', view_func=get_tasks4)
    app.add_url_rule('/tasks4', view_func=create_task4, methods=["POST"])
    app.add_url_rule('/tasks4/<id>', view_func=update_task4, methods=["POST"])
    # 5: add "onClick", remove save button
    app.run(debug=True)
