from flask import Flask, request, jsonify, make_response, abort
import os
from DBManager import DataBase

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)

db = DataBase("notes.db")  # An object for working with DB


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(error="Not found"), 404)

@app.route("/")
def index():  # The main page with jquery enabled for testing api functions
    return "Hello world! <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>"

@app.route("/api/notes", methods=["GET"])
def api_notes():  # List of notes
    notes = db.get_all_notes()
    return jsonify(notes=notes, ok=True)

@app.route("/api/notes/<int:note_id>", methods=["GET"])
def api_note(note_id: int):  # Information about the note
    note = db.get_note_data(note_id)
    if not note is None:
        return jsonify(note=note, ok=True)
    else:
        abort(404)

@app.route("/api/notes/", methods=["POST"])
def api_add_note():  # Creating a new note
    data = request.get_json()
    if not "text" in data or not data["text"]:
        abort(400)
    note_id = db.add_note(data["text"])
    note = db.get_note_data(note_id)
    return jsonify(note=note, ok=True), 201  # code 201 = created

@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def api_delete_note(note_id: int):  # Deleting a note
    note = db.get_note_text(note_id)
    if not note is None:
        db.delete_note(note_id)
        return jsonify(ok=True)
    else:
        abort(404)

@app.route("/api/notes/<int:note_id>", methods=["PUT"])
def api_update_note(note_id: int):  # Updating the text of the note
    data = request.get_json()
    if not "text" in data or not data["text"]:
        abort(400)
    note = db.get_note_data(note_id)
    if not note is None:
        note = list(note)
        db.change_note(note_id, data["text"])
        note[1] = data["text"]
        return jsonify(note=note, ok=True)
    else:
        abort(404)


if __name__ == "__main__":
    app.run("0.0.0.0", port=2020)


"""
// Testing api functions from the browser console.
$.ajax({
	url: '/api/notes',
	data: JSON.stringify({text: "Test note."}),
	type: 'POST',
	success: function(response){
		console.log(response);
	},
	error: function(error){
		console.log(error);
    },
    contentType: "application/json"});
"""