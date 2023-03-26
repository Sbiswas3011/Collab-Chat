from flask import Flask, jsonify, request
from flask_cors import CORS
import BE

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# define a simple route
@app.route('/', methods=['GET'])
def get_all():
    result = BE.GetAccounts()
    return jsonify(result)

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    result = BE.VerifyAccount(data['username'],data['password'])
    return jsonify(result)

# define a route that accepts POST requests
@app.route('/set', methods=['POST'])
def api():
    data = request.get_json()
    BE.SetAccount(data.name,data.password,data.email,data.phno)
    return jsonify("Passed")

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=3000)