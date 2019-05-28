#Las listas unidimensionales nos permiten almacenar informacion no relaciona
#entre si, ni es obligatorio tener el mismo tipo de datos en la lista
#La lista tiene un indice o index, que inicia a contar desde cero y no de uno
#las listas deben de se nombradas en plural y no singular ejemplo
#estudiantes y no estudiante, nombres y no nombre, registros y no registro
#se aplican igualmente las normativas para variables

#crearemos una lista llamada registros, la cual estara vacia
registros = []


#crearemos ahora una lista con nombre de estudiantes
nombres_estudiantes = ["Luis", "Carlos", "Melissa", "Mary", "Pamela", "Rosa"]
#Los inidices son asi> [0,     1,         2,         3,      4,       5     ]




#Para acceder a los datos de una lista unidimensional debemos de utilizar
#la siguiente estructura, el valor entre los corchetes es el numero de indice
print(nombres_estudiantes[3])
#El valor devuelto o impreso es Mary

#Se puede utilizar la siguiente forma
print(nombres_estudiantes)
#Esto devolveria ["Luis", "Carlos", "Melissa", "Mary", "Pamela", "Rosa"] lo cual
#no es adecuado para mostrar a nuestros usuarios

#Si queremos imprimir todos los registros de la lista debemos de utilizar
#la estructura adecuada imprimiendo uno a uno
print(nombres_estudiantes[0])
print(nombres_estudiantes[1])
print(nombres_estudiantes[2])
print(nombres_estudiantes[3])
print(nombres_estudiantes[4])
print(nombres_estudiantes[5])


#Existe otra forma un poco mas sencilla de imprimir todos los registros de la 
#lista sin necesidad de conocer cuantos registros tiene la lista
#esto lo veremos mas adelante


#Podemos cambiar el valor almacenado en un indice de la siguiente forma
nombres_estudiantes[0] = "Eduardo"
print(nombres_estudiantes[0])


#Podemos utilizar los formatos de cadenas de caracter para imprimir los datos
print(nombres_estudiantes[0].upper())
print(nombres_estudiantes[0].lower())
print(nombres_estudiantes[0].title())



#Insertar registros en la lista
#Existen diferentes formas para insertar registros dentro de una lista
#La primera que veremos sera append() que inserta el nuevo valor al final de la
#lista 

nombres_estudiantes.append("Edgardo")
#Sabiendo que el utilimo registro se encuentra en el indice 5 el nuevo toma el 6

print(nombres_estudiantes[6])


#si necesiamos insertar un registro en un indice especifico podemos hacerlo
#de la sigueinte forma, no es lo mismo que reasignar... sino inserta 
#un nuevo registro. ejemplo tengo 5 registros quiero insertar en el 4
#el registro anteriormente 4 pasa a ser el 5 y asi susecibamente

nombres_estudiantes.insert(4, "Alfredo")



#Eliminar registros de una lista unidimesional
#Eliminar un registro especifico
del nombres_estudiantes[0]
#El codigo anterior elimina el primer registro de la lista, pero podemos
#utilizarla para eliminar cualquier registro que desees, solo debes de poner
#el indice entre los corchetes y la funcion eliminara dicho registro


#Eliminar utilizando la funcion o metodo pop() de la lista
nombres_estudiantes.pop()

#Con pop() tambien puedes eliminar el registro que desees pasando el numero
#de indice entre los parentesis

nombres_estudiantes.pop(0)
#El codigo anterior elimina el primer registro

#Eliminar el registro por el contenido y no por el indice
#imaginate que quieres eliminar todos los registros que sean "Eduardo"
#Hasta el momento no hay ningun Eduardo en la lista, por lo que procedemos a
#agregar nuevos registros
nombres_estudiantes.append("Eduardo")
nombres_estudiantes.append("Eduardo")
nombres_estudiantes.append("Eduardo")
nombres_estudiantes.append("Eduardo")
nombres_estudiantes.insert(1, "Eduardo")
nombres_estudiantes.insert(1, "Eduardo")
nombres_estudiantes.insert(1, "Eduardo")
nombres_estudiantes.insert(1, "Eduardo")

#Hemos agregado ocho registros que se llaman Eduardo
#Utilizando la funcion o metodo remove() podemos eliminar todos los elementos 
#llamados Eduardo

nombres_estudiantes.remove("Eduardo")



################################################################################
#Ordenamiento de listas unidimensionales

#Ordenamiento permanente con la funcion o metodo sort()
nombres_estudiantes_ordenado = nombres_estudiantes.sort()

print(nombres_estudiantes_ordenado)

#El codigo anterior crea una listaordenara de forma permanente los datos
#de la lista, en orden de A - Z o de 0 - infinito
#Esto es permanente y no podemos reversar dicho procedimiento

#Que pasa si queremos ordenar la lista de Z - A o de Infinito - 0
#Facil solo debemos de pasar un parametro a la funcion sort, el parametro
#reverse = True
nombres_estudiantes_contrario = nombres_estudiantes.sort(reverse = True)
print(nombres_estudiantes_contrario)


#Ordenamiento temporal de una lista para ser impreso  A - Z
print(sorted(nombres_estudiantes))


#Imprimir una lista temporalmente con el ordenamiento al reves Z - A
print(nombres_estudiantes.reverse())



################################################################################
#Tamanio de la Lista
#Es necesario muchas veces saber la cantidad de registros que tiene una lista
#para eso podemos utilizar el funcion len() entre parentesis pasamos el nombre
#de la lista que deseamos sabes su tamanio

print(len(nombres_estudiantes))

