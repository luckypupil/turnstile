#!/usr/bin/env python
import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from pprint import pprint


from app import app, models, db

#app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)
manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models, pp=pprint)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()