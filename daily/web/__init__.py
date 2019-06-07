from flask import Flask

from daily.web import views
from daily.config import config

app = Flask(__name__)
app.config.update(DEBUG=config.debug)

app.register_blueprint(views.mod)
