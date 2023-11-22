# 1.Más de 8 carácteres
# 2.Al menos una letra mayúscula X
# 3.Al menos una letra minúscula X
# 4.Al menos un número
# 5.Al menos un carácter especial X
# 6.No tiene espacios en blanco

def verificaLongitud(contraseña): 
  longitud=len(contraseña)
  respuesta=True
  if(longitud<=8):
    respuesta=False
  print("La longitud de la contraseña es "+str(longitud))
  return(respuesta)

def verificaMayusculas(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
   
    if(contraseña[cont].isupper()):
      respuesta=True
      

  return(respuesta)

def verificaMinusculas(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    
    if(contraseña[cont].islower()):
      respuesta=True
      
  return(respuesta)

def verificaNumeros(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont].isnumeric()):
      respuesta=True
  return(respuesta)

def verificaCaracteresExtraños(contraseña):
  respuesta=False
  lista="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
  for cont1 in range(0,len(contraseña)):
    for cont2 in range(0,len(lista)):
      if(contraseña[cont1]==lista[cont2]):
        respuesta=True
  return(respuesta)


def verificaContraseña():
  contraseña=input("Introduce una contraseña: ")
  validez=0 
  if(verificaLongitud(contraseña)==True):
    validez=validez+1
    print("Longitud correcta")
  if(verificaMayusculas(contraseña)==True):
    validez=validez+1
  if(verificaMinusculas(contraseña)==True):
    validez=validez+1
  if(verificaNumeros(contraseña)==True):
    validez=validez+1
  if(verificaCaracteresExtraños(contraseña)==True):
    validez=validez+1
  
  if(validez==5):
    print("Contraseña válida")
  else:
    print("COntraseña inválida")



verificaContraseña()