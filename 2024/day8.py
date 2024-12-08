from inputs.day8 import INPUT_STR
from enum import Enum

class AntinodeType(Enum):
    DOUBLE = "Double"
    RESONANCE = "Resonance"

EMPTY_CHAR = "."

def generate_input_list(input_str):
    return [list(row) for row in input_str.split("\n")]

def loc_operation(loc1, loc2, operator):
    y = 0
    x = 0
    if operator == "+":
        y = loc1[0] + loc2[0]
        x = loc1[1] + loc2[1]
    if operator == "-":
        y = loc1[0] - loc2[0]
        x = loc1[1] - loc2[1]

    return (y, x)

def calc_antinodes_for_annenas_resonance(antenna1_loc, antenna2_loc, board_boundaries):
    antenna_diff = loc_operation(antenna1_loc, antenna2_loc, "-")

    ops = ["+", "-"]
    antinodes = set()
    antinodes.add(antenna1_loc)
    for op in ops:
        current_diff = antenna_diff
        while True:
            loc = loc_operation(antenna1_loc, current_diff, op)
            
            if loc[0] < 0 or loc[0] > board_boundaries[0] or loc[1] < 0 or loc[1] > board_boundaries[1]:
                break
            
            antinodes.add(loc)
            current_diff = loc_operation(current_diff, antenna_diff, "+")

    return antinodes

def calc_antinodes_for_annenas_double(antenna1_loc, antenna2_loc, board_boundaries):
    antenna_diff = loc_operation(antenna1_loc, antenna2_loc, "-")

    ops = ["+", "-"]
    antinodes = set()
    for op in ops:
        loc = loc_operation(antenna1_loc, antenna_diff, op)
        if loc == antenna2_loc:
            loc = loc_operation(loc, antenna_diff, op)
        
        if loc[0] >= 0 and loc[0] <= board_boundaries[0] and loc[1] >= 0 and loc[1] <= board_boundaries[1]:
            antinodes.add(loc)
    
    return antinodes

def get_antinodes_for_board(input_list, antinode_type):
    antenna_dict = generate_antenna_dict(input_list)
    board_boundaries = get_max_board_boundaries(input_list)

    antinodes = set()

    for atenna_loc_list in antenna_dict.values():
        antenna_antinodes = get_antinodes_for_antennas(atenna_loc_list, board_boundaries, antinode_type)
        antinodes.update(antenna_antinodes)

    return antinodes

def get_antinodes_for_antennas(atenna_loc_list, board_boundaries, antinode_type):
    atenna_loc_list_copy = [loc for loc in atenna_loc_list]
    antinodes = set()
    while (len(atenna_loc_list_copy) > 1):
        antenna1_loc = atenna_loc_list_copy.pop()
        for antenna2_loc in atenna_loc_list_copy:
            loc_antinodes = set()
            if antinode_type == AntinodeType.DOUBLE:
                loc_antinodes = calc_antinodes_for_annenas_double(antenna1_loc, antenna2_loc, board_boundaries)
            elif antinode_type == AntinodeType.RESONANCE:
                loc_antinodes = calc_antinodes_for_annenas_resonance(antenna1_loc, antenna2_loc, board_boundaries)
            antinodes.update(loc_antinodes)

    return antinodes

def generate_antenna_dict(input_list):
    antenna_dict = {}
    for n, y in enumerate(input_list):
        for i, x in enumerate(y):
            if x == EMPTY_CHAR:
                continue

            value = antenna_dict.get(x)
            if value is None:
                value = []
            
            value.append((n, i)) # (y, x)
            antenna_dict[x] = value
        
    return antenna_dict

def get_max_board_boundaries(input_list):
    return (len(input_list) - 1, len(input_list[0]) - 1) # (y, x)

if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)
    print(f"Antinode Count Double: {len(get_antinodes_for_board(input_list, AntinodeType.DOUBLE))}")
    print(f"Antinode Count Resonance: {len(get_antinodes_for_board(input_list, AntinodeType.RESONANCE))}")
