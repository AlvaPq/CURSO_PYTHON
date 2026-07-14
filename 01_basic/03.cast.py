#casting de types
# trasnsformar un tipo de valor a otro
#aqui en python no se redondea de la manera convecional sino q busca al par mas cercano es decir
#si tenemos 2.5 redondera a 2 y no a 3 pero si tenemos 3.5 redondeara a 4


print("conertir tipos")

print(2+ int("100"))
#a diferencia del primero no hace la suma como tal lo q hace es agregar el dos al texto 100 
print("100" + str(2))


print(type(float(3.1416)))

print(bool(3))
print(bool(0))
print(bool(-1))
#en que si esta vacio se considera false
print(bool(""))
#pero si le pones un espacio en blanco ya se considera que hay algo y te dara true
print(bool(" "))
print(bool("False"))

