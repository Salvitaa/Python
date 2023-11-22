def factorial(f):
  if f == 0 or f == 1:
      return 1
  else:
      return f * factorial(f - 1)
    
resultado = factorial(4)
print(resultado)