# Famous_CODING_Problems

TIC-TAC-TOE :
=
This Python script implements a Tic-Tac-Toe game where a human player can play against an AI opponent. The AI opponent uses the minimax algorithm with alpha-beta pruning to make its moves efficiently. The game interface prompts the player for moves, validates them, and displays the current state of the game board after each move. The AI evaluates possible future game states to make optimal moves, aiming to either win or force a draw. The game continues until one player wins, the board fills up resulting in a draw, or until the maximum number of moves (9) is reached. Overall, this script demonstrates the implementation of a playable Tic-Tac-Toe game with a challenging AI opponent.

TRAVELLING_SALESMAN_PROB :
=
This Python script implements a genetic algorithm to solve the Traveling Salesman Problem (TSP) for a given set of cities and their coordinates. The TSP involves finding the shortest possible route that visits each city exactly once and returns to the origin city. The script first defines functions to calculate the distance between cities, generate an initial population of routes, calculate the total distance of a route, perform crossover and mutation operations on routes, and finally, execute the genetic algorithm to evolve solutions over multiple generations.
In the main function, the script initializes parameters such as population size, number of generations, and mutation rate. It then generates an initial population of routes, applies the genetic algorithm to evolve better solutions, and prints out the best route found along with its total distance.Overall, this script demonstrates the application of genetic algorithms to efficiently solve the TSP, providing an approximate solution to one of the most well-known combinatorial optimization problems.

CITY_OF_KONIGSBERG_PROB :
=
This code is determines whether an Eulerian Path exists in a given undirected graph. An Eulerian Path is a path that traverses each edge of the graph exactly once. If such a path exists, the code identifies the starting node from which the Eulerian Path can be traversed. The approach employed involves recursively traversing the graph from each node, checking if a path exists that covers all nodes in the graph. If such a path is found, it indicates the existence of an Eulerian Path. The code returns a Boolean value indicating the existence of an Eulerian Path and, if applicable, specifies the starting node of the path. This problem is significant in graph theory and has various applications, including in network analysis, circuit design, and bioinformatics.

TOWER_OF_HANOI : 
=
The Tower of Hanoi problem is a classic mathematical puzzle that involves moving a stack of disks from one rod to another, obeying certain constraints. This recursive Python function, `tower_of_hanoi`, solves the Tower of Hanoi problem for a given number of disks.
"The function `tower_of_hanoi` implements the solution to the Tower of Hanoi problem recursively. Given the number of disks `n`, along with three rods labeled as source, destination, and auxiliary, the function recursively moves the disks from the source rod to the destination rod using the auxiliary rod as an intermediary, following the rules of the Tower of Hanoi puzzle. At each step, it prints the move required to accomplish this task. Finally, when `n` becomes 1, it simply moves the smallest disk directly to the destination rod."

8_PUZZLE_PROB :
=
This Python code solves the Eight Puzzle problem using Iterative Deepening Search (IDS). The Eight Puzzle is a sliding puzzle where the goal is to rearrange numbered tiles into a specific configuration by sliding them one at a time into a blank space.
1) The `eight_Puzzle` class represents a state in the puzzle. It stores the current state, parent state (for backtracking), and cost functions `g`, `h`, and `f`, where `g` represents the cost to reach the current state, `h` is the heuristic function value, and `f` is the sum of `g` and `h`.
2) The `Manhattan_Distance` method calculates the Manhattan distance heuristic for the current state, estimating the minimum number of moves required to reach the goal state.
3) The `get_position` function generates neighboring states reachable from the current state by moving the blank tile in four directions (up, down, left, right).
4) The `IDS_Search` function implements Iterative Deepening Search. It performs depth-limited searches with increasing depth limits until a solution is found or all depths are exhausted.
5) The `depth_limited_search` function performs a depth-limited search up to a specified depth limit, expanding nodes and exploring neighboring states until a solution is found within the depth limit.
6) The `reconstruct_path` function backtracks from the goal state to the initial state, reconstructing the solution path.
7) The `print_path` function prints each step of the solution path, displaying the state of the puzzle at each step.
In the `main` block, an initial state of the Eight Puzzle is defined. The `IDS_Search` function is called to find a solution. If a solution is found, it prints the solution path; otherwise, it indicates that no solution was found.

Maze_Problem
---
The problem is to find the shortest path from a start point to an end point in a maze. The maze is represented as a grid where `0` indicates an empty cell and `1` indicates an obstacle. The solution uses Dijkstra's algorithm to traverse the maze, prioritizing cells with lower accumulated distances from the start. It maintains a priority queue to efficiently select the next cell to explore until reaching the end point or determining that no path exists.

Minimun Spanning Tree
--
Given a connected, undirected graph with weighted edges, find a tree that connects all vertices with the minimum total edge weight.

Prim's Algorithm:
--
1. Start with an arbitrary vertex.
2. At each step, add the edge with the smallest weight that connects a vertex in the tree to one not yet in the tree.
3. Repeat until all vertices are included in the tree.
Prim's algorithm guarantees a minimum spanning tree by greedily selecting edges with the smallest weights to connect vertices, ensuring that the tree formed has the minimum possible total edge weight.

Eight Queen Problem
--
The Eight Queens Puzzle involves placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. This means no two queens can be in the same row, column, or diagonal. The problem is commonly solved using backtracking, where queens are recursively placed on the board one by one, ensuring they don't conflict with each other.

Dining Philosopher Problem
--
The Dining Philosophers Problem is a classic concurrency problem where a number of philosophers sit at a table and do one of two things: eat or think. However, they must use shared resources (the forks) and must avoid deadlock and starvation.
In this problem, each philosopher represents a thread, and each fork is represented by a lock. The philosopher can only eat if they can acquire both the fork on their left and the fork on their right. To prevent deadlock, philosophers employ a strategy to avoid simultaneously grabbing both forks. Once a philosopher has finished eating, they release the forks, allowing other philosophers to use them.The challenge lies in designing a solution that ensures each philosopher can eat without causing deadlock or starvation, where deadlock occurs when each philosopher holds one fork and is waiting for the other, and starvation occurs when a philosopher is unable to acquire the forks they need to eat.

Consumer Producer Problem
--
The Producer-Consumer Problem is a synchronization challenge where multiple producer threads generate data items to be stored in a shared buffer, while consumer threads retrieve and process these items. The main goal is to ensure that producers and consumers can access the buffer safely and efficiently, preventing issues such as race conditions or buffer overflow. Effective synchronization mechanisms are crucial to address this problem, allowing for coordinated access to the shared buffer while maintaining data integrity.

Coin Change Problem
--
In the Coin Change Problem, we are given a set of coin denominations and a target amount of money. The goal is to determine the minimum number of coins required to make up the target amount. This problem arises frequently in real-world scenarios, such as making change in a vending machine or cash register. The challenge lies in efficiently selecting the optimal combination of coins to minimize the total number used. Dynamic programming is often employed to solve this problem because of its ability to efficiently explore all possible combinations of coins while avoiding redundant calculations. By iteratively considering each coin denomination and updating the minimum number of coins needed to make each amount, dynamic programming offers a systematic approach to find the optimal solution.

Sudoko Solver
--
The Sudoku Solver problem is a classic puzzle that involves filling a 9x9 grid with digits from 1 to 9, such that each row, each column, and each of the nine 3x3 subgrids (also known as boxes) contain all of the digits from 1 to 9 without repetition. The objective is to find a solution that satisfies these conditions.
The puzzle begins with some cells already filled with numbers (clues), and the solver must fill in the remaining empty cells following the Sudoku rules. These rules dictate that:
Each row must contain all digits from 1 to 9 without repetition.
Each column must contain all digits from 1 to 9 without repetition.
Each of the nine 3x3 subgrids (boxes) must contain all digits from 1 to 9 without repetition.
To solve the Sudoku puzzle, we typically use backtracking, a brute-force algorithmic technique that systematically tries all possible configurations until a solution is found. Here's how the algorithm works:
1. Find an empty cell in the Sudoku grid.
2. Try filling the cell with a number from 1 to 9.
3. Check if the placement of this number is valid according to the Sudoku rules.
4. If the number is valid, move to the next empty cell and repeat steps 2-4 recursively.
5. If no valid number can be placed in the current cell, backtrack to the previous cell and try a different number.
6. Repeat this process until the entire grid is filled, or until no valid solution exists.

The backtracking algorithm explores the solution space efficiently, discarding branches that violate the Sudoku constraints and backtracking to explore alternative choices.
Once a solution is found, the Sudoku puzzle is considered solved, and the grid is filled with numbers adhering to the Sudoku rules. If no solution exists (i.e., the puzzle is unsolvable), the solver will backtrack until all possibilities have been exhausted, indicating that the puzzle is invalid or improperly constructed.

Josephus Problem
--
The Josephus Problem involves a group of \( n \) people arranged in a circle, where every \( k \)-th person is to be executed, and the goal is to find the position of the last survivor.
To solve this problem efficiently, a recursive function can be used. At each step, the function determines the position of the survivor by recursively reducing the circle size and adjusting for the elimination rule. Finally, the survivor's position is returned.
This problem illustrates the use of recursion in solving sequential elimination problems and has applications in various fields such as computer science, mathematics, and game theory.
