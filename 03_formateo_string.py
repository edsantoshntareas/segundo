#Cuando tienes una cadena de caracter, en algunos casos es necesario darle
#formato, porner en mayusculas, minusculas, tipo titulo etc.
#Para realizar dichas operaciones Python tiene opciones que no modifican el
#texto almacenado pero si la forma en que se muestra.

nombre_completo = "eduardo netanel santos paz"

#El texto almacenado en nombre_completo se encuentra en minusculas, siendo
#un nombre propio debe de iniciar cada nombre en mayusculas.
#Para este caso y similares podemos utilizar la funcion title() 
#la cual pone nuestro texto en mayusculas la primer letra de cada palabra

print(nombre_completo.title())



nombre_lugar = "TEXTO EN MAYUSCULAS"

#En este caso el texto se encuentra en mayusculas y es necesario pasarlo a 
#minusculas, eso lo podemos realizar utilizando la funcion lower()

print(nombre_lugar.lower())



nombre_pais = "holanda"

#Es el caso anterior tenemos el nombre de un pais en minusculas, como podemos
#pasarlo a mayusculas, utilizando la funcion upper()

print(nombre_pais.upper())



################################################################################
#Eliminando espacios en blanco

#Muchas de las veces escribimos una cadena de texto con espacios al final
#Python no reconoce lo mismo una cadena de caracter sin espacios al final
#y otra que tenga espacios al final, aunque digan lo mismo
#El espacio de almacenamiento es mayor si se guardan espacios en ambos lados
#o almenos en alguno de los lados (derecha o izquierda)

texto_espacio_derecho = "Texto con espacio derecha     "
print(texto_espacio_derecho)
print(texto_espacio_derecho.rstrip())

#La linea anterior muestra el texto sin espacios a la derecha
#podemos hacer lo mismo para almacenarla

texto_sin_espacio_derecho = texto_espacio_derecho.rstrip()

#De esta forma al imprimir texto_sin_espacio_derecho se imprimira sin espacios
#no siempre es necesario crear una nueva variable.

print(texto_sin_espacio_derecho)

#El codigo anterior muestra el texto almacenado



texto_espacio_izquierdo = "      Texto con espacios izquierda"
print(texto_espacio_izquierdo)
print(texto_espacio_izquierdo.lstrip())

#La linea anterior muestra el texto sin espacios a la izquierda
#podemos hacer lo mismo para almacenarla

texto_sin_espacio_izquierdo = texto_espacio_izquierdo.lstrip()

#De esta forma al imprimir texto_sin_espacio_izquierdo se imprimira sin espacios
#no siempre es necesario crear una nueva variable.

print(texto_sin_espacio_izquierdo)

#El codigo anterior muestra el texto almacenado


#En las lineas anteriores aprendimos como limpiar el texto de espacios en blanco
#tanto a la derecha (rstrip()) como a la izquierda (lstrip())
#pero como saber donde dejo el usuario o nosotros el espacio en blanco
#realizar dos procedimientos o funciones para asegurarnos no es adecuado
#utilizando una funcion mas simple podemos lograrlo, la funcion strip()
#elimina los espacios en blanco en ambos lados, utilizaremos las variables


print(texto_espacio_derecho)
print(texto_espacio_derecho.strip())


print(texto_espacio_izquierdo)
print(texto_espacio_izquierdo.strip())


texto_espacios_ambos_lados = "           Texto con espacios         "

print(texto_espacios_ambos_lados)
print(texto_espacios_ambos_lados.strip())

#De esta forma limpiamos o elimanos los espacios innecesarios a ambos lados
#no nos interesa donde el usuario o nosotros dejamos el espacio en blanco.



###############################################################################
#Concatenar cadenas de caracter

#imaginate que debes de saludar al usuario del sistema por nombre,
#es imposible que siempre conozcas el nombre del usuario
#por otro lado si tienes 100 usuarios, escribir 100 lineas saludando
#seria ridiculo, eso lo podemos solventar concatenando el saludos y el nombre

saludo_nombre_completo = "Saludo " + nombre_completo.title()
print(saludo_nombre_completo)
#debemos de dejar el espacio a la derecha, para que la salida de datos sea
#Saludo Eduardo y no SaludoEduardo


#Para concatenar un numero con texto primero debemos de Convertirlo el numero
#a una cadena de caracteres Esto solo es momentaneo, o si lo almacenamos en
#otra variable puede ser permanente

soy_numero_uno = 54125
soy_texto_numero_uno = str(soy_numero_uno)

#La funcion str() nos sirve para convertir un numero en texto
# soy_numero_uno = 54125 pero la segunga soy_texto_numero_uno = "54125"
#Se puede notar la diferencia de ambas variables, 
#si las tratamos de imprimir, no existira diferencia visual

print(soy_numero_uno)

print(soy_texto_numero_uno)

###vamos a concatenar un numero con texto

presentacion = "Hola, mi nombre es " + nombre_completo.title() + " y tengo " + \
                soy_texto_numero_uno

print(presentacion)


#no es necesario convertir el numero en texto y luego almacenarlo, podemos
#convertirlo directamente en la setencia y de esa forma ahorrar memoria

presentacion_2 = "Hola, mi nombre es " + nombre_completo.title() + " y tengo "\
                 + str(soy_numero_uno)

#Si no agregamos el str() nos daria un error de sintaxis 

