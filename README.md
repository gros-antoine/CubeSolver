# CubeSolver
Python code of the CubeSolver project

This is the code of our CubeSolver projet adapted in Python.

**Les explications en français sont en-dessous.**

The explanation of our solving method is epxlained down below (after the french explanation).

## How to use it

To use it launch useSolver.py, it will ask you for a representation of your cube. Here is how it works :

A Rubik's Cube is represented in our code by an array containing 54 integers like this (it's only an example!):
```

[3,0,5,5,0,5,0,4,0,3,2,4,1,3,4,3,1,0,0,3,4,1,4,5,3,0,5,1,0,1,2,1,3,1,1,4,2,4,4,2,2,5,1,4,2,2,2,5,3,5,3,2,0,5]

```
They each reprensent one color of the cube.
You'll need to write this array for the solver to solve your cube, here is how to do it:
- ### Color representation:
  Each color is assigned to a number:
  
  - Yellow = 0
  - Blue = 1
  - Red = 2
  - Green = 3
  - Orange = 4
  - White = 5
  
  The order is not random and is linked to the array reprensentation.
- ### Faces order and representations
  The representation is composed of 6 individual reprensatations of the 6 faces of the Rubik's Cube, considering the previous example:
  ```
  
  [3,0,5,5,0,5,0,4,0] = Yellow face
  [3,2,4,1,3,4,3,1,0] = Blue face
  [0,3,4,1,4,5,3,0,5] = Red face
  [1,0,1,2,1,3,1,1,4] = Green face
  [2,4,4,2,2,5,1,4,2] = Orange face
  [2,2,5,3,5,3,2,0,5] = White face
  
  ```
  The order of represented faces is the same as the one of colors.
- ### How to represent your scrambled cube
  - First, take the blue face in front of you with the **yellow face up**.
  - Then, you need to represenet the yellow face by using the number above by beginning by the color in the top left corner.
  - Then, write the one to its right.
  - Then the one to its right again.
  - Now repeat this step with the row below.
  - And again with the row below.
  - You should now have the yellow face represented by numbers, and format it like this:
  ```
  
  3,0,5,5,0,5,0,4,0 or 3, 0, 5, 5, 0, 5, 0, 4, 0
  
  ```
  - **The order should be the order you red and wrote them before!**
  - Then do this exact same process for the blue face still with the **yellow face up**.
  - Then with the red face and **yellow face up**.
  - Then with the green face and **yellow face up**.
  - Then with the orange face and **yellow face up**.
  - Then with the **white face and _blue face up_**.
  - You should now have the representation of the 6 faces, you just have to concatenate them and put them between '[ ]', it should look like this:
  ```

  [3,0,5,5,0,5,0,4,0,3,2,4,1,3,4,3,1,0,0,3,4,1,4,5,3,0,5,1,0,1,2,1,3,1,1,4,2,4,4,2,2,5,1,4,2,2,2,5,3,5,3,2,0,5]

  ```
  - You can now copy/paste it when the program is asking for your representation.
  - The program should print you the solution.
  - #### Remember, you should apply the solution given with the blue face in front and yellow face up!
  
## Comment utiliser le programme

Pour l'utiliser, lancez useSolver.py, il vous sera demandé une représentation de votre cube, voilà comment le systeme marche :

Un Rubik's Cube est représenté dans notre code par un tableau de dimension 1 comportant 54 entiers de cette façon (c'est seulement un exemple !) :
```

[3,0,5,5,0,5,0,4,0,3,2,4,1,3,4,3,1,0,0,3,4,1,4,5,3,0,5,1,0,1,2,1,3,1,1,4,2,4,4,2,2,5,1,4,2,2,2,5,3,5,3,2,0,5]

```
Ils représentent chacun une couleur du cube.
Vous allez avoir besoin de ce tableau pour que le programme puisse résoudre votre cube, voici comme l'obtenir :
- ### Représentation des couleurs :
  Chaque couleur est assignée à un nombre :
  
  - Jaune = 0
  - Bleu = 1
  - Rouge = 2
  - Vert = 3
  - Orange = 4
  - Blanc = 5
  
  L'ordre n'est pas aléatoire et est lié à la représentation sous forme de tableau.
- ### Représentations et ordre des faces
  La représentation est composée de 6 représentations individuelles des 6 faces du Rubik's Cube, ce qui donne avec l'exemple précédent :
  ```
  
  [3,0,5,5,0,5,0,4,0] = Face jaune
  [3,2,4,1,3,4,3,1,0] = Face bleue
  [0,3,4,1,4,5,3,0,5] = Face rouge
  [1,0,1,2,1,3,1,1,4] = Face verte
  [2,4,4,2,2,5,1,4,2] = Face orange
  [2,2,5,3,5,3,2,0,5] = Face blanche
  
  ```
  L'ordre des faces représentées est le même que celui des couleurs.
- ### Comment représenter votre cube mélangé
  - Premièrement, prenez la face bleu devant vous avec la **face jaune au-dessus**.
  - Ensuite, vous allez représentez la face jaune avec les nombres au-dessus en commençant par la couleur en haut à gauche.
  - Ensuite, écrivez celle à sa droite.
  - Ensuite, celle à la droite de la précendente.
  - Maintenant, répetez cette étape sur la ligne du dessous.
  - Et encore avec la ligne du dessous.
  - Vous devriez maintenant avoir la représentation de la face jaune, ecrivez là ainsi :
  ```
  
  3,0,5,5,0,5,0,4,0 ou 3, 0, 5, 5, 0, 5, 0, 4, 0
  
  ```
  - **L'ordre doit être celui avec lequel vous avez lu et écrit les couleurs**.
  - Ensuite, répétez ce procédé pour la face bleue, toujours avec la **face jaune au-dessus**.
  - Ensuite pour la face rouge avc la **face jaune au-dessus**.
  - Ensuite pour la face verte avec la **face jaune au-dessus**
  - Ensuite pour la face orange avec la **face jaune au-dessus**
  - Ensuite pour la **face blanche devant avec la _face bleue au-dessus_**.
  - Vous devriez maintenant avoir les représentations des 6 faces, vous devez juste les concaténer et les mettre entre '[ ]', cela devrait ressembler à cela :
  ```

  [3,0,5,5,0,5,0,4,0,3,2,4,1,3,4,3,1,0,0,3,4,1,4,5,3,0,5,1,0,1,2,1,3,1,1,4,2,4,4,2,2,5,1,4,2,2,2,5,3,5,3,2,0,5]

  ```
  - Vous pouvez maintenant la copier-coller quand le programme vous la demande.
  - Le programme vous donnne alors la résolution.
  - #### Attention, vous devez appliquer les mouvements de résolution avec la face bleue devant et la face jaune au-dessus.

**Les explications en français sont en-dessous.**

## How does our algorithm work ?

Our first idea was to solve the cube as it's done in blind speedcubing because we wouldn't have to code movements to change the representation of the cube in the code. We only needed a representation of the scrambled cube and we could solve it. We coded this with the basic Pochmann method but it was very slow (~ 300 moves to solve the cube), so we started searching for faster blind methods. We learned about the [Beyer-Hardwick method](https://www.speedsolving.com/wiki/index.php/Beyer-Hardwick_Method) to solve the edges. It was really fast, so we decided to use it. Then Lucas had the brilliant idea that we have an advantage over blind speedsolvers: we can modify the representation of the cube in our 'head'(program). So we needed the fastest way to solve corners, he then had another brilliant idea, solving the corner of a 3x3x3 cube is like solving a 2x2x2 cube! So we choosed to use the [Ortega method](https://www.speedsolving.com/wiki/index.php/Ortega_Method) to solve corners. That's the main idea of our algorithm, here is some more in depth explanation.

### First part: solving corners

As we explained, we solve corners using the Ortega method. The principle is to get all white corners on the white face, all yellow corners on the yellow face then, you only have 5 cases to solve corners.

- We choosed to place white corners first.
- We first check if there is any corners already well placed.
- Then, while all white corners are not well placed:
  - We first check if the Yellow-Green-Orange corner has white.
  - If it's the case, we look where there is place to put the corner on the white face.
    - We do the coresponding move to place the corner on the white face with the white sticker of the corner facing the wite face.
  - If it's not the case, we check another corner until we find one and repeat previous steps.
- When all white corners are on the white face with their white sticker facing the white face, all yellow corners are now
 on the yellow face.
- We now need to align corners (make yellow sticker of each corner facing the yellow face of the cube)
- The Orthega method gives us method to do this (it's like [OLL](https://www.speedsolving.com/wiki/index.php/OLL) but without placing edges so the algorithm are shorter). So we detect the case by looking at where are placed yellow stickers of corners and apply the corresponding algorithm.
- We then look at colors of corners to know in which case of the Orthega method we are.
- We apply the corresponding algorithm.

Corners are now solved!

### Second part: solving edges

As we eplained previously, we use the Beyer-Hardwick method to solve edges. The principle is to use an edge as a buffer, look where this edge need to go then look at the edge at this location and look where this edge need to go. Every combination of edges is listed in this method, so we apply corresponding moves, it will place the edge previously in the buffer place in her good position, place the edge previously there in her good position and the edge previously there go in the buffer place. We continue this process until the cube is solved.

- We first look if there is any already well placed edge.
- We then look if there is any inverted edge (edge in their position but reverted), we will solve them at the end.
- We look at the edge in the buffer place (we chose the BLUE-RED one).
  - If the edge is the buffer itself, we look for the first two free place and we do the corresponding algorithm to get a new edge.
  - If not, this is a normal case so we look where this edge need to go:
    - If the edge is the buffer (BLUE-RED edge), we find a free place for this edge and we apply the algortihm that will send the first edge to her place, send the buffer to the free place and send the edge in the free place to the buffer place.
    - If the edge is not the buffer, this is a normal case and we look where this edge need to go and we apply the corresponding algortihm.
- We repeat this until all edges are in their correct place.
- We will now treat the problem of inverted edges, if there was one inverted edge at the start of the solve, the buffer is neccessarily inverted at the end. If there was more than one edge inverted at the start, it depends on the case.
- The goal is to bring inverted edges on the top face and apply algorithm that invert edges
- If the edge is already on the top face we donn't touch it.
- If the edge is on the rest of the cube, we check what place on the top face are free and we apply moves to bring it there.
- Depending on the number of edges and where they areplaced, we use different algortihm (algorithm that invert two edges facing each other, algortihm that invert two edges next to each other ...)
- When all edges are inverted:

#### The rubik's cube is solved! FINALLY!

### Pre-solve moves

The previous method gave us way faster solves (80-100 moves) but we wanted to be faster. Our algorithm is not perfect and due to how it's coded (always checking for corners in the same order...), a slight change at the start of the solve can make a big difference afterward. So we thought about doing every combination of 2 moves on the cube before solving it and only keep the shortest algorithm we found (taking in count pre-solve moves of course). This means solvinh 262 cubes, as it was pretty fast to solve one cube, doing this was not a problem.
So we do those moves before doing the algorithm above:
```
R concatened with L, L', L2, F, F', F2, D, D', D2, U, U', U2, B, B', B2
R' concatened with L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
R2 concatened with : ["L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
L concatened with ["F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
L concatened with ["F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
L2 concatened with ["F", "F'", "F2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
F concatened with ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
F' concataned with ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
F2 concatened with ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", "B", "B'", "B2", " "],
B concatened with ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", " "],
B' concatened with : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", " "],
B2 concatened with : ["R", "R'", "R2", "L", "L'", "L2", "D", "D'", "D2", "U", "U'", "U2", " "],
U concatened with: ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2", " "],
U' concatened with ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2", " "],
U2 concatened with : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2", " "],
D concatened with : ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", " "],
D' concatened with ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", " "],
D2 concatened with: ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2", " "
```
We keep the shortest algorithm counting a '2 move (R2, F2 ...) as 2 moves.

Doing this can be very interesting and bring solves of 65 moves in average.

For example, we let our program run for hours searching for the fastest solution it could find, here it is:
```
Scramble (blue face front, yellow face up): B R' D' R U2 L2 B2 D B2 L2 D2 F R F2 D' B2 L2 B D F2 L2 B2 R' B' D2
Solve (without pre-solve moves):
Solve (with pre-solve moves): L'B' R2U'L' F UFUF' D' URL'B2R'LU R'LF'RF'BU'FUFB'L' R2FB'D2F'B (the solve is pretty insane though!)
```
You can see that the first two moves ' L'B' ' are ***VERY*** interesting and divide the lenght of the solve by two.

#### That's it for our algorithm!
