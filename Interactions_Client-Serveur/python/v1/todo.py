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


def init():
    app = Flask(__name__)
    app.add_url_rule('/hello', view_func=hello)
    app.add_url_rule('/tasks', view_func=get_tasks)
    app.run(debug=True)


if __name__ == '__main__':
    init()

