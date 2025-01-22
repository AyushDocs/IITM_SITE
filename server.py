# api/index.py
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_data():
    with open(os.path.join('data', 'q-vercel-python.json')) as f:
        return json.load(f)

data = load_data()

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [d['marks'] for d in data if d['name'] in names]
    return jsonify({"marks": ' '.join(marks)})

if __name__ == '__main__':
    app.run(debug=True)
