import random
import math


def hill_climb(objective_fn, initial_soln, move_operator, max_itr):
    sol = initial_soln
    score = objective_fn(sol)

    for i in range(max_itr):
        new_sol = move_operator(sol)
        new_score = objective_fn(new_sol)

        if new_score > score:
            sol = new_sol
            score = new_score

    return sol, score


def get_user_input():
    try:
        initiial_solution = float(input("Enter the initial solution : "))
        max_itr = int(input("Enter the maximum number of interation : "))
        return initiial_solution, max_itr
    except ValueError:
        print("Invalid Input. Please enter a valid number")
        return get_user_input()


def objective_fn(x):
    return math.sin(x)


def move_operator(x):
    return x + random.uniform(-0.1, 0.1)


def main():
    initial_soln, max_itr = get_user_input()

    solution, score = hill_climb(objective_fn, initial_soln, move_operator, max_itr)

    print("Solution : ", solution)
    print("Score : ", score)


if __name__ == "__main__":
    main()
