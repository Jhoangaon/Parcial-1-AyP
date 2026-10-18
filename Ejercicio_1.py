print("MENÚ DE COSITAS RICAS")
print("1. Hamburguesa - $18000")
print("2. Perro caliente - $14000")
print("3. Salchipapa - $15000")
print("4. Gaseosa - $4500")
print("5. Empanadas - $2500")

total = 0
continuar = "si"

while continuar == "si":
    pedido = input("\nDigite el número del plato que desea: ")
    
    if pedido == "1":
        total = total + 18000
        print("¡Agregaste una Hamburguesa!")
    elif pedido == "2":
        total = total + 14000
        print("¡Agregaste un Perro caliente!")
    elif pedido == "3":
        total = total + 15000
        print("¡Agregaste una Salchipapa!")
    elif pedido == "4":
        total = total + 4500
        print("¡Agregaste una Gaseosa!")
    elif pedido == "5":
        total = total + 2500
        print("¡Agregaste Empanadas!")
    else:
        print("Mil disculpas no tenemos pero pronto, lo que desee el cliente.")
        
    continuar = input("¿Desea pedir algo más? (si/no): ")

print("El total a pagar es: $", total)
print("¡Gracias por su compra!")