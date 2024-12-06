from inputs.day6 import INPUT_STR
import copy

GUARD_CHAR = "^"
OBSTACLE_CHAR = "#"
EMPTY_CHAR = "."

def generate_input_board(input_str):
    return [list(y) for y in input_str.split("\n")]

def find_guard(board):
    for n, y in enumerate(board):
        for i, x in enumerate(y):
            if x == GUARD_CHAR:
                return(n, i) # (y, x)
        
    return None

def add_coords(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def rotate_direction(direction):
    if direction == (1, 0):
        return (0, -1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (-1, 0):
        return (0, 1)
    else:
        return (-1, 0)

def guard_move(board, guard_pos, direction):
    next_board = board.copy()
    next_move_pos = add_coords(guard_pos, direction)
    if next_move_pos[0] >= len(next_board) or next_move_pos[0] < 0 or next_move_pos[1] >= len(next_board[next_move_pos[0]]) or next_move_pos[1] < 0:
        next_board[guard_pos[0]][guard_pos[1]] = EMPTY_CHAR
        return board, None, None

    next_move = board[next_move_pos[0]][next_move_pos[1]]
    while next_move == OBSTACLE_CHAR:
        direction = rotate_direction(direction)
        next_move_pos = add_coords(guard_pos, direction)
        next_move = board[next_move_pos[0]][next_move_pos[1]]
    
    next_board[guard_pos[0]][guard_pos[1]] = EMPTY_CHAR
    next_board[next_move_pos[0]][next_move_pos[1]] = GUARD_CHAR

    return next_board, next_move_pos, direction

def count_guard_positions(board):
    board_copy = copy.deepcopy(board)
    guard_distinct_trail = set()
    guard_pos = find_guard(board)
    direction = (-1, 0)
    guard_distinct_trail.add(guard_pos)

    while guard_pos:
        board_copy, guard_pos, direction = guard_move(board_copy, guard_pos, direction)
        guard_distinct_trail.add(guard_pos)
    
    return len(guard_distinct_trail) - 1

def unique_loop_obstacle_positions(board):
    loop_obstacle_count = 0
    starting_guard_pos = find_guard(board)
    starting_direction = (-1, 0)

    turns = (len(board) - 1) * (len(board[0]) - 1)
    turn_count = 0

    for n, y in enumerate(board):
        for i, x in enumerate(y):
            print(f"turn {n} {i} - {turn_count} / {turns}")
            turn_count += 1

            if x == GUARD_CHAR:
                continue
            
            board_with_obstacle = copy.deepcopy(board)
            board_with_obstacle[n][i] = OBSTACLE_CHAR
            direction = starting_direction
            guard_pos = starting_guard_pos
            previous_space_mapping = {}

            while guard_pos:
                prev_guard_pos = guard_pos
                board_with_obstacle, guard_pos, direction = guard_move(board_with_obstacle, guard_pos, direction)
                
                previous_current_space_mapping = previous_space_mapping.get(guard_pos)
                if previous_current_space_mapping and prev_guard_pos in previous_current_space_mapping:
                        loop_obstacle_count += 1
                        break
                else:
                    previous_current_space_mapping = set()
                previous_current_space_mapping.add(prev_guard_pos)
                previous_space_mapping[guard_pos] = previous_current_space_mapping


    return loop_obstacle_count

def print_board(board):
    for y in board:
        print(y)
    
    print("\n")

if __name__ == '__main__':
    board = generate_input_board(INPUT_STR)
    print(f"Guard Distinct Positions: {count_guard_positions(board)}")
    print(f"Distinct Guard Loop Obstacle Positions: {unique_loop_obstacle_positions(board)}")