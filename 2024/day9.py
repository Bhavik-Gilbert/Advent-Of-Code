from inputs.day9 import INPUT_STR
import copy

EMPTY_CHAR = "."
def generate_expanded_files(input_str):
    expanded_file_list = []
    for i, v in enumerate(input_str):
        char = ""
        if i % 2 == 0:
            char = str(int(i / 2))
        else:
            char = EMPTY_CHAR
        
        for n in range(int(v)):
            expanded_file_list.append(char)
    
    return expanded_file_list

def find_last_non_empty_val(file_str, file_str_len):
    for i in range(len(file_str)):
        index = file_str_len - i - 1
        v = file_str[index]
        if v != EMPTY_CHAR:
            return v, index

    return None, None

def compress_expanded_file_v1(expanded_file_list):
    expanded_file_list_copy = copy.deepcopy(expanded_file_list)
    compressed_file_list = []
    compressed_file_len = len(expanded_file_list_copy)

    for i in range(compressed_file_len):
        print(f"Compressing file -> {i + 1}/{compressed_file_len}")

        if i >= compressed_file_len:
            break
        v = expanded_file_list_copy[i]

        if v != EMPTY_CHAR:
            compressed_file_list.append(v)
            continue

        last_val, last_index = find_last_non_empty_val(expanded_file_list_copy, compressed_file_len)
        if last_val and last_index > i:
            compressed_file_len -= 1
            expanded_file_list_copy.pop(last_index)
            compressed_file_list.append(last_val)
        else:
            break
        
    return compressed_file_list

def find_first_empty_slot_with_space(file_list, slot_size):
    for i, (file_val, file_len) in enumerate(file_list):
        if file_len >= slot_size and file_val == EMPTY_CHAR:
            return i, file_len

    return None, None

def compress_expanded_file_v2(expanded_file_list):
    two_d_expanded_file_list = []
    temp_list = []
    last_file_value = None
    for expanded_file in expanded_file_list:
        if last_file_value and expanded_file != last_file_value:
            two_d_expanded_file_list.append((last_file_value, len(temp_list)))
            temp_list = []
        temp_list.append(expanded_file)
        last_file_value = expanded_file
    two_d_expanded_file_list.append((last_file_value, len(temp_list)))

    len_two_d_expanded_file_list = len(two_d_expanded_file_list)
    index = len(two_d_expanded_file_list) - 1
    while index >= 0:
        print(f"Compressing file -> {len_two_d_expanded_file_list - index}/{len_two_d_expanded_file_list}")
        file_val, file_len = two_d_expanded_file_list[index] 
        if file_val == EMPTY_CHAR:
            index -= 1
            continue
        
        empty_index, empty_len = find_first_empty_slot_with_space(two_d_expanded_file_list[0: index], file_len)
        if empty_index is not None and empty_len is not None and empty_index < index:
            len_diff = empty_len - file_len
            two_d_expanded_file_list[index] = (EMPTY_CHAR, file_len)
            two_d_expanded_file_list.pop(empty_index)
            if len_diff > 0:
                index += 1
                two_d_expanded_file_list.insert(empty_index, (EMPTY_CHAR, len_diff))
            
            two_d_expanded_file_list.insert(empty_index, (file_val, file_len))
            
        index -= 1
        
    compressed_file_list = []
    for file_value, file_length in two_d_expanded_file_list:
        for i in range(file_length):
            compressed_file_list.append(file_value)
    
        
    return compressed_file_list
    
def calc_compressed_checksum(compressed_file_list):
    checksum = 0

    for i, v in enumerate(compressed_file_list):
        if v == EMPTY_CHAR:
            continue
        checksum += i * int(v)
    
    return checksum

if __name__ == "__main__":
    expanded_file_list = generate_expanded_files(INPUT_STR)
    compressed_file_list_v1 = compress_expanded_file_v1(expanded_file_list)
    compressed_file_list_v2 = compress_expanded_file_v2(expanded_file_list)
    print(f"Checksum V1: {calc_compressed_checksum(compressed_file_list_v1)}")
    print(f"Checksum V2: {calc_compressed_checksum(compressed_file_list_v2)}")
