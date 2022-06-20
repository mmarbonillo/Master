# Desarrolla un script en Python que abra un fichero de texto ‘.txt’. 
# Escribe unas cuantas líneas en el fichero y finalmente muestra el contenido de dicho fichero por pantalla.


# CREO EL FICHERO Y LO ABRO EN MODO LECTURA Y ESCRITURA AL FINAL DEL ARCHIVO (AÑADIR)
fich = open('fichero.txt', 'a+')

# CREO EL TEXTO A AÑADIR Y LO ESCRIBO EN EL FICHERO
texto = "Línea 1\nLínea 2\nLínea 3\n"
fich.write(texto)

# POSICIONO EL CURSOR DEL ARCHIVO AL PRINCIPIO DEL MISMO PARA PODER LEERLO
# YA QUE TRAS ESCRIBIR, ESTE SE QUEDA AL FINAL DEL ARCHIVO
fich.seek(0)

# LEO EL FICHERO Y MUESTRO POR PANTALLA EL RESULTADO
print(fich.read())


# OTRA FORMA DE HACER LO MISMO

fich2 = open('fichero2.txt', 'a+')
texto = ['Línea 1\n', 'Línea 2\n', 'Línea 3\n']

fich2.writelines(texto)

fich2.seek(0)

print(fich2.read())