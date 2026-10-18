Identificación de Entradas y Salidas

Entradas: Seleccionar una opción en el menú seleccionada por el usuario (pedido, ingresado como número en texto 1, 2, 3, 4, o 5).
Respuesta de confirmación para continuar con mas opciones (continuar, como si o no).

Salidas: Mostrar del menú de opciones disponibles con precios ($2,500 – $18,000).
Mensaje de confirmando cada que se añade un producto exitosamente.
Mensaje para cuando la opción ingresada no existe en el menú ("Mil disculpas no tenemos pero pronto, lo que desee el cliente.").
Total acumulado a pagar (total) y mensaje final de despedida.


Paso a Paso del Código

Inicio de Variables:
Se inicia la variable acumuladora total = 0 para almacenar el precio total del pedido.
Se define la variable de control continuar = "si" para permitir que el bucle while se ejecute por primera vez.

Presentación del Menú:
Mediante instrucciones print(), se muestra al usuario loa 5 platos disponibles con sus respectivos precios.
Bucle de Captura e Interacción (while):
El programa evalúa si continuar == "si". De ser así, solicita mediante input() la elección del plato.

Estructura Condicional (if-elif-else):
Opciones del 1 al 5: Se evalúa la opción ingresada. Si coincide con alguna válida, suma el valor correspondiente al acumulador total y muestra un mensaje de confirmación del producto.
Caso por defecto (else): Si el usuario ingresa un número distinto o un texto que no forma parte de la lista, el programa captura el error enviando un mensaje sin interrumpir la ejecución del programa ni alterar el valor de total.

Control de Iteración:
Al final del bucle, el programa pregunta al usuario si desea continuar pidiendo (¿Desea pedir algo más?).
 Si el usuario ingresa "no", se rompe la condición del while.

Resultados Finales:
Fuera del bucle, el sistema imprime el valor final acumulado en total y agradece por la compra.