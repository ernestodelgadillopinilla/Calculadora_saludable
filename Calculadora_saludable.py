# "CALCULADORA SALUDABLE"
# Estudiante: Ernesto Delgadillo
def peso_ideal(genero,altura):
	if genero=='H':
		IBW=56.2 + 1.41 * (altura / 2.54 - 60)
		return IBW
	elif genero=='M':
		IBW=53.1 + 1.41 * (altura / 2.54 - 60)
		return IBW	

def calorias(tiempo,peso,MET):
	quemadas=(tiempo * peso * MET)/200
	return quemadas
"""MET:
- Caminar= 2
- Tenis= 5
- Montar en bicicleta= 14
- Correr= 6
- Nadar= 9.8"""

def grasa_corporal(genero,edad, peso,altura):
    imc=peso/(altura/100)**2
    if genero=='H':	
        GPC= 1.20 * (imc + 0.23) * edad - 16.2
        return GPC
    elif genero== 'M':
        GPC= 1.20 * (imc + 0.23) * edad - 5.4
        return GPC

def indice_metabolico_corporal(peso,altura,edad):
	if genero=='H':
		IMB= (13.397 * peso) + (4.799 * edad) - (5.677 * altura) + 88.362
		return IMB
	elif genero=='M':
		IMB= (9.247 * peso) + (3.098 * edad) - (4.330 * altura) + 447.593
		return IMB	
	

opcion = 0

while(opcion !=5):
	print("---BIENVENIDO A SU CALCULADORA SALUDABLE---\n")
	print("Que operación deseas realizar?")
	print("-------------------------------------------")
	print("1. Conocer su peso ideal")
	print("2. Conocer cantidad de calorias quemadas")
	print("3. Conocer su porsentaje de grasa corporal")
	print("4. Conocer su índice metabólico basal")
	print("5. salir")
	print("-------------------------------------------")

	opcion = int(input("Por favor seleccione una opción:"))

	if opcion == 1:
		genero=(input("Eres Hombre(H) o mujer(M)? "))
		altura=float(input("Ingrese su altura(cm): "))
		resultado_peso_ideal= peso_ideal(genero,altura)
		print("****Su peso ideal debería ser de: ", resultado_peso_ideal, "Kg****\n")
	elif opcion == 2:
		peso=float(input("Ingrese su peso(kg): "))
		print("")
		print("-caminar= 2   -Tenis= 5   -Montar en bicicleta= 14   -Correr= 6  -Nadar= 9.8")
		MET=float(input("Ingrese la opción segun el ejercicio realizado: "))
		tiempo=float(input("Ingrese su tiempo(min): "))
		calorias_quemadas= calorias(tiempo,peso,MET)
		print("****Sus calorías quemadas es de: ", calorias_quemadas,"****\n")
	elif opcion == 3:
		genero=(input("Eres Hombre(H) o mujer(M)? "))
		peso=float(input("Ingrese su peso(kg): "))
		altura=float(input("Ingrese su altura(cm): "))
		edad=float(input("Ingrese su edad(años): "))
		resultado_grasa_corporal=grasa_corporal(genero,edad, peso,altura)
		print("****Su porcentaje de grasa corporal es: ", resultado_grasa_corporal,"****\n")
	elif opcion == 4:
		peso=float(input("Ingrese su peso(kg): "))
		altura=float(input("Ingrese su altura(cm): "))
		edad=float(input("Ingrese su edad(años): "))
		genero=(input("Eres Hombre(H) o mujer(M)? "))
		resultado_IMB= indice_metabolico_corporal(peso,altura,edad,)
		print("****Su indice metabólico basal es: ", resultado_IMB,"****\n")
	elif opcion == 5:
		print("***SALIENDO DE LA CALCULADORA***")
	else:
		print("****Por favor ingrese una opcion válida**** \n")