from flask import Flask
from config import config

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_version):
	app = Flask(__name__)
	app.config.from_object(config[config_version])

	db.init_app(app)

	bootstrap.init_app(app)
	 
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
