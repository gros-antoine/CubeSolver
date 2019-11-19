# CubeSolver
Python code of the CubeSolver project

This is the code of our CubeSolver projet adapted in Python.

## How to use it

To use it launch useSolver.py, it will ask you for a representation of your cube. Here is how it works :

A Rubik's Cube is represented in our code by an array containing 54 integers like this:
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
  - Then, you need to write the color with the number above by beginning by the top left one.
  - Then, write the one to its left.
  - Then the one to its left again.
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
  - You can now copy/paste it when the program is asking you for your representation.
  - The program should print you the solution.
