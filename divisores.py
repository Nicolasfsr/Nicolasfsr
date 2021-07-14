numero  = 15
divisores_del_numero = []
numero_a_dividi = 1
while numero_a_dividi<= numero:
	numero_total = (numero% numero_a_dividi)
	if numero_total == 0:
		divisores_del_numero.append(numero_a_dividi)
	numero_a_dividi = numero_a_dividi + 1
	
print(divisores_del_numero)