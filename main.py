from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'ok', 'message': 'Hello from CTAG Backend!', 'owner': 'itztankee', 'id': '202b5c6d-fc08-4dfe-a568-88c7b7e063a3'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
