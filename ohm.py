
"""
Programa para calcular la Ley de Ohm
Opciones:
1. Calcular Voltaje
2. Calcular Corriente
3. Calcular Resistencia
"""
print("Ley de Ohm")
print("Selecciona la opción:")
print("1 = Voltaje\n2 = corriente\n3 = Resistencia")
opcion = int(input("Opción: "))

try:
    if opcion == 1:
        resistencia = float(input("Ingresa la resistencia (Ohm): "))
        corriente = float(input("Ingresa la corriente (Amperios): "))
        voltaje = resistencia * corriente
        print("El voltaje es:", voltaje, "Voltios")
    elif opcion == 2:
        voltaje = float(input("Ingresa el voltaje (Voltios): "))
        resistencia = float(input("Ingresa la resistencia (Ohm): "))
        if resistencia == 0:
            print("Error: La resistencia no puede ser cero.")
        else:
            corriente = voltaje / resistencia
            print("La corriente es:", corriente, "Amperios")
    elif opcion == 3:
        voltaje = float(input("Ingresa el voltaje (Voltios): "))
        corriente = float(input("Ingresa la corriente (Amperios): "))
        if corriente == 0:
            print("Error: La corriente no puede ser cero.")
        else:
            resistencia = voltaje / corriente
            print("La resistencia es:", resistencia, "Ohm")
    else:
        print("Opción no válida.")
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")