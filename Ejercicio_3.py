print("MÁQUINA EMPACADORA DE ARROZ")

numero_lote = 1
bolsas_en_stock = 2 
maquina_encendida = "si"

while maquina_encendida.lower() == "si":
    print(f"\n         PROCESANDO LOTE N° {numero_lote}")
    
    caja = {
        "lote": numero_lote,
        "capacidad_maxima": 4,
        "bolsas": [],        
    }
    
    while len(caja["bolsas"]) < caja["capacidad_maxima"]:
        print(f"\nEstado actual de la caja: {len(caja['bolsas'])}/{caja['capacidad_maxima']} bolsas")
        print(f"Bolsas disponibles en el depósito de la máquina: {bolsas_en_stock}")
        
        if bolsas_en_stock <= 0:
            print("ATENCION: Se han acabado las bolsas en el depósito")
            rellenar = input("¿Desea rellenar el depósito con más bolsas? (si/no): ")
            if rellenar.lower() == "si":
                cantidad_nueva = int(input("¿Cuántas bolsas quiere agregar al depósito?: "))
                bolsas_en_stock = cantidad_nueva
                print(f"El deposito ha sido rellenado,ahora hay {bolsas_en_stock} bolsas.")
            else:
                print("La máquina no puede continuar sin bolsas.")
                maquina_encendida = "no"
                break

        if bolsas_en_stock > 0:
            print("1. Verificando bolsa......,Bolsa detectada")
            print("2. Vaciando arroz en la bolsa...")
            print("3. Sellando la bolsa...")
            
            bolsas_en_stock -= 1
            caja["bolsas"].append(f"Bolsa de arroz #{len(caja['bolsas']) + 1}")
            
            print("4. La bolsa ha sido empacada")
            
        if len(caja["bolsas"]) < caja["capacidad_maxima"] and maquina_encendida.lower() == "si":
            maquina_encendida = input("¿La máquina sigue en funcionamiento? (si/no): ")
            if maquina_encendida.lower() != "si":
                break

    if len(caja["bolsas"]) == caja["capacidad_maxima"]:
        print("\nLa caja esta llena, Cerrando y enviando a distribución.")
        print("DATOS DE ALMACENAMIENTO DE LA CAJA:")
        print(f"Lote de la caja: {caja['lote']}")
        print(f"Contenido (Lista): {caja['bolsas']}")
        
        # Incrementamos el número de lote para la siguiente caja
        numero_lote += 1 
        
        if maquina_encendida.lower() == "si":
            maquina_encendida = input("¿Desea procesar la siguiente caja con la máquina? (si/no): ")

print("\nLa máquina se ha apagado. ¡Proceso finalizado!")