#Closures
# Es una forma de acceder a variables de otros scopes a 
# través de una nested function. Se retorna la nested function y esta 
# recuerda el valor que imprime, aunque a la hora de 
# ejecutarla no este dentro de su alcance.

def main():
	a = 1
	def nested():
		print(a)
	return nested

my_func = main()
del(main)# se borrra la funcion main y se sigue retornando el valor de a
my_func()

# Reglas para encontrar un Closure

#     Debemos tener una nested function
#     La nested function debe referenciar un valor de un scope superior
#     La función que envuelve a la nested function debe retornarla también
