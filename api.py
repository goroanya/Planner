from flask import Flask, jsonify,  make_response, request
from flask_restful import abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from planner import Planner


auth = HTTPBasicAuth()
app = Flask(__name__)

planner = Planner('data.json')

users = {
    "goroanya": generate_password_hash("python"),
    "lazygirl": generate_password_hash("python"),
    "gorartem": generate_password_hash("python")
}


def abort_if_resourse_doesnt_exist(date):
    if planner.get(date) is None:
        abort(404)

# auth
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

# error handlars
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def add_existing_resourse(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

# app routes
@app.route('/planner/api/v1.0/', methods=['GET'])
@auth.login_required
def print_hello():
    return jsonify({'message': "Hello, world!"})


@app.route('/planner/api/v1.0/notes', methods=['GET'])
@auth.login_required
def get_notes():
    return jsonify({'notes': planner.getAll()})


@app.route('/planner/api/v1.0/notes/<string:date>', methods=['GET'])
@auth.login_required
def get_note(date):
    abort_if_resourse_doesnt_exist(date)
    return jsonify({date: planner.get(date)})


@app.route('/planner/api/v1.0/notes', methods=['POST'])
@auth.login_required
def create_note():
    if not request.json or not 'note' in request.json or not 'date' in request.json:
        abort(400)

    date = request.json['date']
    note = request.json['note']

    if planner.add(date, note) is False:
        return make_response(jsonify({'error': 'Adding existing resourse'}), 400)
    else:
        return jsonify({date: note}), 201


@app.route('/planner/api/v1.0/notes/<string:date>', methods=['PUT'])
@auth.login_required
def update_note(date):
    if not request.json or not 'note' in request.json or type(request.json['note']) != str:
        abort(400)

    if planner.update(date, request.json['note']) is True:
        return jsonify({'updated': {date: planner.get(date)}})
    else:
        return make_response(jsonify({'error': 'Updating non-existing resourse'}), 400)


@app.route('/planner/api/v1.0/notes/<string:date>', methods=['DELETE'])
@auth.login_required
def delete_note(date):
    if planner.delete(date) is False:
        abort(404)
    else:
        return jsonify({'deleted': True})


if __name__ == '__main__':
    app.run(debug=True)

# root url:  http://127.0.0.1:5000/planner/api/v1.0/
"""
bash: $ curl -i -u username:password -X [METHOD]  -d [DATA] [URL]
METHODS: GET, PUT, DELETE, POST
POSSIBLE URL:
        http://127.0.0.1:5000/planner/api/v1.0/
        http://127.0.0.1:5000/planner/api/v1.0/notes
        http://127.0.0.1:5000/planner/api/v1.0/notes/<string:date>
POSSIBLE DATA : '{"note":"something, "date":"something"}', '{"note":"something"}'   

"""