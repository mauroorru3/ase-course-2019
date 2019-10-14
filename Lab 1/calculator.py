#calcultator.py

def sum(m,n):
	result = m
	if n < 0:
		for i in range(abs(n)):
			result -= 1
	else:
		for i in range(n):
			result +=1
	return result




def substract(m, n):
	result = m
	if n < 0:
		for i in range(abs(n)):
			result += 1
	else:
		for i in range(n):
			result -=1
	return result



def divide(m, n):
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






def multiply(m, n):
	result = 0
	negativeResult = m > 0 and n < 0 or m < 0 and n > 0
	n = abs(n)
	m = abs(m)


	if n == 0 or m == 0:
		return 0

	while n > 0:
		result += m
		n -= 1

	result = -result if negativeResult else result

	return result


def gdc(m,n):
	if m == 0 and n != 0:
		return abs(n)
	elif m != 0 and n == 0:
		return abs(m)
	elif m == 0 and n == 0:
		raise ValueError("At least one number must me different from 0!")
	else:
		return gdc(n, m - ( n * divide(m,n)))



print(gdc(10,2))