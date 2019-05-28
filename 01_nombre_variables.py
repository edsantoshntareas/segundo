#Los nombres de las variables en python solo pueden contener letras menores
#no se permiten espacios en blanco, para evitar problemas de lectura se pueden
#utilizar guiones bajos, tampoco puede iniciar con numeros, pero si pueden
#ser utilizados al final.

#Este es el ejemplo clasico en el mundo de la programacion
#Sin variable, debemos poner la cadena de caracter dentro de comillas
print("Hola Mundo!")


#Utilizando el mismo ejemplo anterior solo que seria con una variable
#El nombre de la variable sera saludo
#En este caso el programa imprime el valor o el contenido de la variable saludo
saludo = "Hola Mundo!"
print(saludo)


#Las variables pueden reasingar o cambiar el valor o contenido de la misma
#Primer valor
saludos = "Hola como estas"
print(saludos)

#Segundo valor
saludos = "Deseo que todo este bien!!"
print(saludos)


#Variables con numeros
nombre_1 = "Eduardo"
nombre_2 = "Netanel"
print(nombre_1, nombre_2)

#Errores de estilo
#No se estan permtidas las variables con los numeros pegados al texto, PEP8
#No genera un error de interpretacion, de sintaxis o logico, es puramente estilo
nombre1 = "Mary"
apellido1 = "Desconocido"

#Para corregir dicho error de estilo podmeos utilizar los siguientes ejemplos
primer_nombre = "Mary"
primer_apellido = "Desconocido"

#No recomendado; pero entendible
nombre_1 = "Mary"
apellido_1 = "Desconocido"


