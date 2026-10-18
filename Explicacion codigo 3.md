
Identificación de Entradas y Salidas

Entradas:Confirmación de si la máquina continúa encendida / en funcionamiento (maquina_encendida, como "si" o "no").
Confirmación para rellenar el depósito cuando las bolsas de stock se agotan (rellenar, como "si" o "no").
Cantidad de bolsas nuevas ingresadas al depósito (cantidad_nueva, convertida a entero con int()).

Salidas:Etapas del proceso (verificación de bolsa, vaciado de arroz, sellado hermético y empaque en caja).
Alerta de inventario cuando el stock llega a 0.
Resumen de los métodos de almacenamiento de la caja (número de lote y contenido en lista) al alcanzar la capacidad máxima (4 bolsas).
Mensaje de apagado del sistema al finalizar las operaciones.


Paso a Paso del Código

Inicio de Variables:
numero_lote = 1: Contador para identificar el lote actual del producto.
bolsas_en_stock = 2: Inventario disponible en el depósito de la máquina.
maquina_encendida = "si":control para mantener la ejecución en bucle principal.

Estructura de Almacenamiento (Diccionario y Lista):
En cada ciclo principal, se crea la caja utilizando un diccionario caja, que contiene las claves "lote","capacidad_maxima" (fijada en 4) y "bolsas", la cual es una lista vacía destinada a almacenar dinámicamente las bolsas procesadas.

Control del Bucle de Empaque (while len(caja(bolsas)) < caja(capacidad maxima)):
El ciclo interno se ejecuta continuamente mientras la cantidad de bolsas en la caja sea menor a su capacidad máxima.

Gestión de Stock:
Si bolsas_en_stock son menores o igual a 0, el sistema entra en estado de advertencia y solicita reabastecimiento. Si se responde "si", se actualiza bolsas_en_stock con la nueva cantidad ingresada. De lo contrario, la máquina se apaga (maquina_encendida = "no") y rompe el bucle con break.

Si bolsas_en_stock son mayores a 0, la máquina realiza las 4 etapas del proceso:
 descontando una bolsa del depósito (bolsas_en_stock -= 1), agregándola a la lista del diccionario mediante caja(bolsas).append(...) escribiendo la confirmación de empaque.

Caja llena e Incremento del Lote:
Una vez alcanzadas las 4 bolsas en la lista, la condición del bucle interno finaliza.
El sistema verifica que la caja está llena (len(caja(bolsas)) == 4), imprime los datos de almacenamiento estructurado de la caja, incrementa numero_lote += 1 para la siguiente iteración y consulta si se desea procesar el siguiente lote.
