def fibonacci():
	resultado = [0]
	if n == 0: 
		return print(resultado)

	resultado.append(1)
	actual = 1
	anterior = 0
	suma = 0
	i = 1

	while i < n:
		   suma=actual+anterior
		   anterior=actual
		   actual=suma
		   resultado.append(suma)
		   i=i+1

	print(resultado)

if __name__ == '__main__':
	n = int(input("Serie de Fibonachi, ¿número de términos?: "))
	fibonacci()