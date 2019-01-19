from app import db
import json

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(90), nullable=False)
    foto = db.Column(db.TEXT, nullable=False)

    def buat(username, foto):
        data = User(username=username, foto=foto)
        db.session.add(data)
        db.session.commit()