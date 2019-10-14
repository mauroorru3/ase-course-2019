from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/auth')
def auth():
	json_data = request.get_json()
	email = json_data['email']
	password = json_data['password']
	return jsonify({'email':email})


if __name__=='__main__':
	app.run()



