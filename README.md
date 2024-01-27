# Famous_CODING_Problems

#TIC-TAC-TOE :
=
This Python script implements a Tic-Tac-Toe game where a human player can play against an AI opponent. The AI opponent uses the minimax algorithm with alpha-beta pruning to make its moves efficiently. The game interface prompts the player for moves, validates them, and displays the current state of the game board after each move. The AI evaluates possible future game states to make optimal moves, aiming to either win or force a draw. The game continues until one player wins, the board fills up resulting in a draw, or until the maximum number of moves (9) is reached. Overall, this script demonstrates the implementation of a playable Tic-Tac-Toe game with a challenging AI opponent.

#TRAVELLING_SALESMAN_PROB :
=
This Python script implements a genetic algorithm to solve the Traveling Salesman Problem (TSP) for a given set of cities and their coordinates. The TSP involves finding the shortest possible route that visits each city exactly once and returns to the origin city. The script first defines functions to calculate the distance between cities, generate an initial population of routes, calculate the total distance of a route, perform crossover and mutation operations on routes, and finally, execute the genetic algorithm to evolve solutions over multiple generations.
In the main function, the script initializes parameters such as population size, number of generations, and mutation rate. It then generates an initial population of routes, applies the genetic algorithm to evolve better solutions, and prints out the best route found along with its total distance.Overall, this script demonstrates the application of genetic algorithms to efficiently solve the TSP, providing an approximate solution to one of the most well-known combinatorial optimization problems.

#CITY_OF_KONIGSBERG_PROB :
=
This code is determines whether an Eulerian Path exists in a given undirected graph. An Eulerian Path is a path that traverses each edge of the graph exactly once. If such a path exists, the code identifies the starting node from which the Eulerian Path can be traversed. The approach employed involves recursively traversing the graph from each node, checking if a path exists that covers all nodes in the graph. If such a path is found, it indicates the existence of an Eulerian Path. The code returns a Boolean value indicating the existence of an Eulerian Path and, if applicable, specifies the starting node of the path. This problem is significant in graph theory and has various applications, including in network analysis, circuit design, and bioinformatics.

#TOWER_OF_HANOI : 
=
The Tower of Hanoi problem is a classic mathematical puzzle that involves moving a stack of disks from one rod to another, obeying certain constraints. This recursive Python function, `tower_of_hanoi`, solves the Tower of Hanoi problem for a given number of disks.
"The function `tower_of_hanoi` implements the solution to the Tower of Hanoi problem recursively. Given the number of disks `n`, along with three rods labeled as source, destination, and auxiliary, the function recursively moves the disks from the source rod to the destination rod using the auxiliary rod as an intermediary, following the rules of the Tower of Hanoi puzzle. At each step, it prints the move required to accomplish this task. Finally, when `n` becomes 1, it simply moves the smallest disk directly to the destination rod."
