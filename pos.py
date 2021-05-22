def possitivo(n):
	if n < 0:
		return n - (n * 2)
	print('Esse numero não é negativo.')

def negativo(n):
	if n >= 0:
		return n - (n * 2)
	else:
		print('Esse numero não é possitivo.')

if __name__ == '__main__':
	try:
		print(f'Menu: \n[ 1 ] Possitive\n[ 2 ] Negative\n')
		menu = input('>>> ')
		if menu == '1':
			num = int(input('Digite um numero: '))
			if num < 0:
				r = possitivo(num)
				print('Resultado', r)
		elif menu == '2':
			num = int(input('Digite um numero: '))
			if num > 0:
				r = negativo(num)
				print('Resultado', r)
		else:
			print('Opcao invalida.')
	except:
		raise TypeError('Digite um numero inteiro.')

