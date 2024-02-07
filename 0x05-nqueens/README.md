# N Queens

**By**: Alexa Orrico, Software Engineer at Holberton School

**Weight**: 1

## Overview
The N queens puzzle is a classic chess problem that challenges the placement of N non-attacking queens on an N×N chessboard. This project implements a program in Python that solves the N queens problem and prints every possible solution. 

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable

### Usage
The program can be executed from the command line using the following syntax:
```bash
./nqueens.py N
```
Where N is an integer greater than or equal to 4, representing the size of the chessboard and the number of queens to be placed.

### Error Handling
The program includes error handling to ensure correct usage:

- If the user provides the wrong number of arguments, it prints Usage: nqueens N and exits with status 1.
- If N is not an integer, it prints N must be a number and exits with status 1.
- If N is smaller than 4, it prints N must be at least 4 and exits with status 1.

### Output Format
The program prints every possible solution to the problem, with each solution represented as a list of queen positions. One solution is printed per line.

### Example
```bash
$ ./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Notes
- The solutions are not printed in a specific order.
- The program uses the backtracking algorithm to find all possible solutions.
- Only the sys module is imported, as per the project requirements.
- The code follows the PEP 8 style guide.
