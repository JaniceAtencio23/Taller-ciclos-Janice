sumaa = 0
cantidad = 0
nota = float(input("Nota (-1 para terminar): "))
 
while nota != -1:
    sumaa += nota
    cantidad += 1
    nota = float(input("Nota (-1 para terminar): "))
 
if cantidad > 0:
    print("Promedio:", sumaa / cantidad)
else:
    print("No ingresaste notas")

