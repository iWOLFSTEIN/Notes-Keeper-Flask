from flask import Flask
from flask_restful import Api
from endpoints.notes import Notes
from models import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


api.add_resource(Notes, "/notes/<int:id>")


if __name__ == '__main__':
    app.run(debug=True, port=8000)