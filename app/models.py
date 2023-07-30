from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, nullable=False)
    telefone = db.Column(db.String(64), index=True, nullable=False)
    endereco = db.Column(db.String(64), index=True, nullable=False)
    cpf = db.Column(db.String(120), index=True, nullable=False)
