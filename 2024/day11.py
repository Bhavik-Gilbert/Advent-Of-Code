from inputs.day11 import INPUT_STR

def blinks(input_list, total_blinks):
    if total_blinks == 0:
        return len(input_list)

    total_count = 0
    input_list_len = len(input_list)
    if input_list_len > 32768:
        for v in input_list:
            total_count += blinks(blink([v]), total_blinks - 1)
    else:
        total_count += blinks(blink(input_list), total_blinks - 1)
    
    return total_count

def blink(input_list):
    blinked_list = []
    for v in input_list:
        v_len = len(v)
        if int(v) == 0:
            blinked_list.append("1")
        elif v_len % 2 == 0:
            # TODO: is there a more efficient way to split this value in half
            blinked_list.append(str(int(v[:v_len//2])))
            blinked_list.append(str(int(v[v_len//2:])))
        else:
            blinked_list.append(str(int(v) * 2024))
    
    return blinked_list

def generate_input_list(input_str):
    return input_str.split(" ")

if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)
    print(f"25 Blinks Length: {blinks(input_list, 25)}")
    t = 0
    l = len(input_list)
    for i, v in enumerate(input_list):
        print(f"{i + 1} / {l}")
        t += blinks([v], 75)
    print(f"75 Blinks Length: {t}")
    # print(f"75 Blinks Length: {blinks(input_list, 75)}")
