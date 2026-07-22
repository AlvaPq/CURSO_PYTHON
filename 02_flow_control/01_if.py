#sentencias condicionales (if, elif, else)
import subprocess

subprocess.run(["cmd", "/c", "cls"])

print("\n Sentencia simple")

edad = 17
if edad >= 18:
 print("Eres mayor de edad")

print("\n Sentencia simple")

edad = 17
if edad >= 18:
 print("Eres mayor de edad")
else :
 print("Eres menor de edad")
 print("\n Sentencia de condicional elif")
 nota = 17

 if nota >= 19:
  print("Sobresaliente")
 elif nota >= 17:
  print("Bueno")
 elif nota >= 13:
  print("Aprobaste")
 else :
  print("Ya perdiste ps causa")

  #operadores logicos

print("\n sentencias condicionales multiples")
age = 25
tiene_carnet = True
  
if age >= 18 and tiene_carnet:
 print("si tienes permiso de conducir")
else:
 print("Policiaaaaa")