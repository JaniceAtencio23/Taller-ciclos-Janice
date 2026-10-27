suma= 0 
for i in range(3):
    nota= float(input("ingresa una nota: "))
    suma+= nota
    promedio = suma/3
    print("tu promedio es:", promedio)

    if promedio>=3:
        print("aprobaste")
    else: print ("Reprobaste ")
    