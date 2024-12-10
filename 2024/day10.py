from inputs.day10 import INPUT_STR

def find_trailheads(board):
    trailheads = set()
    for y, row in enumerate(board):
        for x, column in enumerate(row):
            if column == 0:
                trailheads.add((y, x))
    return trailheads

def generate_input_board(input_str):
    input_list = input_str.split("\n")
    input_board = []
    for row_input in input_list:
        input_board.append([int(v) for v in row_input])

    return input_board

def add_positions(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def nav_path_end_points(board, position, current_value, y_max, x_max):
    if current_value == 9:
        return {position}

    end_locations = set()
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for direction in directions:
        new_pos = add_positions(position, direction)
        if new_pos[0] < y_max and new_pos[1] < x_max and new_pos[0] >= 0 and new_pos[1] >= 0:
            new_val = board[new_pos[0]][new_pos[1]]
            if new_val == current_value + 1:
                end_locations.update(nav_path_end_points(board, new_pos, new_val, y_max, x_max))
            
    return end_locations

def find_trailhead_endings_score(board, trailheads):
    y_max = len(board)
    x_max = len(board[0])

    trailhead_score = 0
    for trailhead in trailheads:
        trailhead_score += len(nav_path_end_points(board, trailhead, 0, y_max, x_max))

    return trailhead_score

def nav_paths(board, position, current_value, y_max, x_max):
    if current_value == 9:
        return [position]

    end_locations = []
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for direction in directions:
        new_pos = add_positions(position, direction)
        if new_pos[0] < y_max and new_pos[1] < x_max and new_pos[0] >= 0 and new_pos[1] >= 0:
            new_val = board[new_pos[0]][new_pos[1]]
            if new_val == current_value + 1:
                end_locations += nav_paths(board, new_pos, new_val, y_max, x_max)
            
    return end_locations
    
def find_trailhead_paths_score(board, trailheads):
    y_max = len(board)
    x_max = len(board[0])

    trailhead_score = 0
    for trailhead in trailheads:
        trailhead_score += len(nav_paths(board, trailhead, 0, y_max, x_max))

    return trailhead_score

def print_board(board):
    for row in board:
        print(row)
    print("\n")

if __name__ == "__main__":
    input_board = generate_input_board(INPUT_STR)
    trailheads = find_trailheads(input_board)
    
    print(f"Trailhead Score by trailhead endpoints: {find_trailhead_endings_score(input_board, trailheads)}")
    print(f"Trailhead Score by trailhead paths: {find_trailhead_paths_score(input_board, trailheads)}")