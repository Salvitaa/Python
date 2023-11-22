import secrets
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contraseña = 12  
contraseña_generada = generar_contrasena(longitud_contraseña)

print("Contraseña generada:", contraseña_generada)