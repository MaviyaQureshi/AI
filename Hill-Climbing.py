import random
import math


def hill_climbing(objective_function, initial_solution, move_operator, max_iterations):
    current_solution = initial_solution
    current_score = objective_function(current_solution)

    for i in range(max_iterations):
        new_solution = move_operator(current_solution)
        new_score = objective_function(new_solution)

        if new_score > current_score:
            current_solution = new_solution
            current_score = new_score

    return current_solution, current_score


def get_user_input():
    try:
        initial_solution = float(input("Enter the initial solution: "))
        max_iterations = int(input("Enter the maximum number of iterations: "))
        return initial_solution, max_iterations
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()


def objective_function(x):
    return math.sin(x)


def move_operator(x):
    return x + random.uniform(-0.1, 0.1)


def main():
    initial_solution, max_iterations = get_user_input()
    solution, score = hill_climbing(
        objective_function, initial_solution, move_operator, max_iterations
    )

    print("Solution:", solution)
    print("Score:", score)


if __name__ == "__main__":
    main()
