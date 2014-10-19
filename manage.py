#!/usr/bin/env python
import os
from flask.ext.script import Manager


from app import create_app


#app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(create_app)

@manager.shell
def make_shell_context():
    app = create_app()
    from app import db, models
    return dict(app=app, db=db, models=models)



if __name__ == '__main__':
    manager.run()