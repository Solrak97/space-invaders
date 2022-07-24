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
Consiste en un simulador del juego "space invaders" donde el jugador se enfrenta a varias oleadas de enemigos, y debe dispararles para eliminarlas y obtener puntos. 
El simulador busca que un agente de Q-Learning logre aprender a jugar y ganar.


(25%) Un documento descriptivo que detalle: el juego al que se le implementará un agente inteligente, el tipo de algoritmo de aprendizaje mecánico que se utilizará para el desarrollo del agente, las características del agente (entradas/salidas/interacción con el espacio), los desafíos encontrados en el desarrollo de su agente, cómo se resolvieron los mismos y los resultados obtenidos. Puede adjuntar capturas de pantalla y resultados de las métricas observadas para su agente.
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