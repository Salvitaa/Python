def suma_cifras():

  suma=0
  numero=input("Introduce un número: ")

  for cont in range(0,len(numero)):
    suma=suma+int(numero[cont])

  print("La suma vale= "+str(suma))


suma_cifras()