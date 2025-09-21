# Original de snake.py

## Descripción  
Este proyecto es una adaptación del clásico juego Snake del paquete Freegames.  
Utiliza la librería `turtle` de Python para crear una serpiente que se desplaza por la pantalla en busca de comida, la cual va aumentando su tamaño a medida que se consume. El objetivo principal del juego es evitar que la serpiente choque contra sí misma o contra los límites del tablero.  

## Modificaciones  
En una primera versión modificada se agregó la función `moveFood()`, que permite que la comida se mueva paso a paso en una dirección aleatoria utilizando vectores, validando además que no se salga de los límites de la ventana.  

Posteriormente, se amplió el programa en el manejo de los colores de la serpiente: originalmente cambiaba de color completo solo al reiniciar el programa, pero además se implementó que cambie de color en cada movimiento dentro de la función `move()` y también cada vez que se agrega un nuevo segmento al cuerpo. De este modo, cada parte de la serpiente puede tener un color distinto, haciendo el juego más dinámico y difícil por el cambio continuo de los colores.
