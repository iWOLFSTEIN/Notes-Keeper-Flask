from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models import NoteModel, db



resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'note': fields.String
}


class Notes(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = NoteModel.query.filter_by(id=id).first()
        if not result:
            abort(404, "Not found!")
        return result


    @marshal_with(resource_fields)
    def put(self, id):
        if self.get(id):
            abort(409, message='Id is already taken!')

        notes_args = reqparse.RequestParser()
        notes_args.add_argument("title", type=str, help="string title is required" , required=True)
        notes_args.add_argument("note", type=str, help="string note is required" , required=True)
        args = notes_args.parse_args()

        note = NoteModel(id=id, title= args['title'], note = args['note'])
        db.session.add(note)
        db.session.commit()

        return note, 201


    # def delete(self, id):
    #     abort_request(id)
    #     del notes[id]
    #     return 'operation successful!', 204