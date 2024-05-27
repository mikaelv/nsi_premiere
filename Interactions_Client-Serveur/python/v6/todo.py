from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session


def hello():
    return 'Hello World!'


def read_session_tasks():
    print(session.get('tasks'))
    if 'tasks' in session:
        return session['tasks']
    else:
        tasks = []
        session['tasks'] = tasks
        return tasks


def write_session_tasks(tasks):
    session['tasks'] = tasks


def get_tasks():
    return render_template('tasks.html', tasks=read_session_tasks())


def create_task():
    form = request.form
    title = form['title']
    tasks = read_session_tasks()
    tasks.append({'title': title, 'done': False})
    write_session_tasks(tasks)
    return redirect(url_for('get_tasks'))

def update_task(id):
    form = request.form
    i = int(id) - 1
    print(form)
    task = read_session_tasks()[i]
    if form.get('done'):
        task['done'] = True
    else:
        task['done'] = False

    return get_tasks()




# TODO: filter, checkbox, css
# more tricky: add another field 'due date'
# traitement client: sort or filter. compare client vs serveur
# cookie session
# idees : bouton "delete all done", CSS, refresh button: show problem, use redirection
# ajouter attribut 'categorie' drop-down
# objectifs: connaitre methodes GET/POST. Comprendre traitement client vs serveur


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key = 'supersecretkey'
    Session(app)
    app.add_url_rule('/hello', view_func=hello)
    app.add_url_rule('/tasks', view_func=get_tasks)
    app.add_url_rule('/tasks', view_func=create_task, methods=["POST"])
    app.add_url_rule('/tasks/<id>', view_func=update_task, methods=["POST"])
    # 5: add "onClick", remove save button
    app.run(debug=True)
