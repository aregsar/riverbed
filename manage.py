from app import app
from flask.ext.script import Manager,Server

##
#import models
##

from app.models.user import User


##
#create the manager
##
manager = Manager(app)


##
#add commands
##

#python manage.py runserver
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

##
#run the app
##

print app.url_map
#print app.config


if __name__ == '__main__':
    manager.run()

