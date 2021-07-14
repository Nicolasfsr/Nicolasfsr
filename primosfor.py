

def esPrimo(numero):
	divisores_del_numero = []
	numero_a_dividi = 1
	while numero_a_dividi<= numero:
		numero_total = (numero% numero_a_dividi)
		if numero_total == 0:
			divisores_del_numero.append(numero_a_dividi)
		numero_a_dividi = numero_a_dividi + 1
	#print(numero, 'es un numero primo?')
	tamano = len(divisores_del_numero)
	#nm.type()(
	return tamano <= 2
		
def lista():
	lista= range(1001)
	lp = []
	r = len(lista)
	for i in lista:
		resultado = esPrimo(lista[i])
		if resultado:
			lp.append(lista[i])
	print(lp)
lista()