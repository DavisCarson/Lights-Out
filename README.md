# Lights Out Puzzle Solver

A Python implementation of a solver for the **Lights Out** puzzle, where the objective is to turn off all the lights on an N x N grid. Pressing a light toggles it and its adjacent neighbors (up, down, left, right), and the puzzle starts with all lights turned on.

### How It Works
The solver employs **backtracking** and **iterative deepening** to explore all possible button presses up to a given depth, aiming to find a sequence that turns all the lights off. It tracks each sequence of presses and prints out the solution in a visual format.

### Key Features
- **Button Press Simulation:**  
  The `flip()` function simulates a button press, flipping the state of the target light and its adjacent neighbors.
  
- **Iterative Deepening:**  
  The solver incrementally increases the maximum depth (i.e., the number of button presses) until a solution is found or the maximum possible presses are exhausted.

- **Visual Output of Solution:**  
  Once a solution is found, the sequence of button presses is displayed visually using `'*'` for a press and `'.'` for no press, alongside the N x N grid.
  
- **Initial State Generation:**  
  The solver initializes the puzzle with all lights turned on, allowing the algorithm to search for a solution from this state.

### File Overview
- **main.py**:  
  Contains all core functions, including:
  - `flip()`: Simulates the button press on the lights grid.
  - `all_lights_are_off()`: Checks if all lights are turned off.
  - `solve_with_visual_output()`: Recursively solves the puzzle using backtracking.
  - `print_solution()`: Prints the button press solution visually.
  - `iterative_deepening_solver_all_on_state()`: Runs the search with iterative deepening.

### How to Use
1. Clone the repository.
2. Run the script using Python:
   ```bash
   python main.py
   ```
   The solver will display the initial state (all lights on) and, if successful, print out the solution grid with the button presses.
