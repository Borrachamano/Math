def po(base, expoente):
	result = 1
	for c in range(0, expoente):
		result *= base
	return result

if __name__ == '__main__':
	try:
		b = int(input('Base: '))
		e = int(input('Expoente: '))
		r = po(b, e)
		print('Resultado', r)
	except:
		print('Error.')

