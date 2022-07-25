# space-invaders
### Universidad de Costa Rica
### Escuela de Ciencias de la Computación e Informática
### Curso: Aprendizaje Mecánico - CI-0148
### Proyecto Final - Space Invaders
### Estudiantes:
 - Luis Carlos Quesada Rodríguez
 - Gianfranco Bagnarello Hernández 
# 
### Descripción del proyecto:
"Space Invaders" consiste en un juego donde se debe luchar contra naves espaciales y destruir la cantidad máxima posible. Para ganar se deben destruir todas las naves. En el variante implementado, las naves llegan en oleadas de tamaño fijo. El jugador debe disparar proyectiles e intentar destruir la mayor cantidad posible antes de que alguna llegue al límite inferior de la pantalla, caso en el que se pierde el juego y se debe volver a empezar.
El tipo de algoritmo de aprendizaje mecánico implementado fue Deep Q learning, que utiliza redes neuronales, en este caso una de predicciones y otra de objetivo, para explorar el juego e intentar aproximar un modelo que permita maximizar una recompensa obtenida. En este caso, al agente se le otorga una recompensa cada vez que destruye una nave invasora, y se le penaliza cuando no toma ninguna acción. El agente toma como entrada una imagen de 640x480 que sirve como estado del ambiente, y la salida del agente es el valor Q de tomar una acción. Las acciones disponibles para el agente son: moverse a la izquierda, moverse a la derecha y disparar. El agente interactúa con el ambiente tomando la acción obtenida en su salida. 

Durante el proceso de desarrollo se encontraron varios desafíos:

- En la fase inicial de pruebas, el agente se movía muy lento, y cada iteración del algoritmo tomaba exactamente 3.7 minutos. Se dejó entrenando por alrededor de 11 horas. El modelo generado (guardado y adjunto como model.pth) no trabajaba de la forma deseada, ya que las acciones que tomaba lo llebavan a quedarse en el borde izquierdo o derecho de la pantalla sin disparar, ejecutando constamente la acción de moverse a la derecha o izquierda, de acuerdo del lado donde se quedaba.
Otro factor que tenía es que el modelo tomaba una cantidad de tiempo considerable para entrenar por lo que se tomaron medidas como acelerar la velocidad de aparición de las oleadas, y reducirles la complejidad un poco removiendo los patrones de movimiento.

-Otro desafío presentado en la fase de pruebas era



#


### Clases implementadas:
- Actions: contiene las acciones posibles que pueden ser tomadas en el juego.
- Agent: clase que contiene la red de DeepQlearning del agente.
- Bullet: maneja detalles del los proyectiles disparados.
- Enemy Manager: manejador de oleadas, movimiento de enemigos y contadores de puntuación la recompensa del agente.
- Enemy: contiene propiedades de los enemigos individualmente, los tipos de enemigos, y sus interacciones con el ambiente.
- Game manager: controla el juego importando clases y corriendo el agente.
- Game: Importa clases de entidades para dibujar el juego y correr el game loop.
- Player: clase que controla el movimiento e interacciones de la nave del agente con el ambiente.

### Resultados:
- Pruebas realizadas con 10 oleadas:
- Pruebas realizadas con 100 oleadas:
- Figuras:

Bibliotecas requeridas:
- Se encuentran en el archivo requirements.txt adjunto