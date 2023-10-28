def print_board(board):
    for row in board:
        print(" ".join(row))


def initialize_game():
    # Create an empty 3x3 tic-tac-toe board
    return [[" " for _ in range(3)] for _ in range(3)]


def game_over(state):
    # Check if the game is over (e.g., someone has won or it's a draw)
    for row in state:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(state[0])):
        check = []
        for row in state:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
            return True

    if state[0][0] == state[1][1] == state[2][2] != " ":
        return True

    if state[0][2] == state[1][1] == state[2][0] != " ":
        return True

    if all(cell != " " for row in state for cell in row):
        return True

    return False


def evaluate(state):
    # Evaluate the current game state (e.g., assign scores for different outcomes)
    if game_over(state) and state[1][1] == "X":
        return 1  # Player X wins
    elif game_over(state) and state[1][1] == "O":
        return -1  # Player O wins
    else:
        return 0  # It's a draw


def get_possible_moves(state):
    # Get a list of possible moves from the current state
    moves = []
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == " ":
                new_state = [row[:] for row in state]
                new_state[i][j] = "X"
                moves.append(new_state)
    return moves


def min_max(state, depth, maximizing_player):
    if depth == 0 or game_over(state):
        return evaluate(state)

    if maximizing_player:
        max_eval = float("-inf")
        for child in get_possible_moves(state):
            eval = min_max(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for child in get_possible_moves(state):
            eval = min_max(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(state, depth):
    best_move = None
    best_eval = float("-inf")
    for move in get_possible_moves(state):
        eval = min_max(move, depth - 1, False)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


# Example usage
initial_state = initialize_game()
best_move = find_best_move(initial_state, depth=3)

# Print the intermediate board states
for move in best_move:
    print_board(move)

# Print the final best move (3x3 tic-tac-toe board)
print("Best Move:")
print_board(best_move)
