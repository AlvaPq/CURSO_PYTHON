#las variables nos sirven para guardar datos en memoria
#python es un lenguaje de tipado dinamico y de tipado fuerte



#Asignar una variable 

my_name = "alvaro"
print(my_name)


#las variables pueden ser reasignadas en tiempo de ejecucion
age = 23
print(age)

age = 40
print(age)

#tipado dinamico
#el tipado de dato se determina en tiempo de ejecucion es decir 
#no hace falta ser ecplicito al declarlo

name = "alvapq"
print(type(name))

#tipado fuerte, en python no se realiza conversiones de tipos atumaticas

#f-string  (literal  de cadena formato)

print(f"Holan {name}, tengo {age} años")

#no es recomendable esta forma de asignar variables

name, age, city = "Alva", 23, "Lima"

#convenciones de nombres de variables
#normalmente se usa snake_case
mi_nombre_variable = "ok"

#si vemos mayusculas relacionarlo a una constante
MI_CONSTANTE = 3.14   # UPPER_CASE -> constantes( es decir no deberia de cambiar)

#en Python hay palabras reservadas que no pueden ser usadas como variables
#ya que forman parte del diccionario de python
is_user_logged_in: bool = True
print(is_user_logged_in)





