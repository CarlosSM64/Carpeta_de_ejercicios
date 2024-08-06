# Escribir un programa que lea la hora de un día de notación de 24 horas y la respuesta en notación de 12 horas. 
# Por ejemplo, si la entrada es 13:45, la salida será: 1:45 PM
import time
valoren24H = input("Ingrese la hora: ")
hora = time.strptime(valoren24H, "%H:%M")
valoren12H = time.strftime( "%I:%M %p", hora)
print(valoren12H)