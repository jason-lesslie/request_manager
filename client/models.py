from request_manager import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    def __init__(self, name):
        self.name = name

# __repr__ used to interact with terminal
    def __repr__(self):
        return '<Client %r>' % self.name
