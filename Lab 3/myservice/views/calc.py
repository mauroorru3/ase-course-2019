from flakon import JsonBlueprint
from flask import Flask, request, jsonify


calc = JsonBlueprint('calc',__name__)




@calc.route('/calc/sum', methods=['GET'])



def sum():
	#http://127.0.0.1:5000/calc/sum?m=3&n=5
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))


	result = m

	if n < 0:
		for i in range(abs(n)):
			result -= 1

	else:
		for i in range(n):
			result += 1


	return jsonify({'result':str(result)})




@calc.route('/calc/substract', methods=['GET'])


def substract():
	#http://127.0.0.1:5000/calc/substract?m=3&n=5
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))
	result = m
	if n < 0:
		for i in range(abs(n)):
			result += 1
	else:
		for i in range(n):
			result -=1
	return jsonify({'result':str(result)})


@calc.route('/calc/divide', methods=['GET'])

def divide():
	#http://127.0.0.1:5000/calc/divide?m=3&n=5
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))
	result = 0
	negativeResult = m > 0 and n < 0 or m < 0 and n > 0
	n = abs(n)
	m = abs(m)



	if n == 0:
		return jsonify({'result':"You cannot divide by 0!"})




	while (m-n) >= 0:
		m -= n
		result += 1

	result = -result if negativeResult else result

	return jsonify({'result':str(result)})




@calc.route('/calc/multiply', methods=['GET'])

def multiply():
	#http://127.0.0.1:5000/calc/multiply?m=3&n=5
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))
	result = 0
	negativeResult = m > 0 and n < 0 or m < 0 and n > 0
	n = abs(n)
	m = abs(m)


	if n == 0 or m == 0:
		return jsonify({'result':str(0)})

	while n > 0:
		result += m
		n -= 1

	result = -result if negativeResult else result

	return jsonify({'result':str(result)})



def divideSupport(m, n):
	result = 0
	negativeResult = m > 0 and n < 0 or m < 0 and n > 0
	n = abs(n)
	m = abs(m)



	if n == 0:
		raise ZeroDivisionError("You cannot divide by 0!")




	while (m-n) >= 0:
		m -= n
		result += 1

	result = -result if negativeResult else result

	return result


def gdcSupport(m,n):
	if m == 0 and n != 0:
		return abs(n)
	elif m != 0 and n == 0:
		return abs(m)
	elif m == 0 and n == 0:
		raise ValueError("At least one number must me different from 0!")
	else:
		return gdcSupport(n, m - ( n * divideSupport(m,n)))


@calc.route('/calc/gdc', methods=['GET'])

def gdc():
	#http://127.0.0.1:5000/calc/gdc?m=3&n=5
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))
	if m == 0 and n != 0:
		return jsonify({'result':str(abs(n))})
	elif m != 0 and n == 0:
		return jsonify({'result':str(abs(m))})
	elif m == 0 and n == 0:
		return jsonify({'result':"At least one number must me different from 0!"})
	else:
		result = gdcSupport(n, m - ( n * divideSupport(m,n)))
		return jsonify({'result':str(result)})

