from inputs.day11 import INPUT_STR

def add_count(numbers_in_list, k, v):
    seen_count = numbers_in_list.get(k)

    if seen_count:
        numbers_in_list[k] = seen_count + v
    else:
        numbers_in_list[k] = v

    return numbers_in_list

def blinks(input_list, total_blinks):
    total_count = 0
    numbers_in_list = {}
    
    for v in input_list:
        numbers_in_list = add_count(numbers_in_list, v, 1)

    for i in range(total_blinks):
        print(i + 1, end="\r")
        numbers_in_list = blink(numbers_in_list)
    
    total_count = 0
    for v in numbers_in_list.values():
        total_count += v
    return total_count

def split_num(num, length):
    base = 10 ** (length // 2)
    return (num // base, num % base)

def blink(numbers_in_list):
    new_numbers_in_list = {}
    for k, v in numbers_in_list.items():
        k_len = len(str(k))
        if k == 0:
            new_numbers_in_list = add_count(new_numbers_in_list, 1, v)
        elif k_len % 2 == 0:
            v1, v2 = split_num(k, k_len)
            new_numbers_in_list = add_count(new_numbers_in_list, v1, v)
            new_numbers_in_list = add_count(new_numbers_in_list, v2, v)
        else:
            res = k * 2024
            new_numbers_in_list = add_count(new_numbers_in_list, res, v)

    return new_numbers_in_list

def generate_input_list(input_str):
    return [int(k) for k in input_str.split(" ")]

if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)
    print(f"25 Blinks Length: {blinks(input_list, 25)}")
    print(f"75 Blinks Length: {blinks(input_list, 75)}")
