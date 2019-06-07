from flask import Blueprint, render_template

from daily.models.header import Header
from daily.db import session

mod = Blueprint('index', __name__)


@mod.route('/')
def index():
    headers = session.query(Header).all()
    return render_template('index.html', tasks_data=headers)
