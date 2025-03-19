# import modules
from flask import Flask, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['notes']
collection = db['notes']
# API endpoint to create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({'message': 'Note created successfully'}), 201
# API endpoint to retrieve all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = collection.find()
    return jsonify([{'title': note['title'], 'content': note['content']} for note in notes]), 200
if __name__ == '__main__':
    app.run(debug=True)
