print("SISTEMA DE COBRO DE LA SALA DE JUEGOS")

turno = "next"

while turno.lower() == "next":
    total_pagar = 0
    cantidad_personas = 0
    continuar_grupo = "si"

    while continuar_grupo.lower() == "si":
        edad = int(input("Ingrese la edad de la persona: "))
        
        if edad < 5:
            precio = 0
            print("-> Entrada gratis ($0)")
        elif edad <= 18:
            precio = 5
            print("-> Precio de la entrada: $5")
        else:
            precio = 10
            print("-> Precio de la entrada: $10")
            
        total_pagar = total_pagar + precio
        cantidad_personas = cantidad_personas + 1
        
        continuar_grupo = input("¿Hay otra persona en este grupo? (si/no): ")

    print("             RESUMEN DE COBRO             ")
    print(f"Total de personas ingresadas: {cantidad_personas}")
    print(f"Total a pagar en conjunto: ${total_pagar}")
    
    turno = input("\nEscribe 'next' para seguir con el siguiente cliente o cualquier tecla para salir: ")

print("\n¡Gracias usar nuestro sistema!")