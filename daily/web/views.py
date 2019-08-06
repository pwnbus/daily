from flask import Blueprint, render_template, jsonify
from datetime import datetime

from daily.models.header import Header
from daily.models.task import Task
from daily.db import session

mod = Blueprint('index', __name__)


@mod.route('/')
def index():
    headers = session.query(Header).all()
    return render_template('index.html', tasks_data=headers)


@mod.route('/task/<task_id>/toggle')
def task(task_id):
    task = session.query(Task).get(task_id)
    if task is None:
        return jsonify({'error': 'Incorrect task_id'})

    if task.completed:
        # Set to uncompleted
        task.completed = False
        task.completed_at = None
        status = "Set task '{0}' to Uncompleted".format(task.name)
    else:
        task.completed = True
        task.completed_at = datetime.now().isoformat()
        status = "Set task '{0}' to Completed".format(task.name)
    session.add(task)
    session.commit()
    return jsonify({'status': status})
