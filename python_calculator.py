print("\n**********************Python Calculator***************************")

def soma (x, y):
	return x + y
		
def resta (x, y):
	return x - y

def multi (x, y):
	return x * y

def divi (x, y):
	return x / y

print("\nSelecione o número da operação desejada: \n")

print("1. Soma")
print("2. Resta")
print("3. Multiplicação")
print("4. Divisão")

opciom = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if opciom == "1":
	print("\n")
	print(num1, "+", num2, "=", soma(num1, num2))
	print("\n")

elif opciom == "2":
	print("\n")
	print(num1, "-", num2, "=", resta(num1, num2))
	print("\n")

elif opciom == "3":
	print("\n")
	print(num1, "*", num2, "=", multi(num1, num2))
	print("\n")

elif opciom == "4":
	print("\n")
	print(num1, "/", num2, "=", divi(num1, num2))
	print("\n")

else:
	print("\nOpção Inválida!")