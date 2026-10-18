Identificación de Entradas y Salidas

Entradas:La edad de cada cliente ingresada (edad, convertida a número entero mediante int()).
La respuesta de control para indicar si hay más personas por registrar en el grupo actual (continuar_grupo, como "si" o "no").
El comando de control general para atender al siguiente grupo de clientes o finalizar la ejecución del sistema (turno, ingresado como "next" o cualquier otra tecla para finalizar).

Salidas:Resumen al finalizar el grupo, mostrando el número total de personas ingresadas y el valor conjunto a pagar.
Mensaje final de despedida al apagar el sistema.

Paso A Paso del Código

Control de Turnos (while turno):
Se define un bucle externo inicializado con turno = "next" que permite operar el sistema de taquilla de forma consecutiva para diferentes grupos de clientes.

Inicio de Variables del Grupo:
Al comenzar cada turno, se ponen en cero o en su estado inicial los acumuladores total_pagar = 0, cantidad_personas = 0 y la variable de control interno continuar_grupo = "si".

Bucle de Ingreso por Persona (while continuar_grupo):El sistema solicita la edad del cliente de manera repetitiva mientras el usuario confirme que hay más personas en el grupo.

Estructura de tarifas por edad (if-elif-else):
Menores de 5 años (edad < 5): Asigna un precio de $0 e imprime el mensaje de entrada gratis.   Entre 5 y 18 años (edad <= 18): Asigna una tarifa de $5.
Mayores de 18 años (else): Asigna una tarifa de $10.
   
Acumuladores:
A cada iteración se suma el precio de la entrada actual al acumulador total_pagar y se incrementa en 1 el contador cantidad_personas.

Resumen y siguiente:
Una vez que el usuario indica que no hay más personas ("no"), el ciclo interno termina y el sistema imprime el resumen financiero del grupo, procediendo a preguntar si se desea atender un nuevo turno.