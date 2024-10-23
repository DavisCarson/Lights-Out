def flip(lights, row, col):
    """Flips the state of a button and its neighbors."""
    n_rows, n_cols = len(lights), len(lights[0])
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # Current, Up, Down, Left, Right

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < n_rows and 0 <= new_col < n_cols:
            lights[new_row][new_col] = not lights[new_row][new_col]

    return lights

def all_lights_are_off(lights, N):
    """Checks if all lights in the grid are off."""
    for row in range(N):
        for col in range(N):
            if lights[row][col]:
                return False
    return True

def solve_with_visual_output(lights, N, current_depth, max_depth, presses=[], solutions=[]):
    """Modified solve function that tracks solutions visually and exits on first solution."""
    if current_depth > max_depth:
        return False

    if all_lights_are_off(lights, N):
        solutions.append(list(presses))  # Store the successful sequence of presses
        print_solution(N, presses)  # Print the solution
        return True  # Indicate a solution has been found

    for row in range(N):
        for col in range(N):
            new_lights = flip([[light for light in row] for row in lights], row, col)  # Create a copy to avoid modifying the original grid
            new_presses = presses + [(row, col)]
            if solve_with_visual_output(new_lights, N, current_depth + 1, max_depth, new_presses, solutions):
                return True  # Solution found, propagate the success signal upwards

    return False  # No solution found in this path

def print_solution(N, presses):
    """Prints the solution in a visual format where '*' indicates a button press and '.' indicates no press."""

    solution_grid = [['.' for _ in range(N)] for _ in range(N)]
    for row, col in presses:
        solution_grid[row][col] = '*'
    print(f"N: {N}")
    for row in solution_grid:
        print(''.join(row))

def get_initial_state_all_on(N):
    """Generates an N x N matrix with all lights turned on."""
    return [[True for _ in range(N)] for _ in range(N)]

def iterative_deepening_solver_all_on_state(N):
    """Runs the backtracking search with iterative deepening for an N x N grid with all lights initially on."""

    solutions = []  # To store solutions
    lights = get_initial_state_all_on(N)  # Initialize with all lights on
    print("Initial State:")
    for row in lights:
        print(''.join(['1' if cell else '0' for cell in row]))
    print("\nSearching for a solution...\n")

    for max_depth in range(1, N*N + 1):
        if solve_with_visual_output(lights, N, 0, max_depth, [], solutions):
            break  # Solution found, no need to search further

    if not solutions:
        print(f"No solution found for N = {N}")

iterative_deepening_solver_all_on_state(4)
