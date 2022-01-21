from userapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password
