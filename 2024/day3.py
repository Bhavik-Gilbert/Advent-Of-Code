from inputs.day3 import INPUT_STR
import re

MUL_REGEX = "mul\([0-9]{1}[0-9]?[0-9]?,[0-9]{1}[0-9]?[0-9]?\)"

def find_valid_muls(input_str):
    return re.findall(MUL_REGEX, input_str)

def find_command_valid_mul(input_str):
    valid_muls = find_valid_muls(input_str)
    mul_split_list = re.split(MUL_REGEX, input_str)

    command_valid_muls = []
    do_command = True

    for i in range(len(valid_muls)):
        mul = valid_muls[i]
        mul_pre_str = mul_split_list[i]
        command_split_list = re.findall("(do\(\))|(don't\(\))", mul_pre_str)
        if (len(command_split_list) > 0):
            command = command_split_list[0][-2]
            do_command = command == "do()"
        
        if do_command:
            command_valid_muls.append(mul)
        

    return command_valid_muls

def multiply_str_list(mul_list):
    total = 0
    for mul in mul_list:
        cleaned_mul = mul.replace("mul", "").replace("(", "").replace(")", "").split(",")
        total += int(cleaned_mul[0]) * int(cleaned_mul[1])

    return total

if __name__ == "__main__":
    valid_muls = find_valid_muls(INPUT_STR)
    command_valid_muls = find_command_valid_mul(INPUT_STR)
    print(f"Multiplication Total: {multiply_str_list(valid_muls)}")
    print(f"Command Multiplication Total: {multiply_str_list(command_valid_muls)}")