from inputs.day4 import INPUT_STR
import re

def generate_input_list(input_str):
    return input_str.split("\n")

def find_xmas_occurences(xmas_list):
    row_len = len(xmas_list[0])
    col_len = len(xmas_list)
    search_lists = xmas_list.copy()

    # up down
    for i in range(0, row_len):
        search_str = ""
        for n in range(0, col_len):
            search_str += xmas_list[n][i]
        search_lists.append(search_str)
    
    # diagonal
    # right up
    for i in range(0, row_len):
        search_str = ""
        for n in range(0, col_len):
            row_index = i + n 
            if row_index >= row_len:
                break
            search_str += xmas_list[n][row_index]
        search_lists.append(search_str)
    
    # left up
    for i in range(0, row_len):
        search_str = ""
        for n in range(0, col_len):
            row_index = i - n
            if row_index < 0:
                break
            search_str += xmas_list[n][row_index]
        search_lists.append(search_str)
    
    # right down
    for n in range(1, col_len):
        search_str = ""
        for i in range(0, row_len):
            col_index = n + i
            if col_index >= col_len:
                break
            search_str += xmas_list[col_index][i]
        search_lists.append(search_str)
    
    # left down
    for n in range(1, col_len):
        search_str = ""
        for i in range(0, row_len):
            row_index = row_len - 1 - i
            col_index = n + i
            if col_index >= col_len:
                break
            search_str += xmas_list[col_index][row_index]
        search_lists.append(search_str)

    valid_xmas_counter = 0
    for search_list in search_lists:
        valid_xmas_counter += len(re.findall("XMAS", search_list))
        valid_xmas_counter += len(re.findall("SAMX", search_list))
    
    return valid_xmas_counter

def find_x_mas_occurences(xmas_list):
    valid_x_mas_counter = 0
    valid_xmas_strs = ["MS", "SM"]
    col_len = len(xmas_list)
    for n, xmas_str in enumerate(xmas_list):
        row_len = len(xmas_str)
        for i, xmas_letter in enumerate(xmas_str):
            if xmas_letter == "A":
                if n + 1>= col_len or n - 1 < 0 or i + 1 >= row_len or i - 1 < 0:
                    continue
                right_down = xmas_list[n-1][i-1] + xmas_list[n+1][i+1]
                left_down = xmas_list[n-1][i+1] + xmas_list[n+1][i-1]
                if right_down in valid_xmas_strs and left_down in valid_xmas_strs:
                    valid_x_mas_counter += 1
    return valid_x_mas_counter


if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)

    print(f"XMAS Occurrences: {find_xmas_occurences(input_list)}")
    print(f"X-MAS Occurrences: {find_x_mas_occurences(input_list)}")
