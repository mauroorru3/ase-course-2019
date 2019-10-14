from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/person/<person_id>')
def person(person_id):
	responde = jsonify({'Hello':person_id})
	return response

if __name__=='__main__':
	print(app.url_map)
	app.run()