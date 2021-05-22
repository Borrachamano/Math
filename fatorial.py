def fac(n):
	if n < 0:
		raise ValuError('Numero negativo karai')
	if type(n) == float:
		raise ValueError('Ponto flutuando não mermão.')
	result = 1
	for c in range(0, n):
		result *= n
		n -= 1
	return result

if __name__ == '__main__':
	try:
		f = int(input('Dogite um numero para ver seu fatorial: '))
		r = fac(f)
		print('Resultado', r)
	except:
		raise ValueError('Epa, Epa! Digita um numero inteiro ae!')
	else:
		print('Até mais!')
