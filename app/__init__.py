import os
from flask import Flask
from config import config
from flask.ext.sqlalchemy import SQLAlchemy



from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])
bootstrap.init_app(app)
db = SQLAlchemy(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint,url_prefix='/admin')



# def create_app(config_version='default'):
#     app = Flask(__name__)
#     app.config.from_object(config[config_version])
#     bootstrap.init_app(app)
    
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
	
#     db.init_app(app)
	
#     return app

