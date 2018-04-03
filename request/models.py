from request_manager import db

class RequestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    description = db.Column(db.String(100))
    target_date = db.Column(db.Date())
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client_request_priority = db.Column(db.Integer)
    def __init__(self, title, description, target_date, product_id, client_id, client_request_priority):
        self.title = title
        self.description = description
        self.target_date = target_date
        self.product_id = product_id
        self.client_id = client_id
        self.client_request_priority = client_request_priority

# __repr__ used to interact with terminal
    def __repr__(self):
        return '<Title %r>' % self.title
