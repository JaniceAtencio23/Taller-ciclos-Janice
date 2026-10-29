secreto = 7
intento = int(input("aadivina el número (1 al 10): "))
 
while intento != secreto:
    if intento < secreto:
        print("muy bajo")
    else:
        print("muy alto")
    intento = int(input("intenta de nuevo: "))
 
print("¡acertastee!")
