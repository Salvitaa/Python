def verificaContraseña():
  contraseña=input("Ingrese una contraseña: ")
  validez=True 
  longitud=len(contraseña)
  cont=0
  if(longitud<=8):
    validez=False
    print("Longitud incorrecta")
  if(contraseña.islower() or contraseña.isupper()):
    validez=False
    print("NO cumple el criterio de contener mayúsculas o minúsculas")
  no_numero=0 
  for cont in range(0,longitud):
    print("El caracter " + str(contraseña[cont]))
    if(contraseña[cont].isnumeric()==False):
       no_numero=no_numero+1
       print(" no es un número")
    else:
      print(" si es un número")
  if(longitud==no_numero):
      validez=False
      print("NO cumple el criterio de contener al menos un número")
  if(validez==True):
    print("Contraseña VÁlIDA")
  else:
    print("Busca otra contraseña")

verificaContraseña()