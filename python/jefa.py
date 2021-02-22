nombre=input("Ingresa tu nombre: ")
nombre=nombre.capitalize()
nombre=nombre.replace(" ","")
nombre=nombre.replace("0","")
nombre=nombre.replace("1","")
nombre=nombre.replace("2","")
nombre=nombre.replace("3","")
nombre=nombre.replace("4","")
nombre=nombre.replace("5","")
nombre=nombre.replace("6","")
nombre=nombre.replace("7","")
nombre=nombre.replace("8","")
nombre=nombre.replace("9","")
perro=float(input("Teclea un numero: "))
gato=float(input("Teclea otro numero: "))

suma=perro+gato
resta=perro-gato
multiplicacion=perro*gato
division=perro/gato

print("")
print(nombre+", los resultados son: ")
print("Suma: "+str(suma))
print("Resta: "+str(resta))
print("Multiplicacion: "+str(multiplicacion))
print("Division: "+str(division))

# x=1
# y=2
# z=y+x
# z=3