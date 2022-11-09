from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable= False)
    note = db.Column(db.String, nullable = False)
