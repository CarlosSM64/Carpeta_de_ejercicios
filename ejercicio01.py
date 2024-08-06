# Cuatro enteros entre 0 y 100 representan las puntuaciones de un estudiante de un curso de informática. 
# Escribir un programa para encontrar 
# la media de estas puntuaciones 
# y visualizar una tabla de notas de acuerdo al siguiente cuadro:

primero = int(input("Ingrese primer valor: "))
segundo = int(input("Ingrese segundo valor: "))
tercero = int(input("Ingrese tercera valor: "))
cuarto =  int(input("Ingrese cuarto valor: "))

media = (primero + segundo + tercero + cuarto)/4
print("la media es: ", float(media))

if media>=90:
    print("Calificación: A")
elif media>=80:
    print("Calificación: B")
elif media>=70:
    print("Calificación: C")
elif media>=60:
    print("Calificación: D")
elif media>=0:
    print("Calificación: E")