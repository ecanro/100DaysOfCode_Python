# Escribe un programa en Python que pida al usuario el valor del radio de un círculo, luego
# calcule y muestre el valor del área, el diámetro y la circunferencia.

# pedimos el radio como numero flotante
radio = float(input("Ingrese el valor del radio del circulo: "))
print("El radio del circulo es:", radio)

# calculamos el diametro segun su formula
diametro = radio * 2
print("El diametro del circulo es:", diametro)

# calculamos la circunferencia usando el valor de pi estatico solo com dos decimales, formula
circunferencia = 3.14 * diametro
print(f"La circunferencia del circulo es: {circunferencia}")