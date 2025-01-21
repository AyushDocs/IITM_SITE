# api/index.py
import json
from http.server import BaseHTTPRequestHandler
import os
from urllib.parse import urlparse, parse_qs

def load_data():
    with open(os.path.join('data','q-vercel-python.json')) as f:
        return json.load(f)
data=load_data()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_params = parse_qs(urlparse(self.path).query)
        names = query_params.get('names', [])
        names = [name[0] for name in names]
        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({ "marks": [d for d in data if data['name'] in names] }).encode('utf-8'))
        return