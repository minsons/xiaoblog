from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps import create_app,db
#app.config.from_object('app.config')

app = create_app()
# configuration
"""
SQLALCHEMY_DATABASE_URI = 'mysql://xiaoia:123456@117.48.202.102/logins'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
"""

"""
在命令行里执行以下：
python gendb.py init
python gendb.py migrate
python gendb.py upgrade
"""
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()