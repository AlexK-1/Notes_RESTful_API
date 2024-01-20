# Notes_RESTful_API
RESTful API for a simple note-taking application

## Structure
The API is located at the relative address `api/`. To work with notes use the address `api/notes`.

To get a list of all the notes, go to `api/notes`. The `GET` request.

To get the data of one specific note, go to the address `api/notes/[note_id]`, where `note_id` is the number (id) of the note in the SQLite database. The `GET` request

To create a new note, you need to send a `POST` request to the address `api/notes` with the `text` parameter in the request body. A note with the text you specified will be created in the database. The data of the new note in the `note` key will be transmitted from the server.

To delete a note, send a `DELETE` request to the page at `api/notes/[note_id]`, where `note_id` is the id of the note to be deleted.

To edit the text of a note, you need to send a `PUT` request to the page at `api/notes/[note_id]`, where `note_id` is the id of the note to be changed. In the body of the `PUT` request, the `text` parameter should contain the new text of the note.

## Testing
To test the `GET` request, it is enough to open a page with the desired address, for example, `api/notes`. To test `POST`, `PUT` and `DELETE` API requests, I ran the following code on the API homepage in the browser console:
```js
$.ajax({
	url: '/api/notes',
	data: JSON.stringify({text: "Test note."}), // in the stringify function, an object with query parameters
                                                  // (only the text parameter for creating and modifying a note)
	type: 'POST', // The request method is in quotes here
	success: function(response){
		console.log(response);
	},
	error: function(error){
		console.log(error);
    },
    contentType: "application/json"});
```
