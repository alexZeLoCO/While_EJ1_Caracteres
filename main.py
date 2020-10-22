caracter = str("letra")     #INICIALIZAMOS VARIABLE CARACTER
            #STR CON VALOR DIFERENTE DE "."
contador = 0        #INCIALIZAMOS VARIABLE CONTADOR EN 0

def Contador (caracter, contador):      #SUBRUTINA CONTADOR
        #RECIBE PARÁMETROS CARACTER Y CONTADOR
    if caracter == "a":     #SI CARACTER == A
        contador = contador + 1     #ACTUALIZAR VALOR DE CONTADOR
    return contador     #DEVOLVER VALOR NUEVO DE CONTADOR

print ("Introduzca letras, el bucle finalizará cuando se introduzca un .")      #GUÍA USUARIO
print ("El programa contará las veces que se introdujo el valor 'a'.")          #GUÍA USUARIO

while (caracter != "."):        #MIENTRAS CARACTER SEA DIFERENTE DE .
    contador = Contador(caracter, contador)     #ACTUALIZAR VALOR DE CONTADOR CON LO QUE DEVUELVA SUBRUTINA
    caracter = input ("Introduzca una letra:")      #SOLICITA VALOR

print ("Se han introducido",contador,"veces la a.")     #OUTPUT
