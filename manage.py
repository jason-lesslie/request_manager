import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from request_manager import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', 'localhost'),
    port = int(os.getenv('PORT', 5000))
    )
)

if __name__ == "__main__":
    manager.run()
