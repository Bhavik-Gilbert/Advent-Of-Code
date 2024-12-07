from inputs.day7 import INPUT_STR

VALID_OPERATORS_1 = ["+", "*"]
VALID_OPERATORS_2 = VALID_OPERATORS_1 + ["||"]

def perform_operation(val1, val2, operator):
    if operator == "+":
        return val1 + val2
    elif operator == "*":
        return val1 * val2
    elif operator == "||":
        return int(str(val1) + str(val2))
    
    raise Exception("Invalid operator provided")

def generate_input_list(input_str):
    input_str_list = input_str.split("\n")
    input_list = []

    for equation_str in input_str_list:
        equation = equation_str.split(":")
        answer = int(equation[0])
        values = [int(v.strip()) for v in equation[1].split(" ") if v != ""]
        input_list.append((answer, values))
    
    return input_list

def valid_equation_totals_1(input_list):
    total_valid_sum = 0
    for answer, equation in input_list:
        if valid_equation_1(answer, equation):
            total_valid_sum += answer

    return total_valid_sum

def valid_equation_1(answer, values):
    if len(values) < 2:
        return False
    
    if len(values) == 2:
        val1 = values[0]
        val2 = values[1]
        for operator in VALID_OPERATORS_1:
            current_answer = perform_operation(val1, val2, operator)
            if current_answer == answer:
                return True
        
        return False

    val1 = values[0]
    val2 = values[1]
    for operator in VALID_OPERATORS_1:
        sub_answer = perform_operation(val1, val2, operator)
        if valid_equation_1(answer, [sub_answer, *values[2:]]):
            return True

    return False

def valid_equation_totals_2(input_list):
    total_valid_sum = 0
    for answer, equation in input_list:
        if valid_equation_2(answer, equation):
            total_valid_sum += answer

    return total_valid_sum

def valid_equation_2(answer, values):
    if len(values) < 2:
        return False
    
    if len(values) == 2:
        val1 = values[0]
        val2 = values[1]
        for operator in VALID_OPERATORS_2:
            current_answer = perform_operation(val1, val2, operator)
            if current_answer == answer:
                return True
        
        return False

    val1 = values[0]
    val2 = values[1]
    for operator in VALID_OPERATORS_2:
        sub_answer = perform_operation(val1, val2, operator)
        if valid_equation_2(answer, [sub_answer, *values[2:]]):
            return True

    return False

if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)
    print(f"{valid_equation_totals_1(input_list)}")
    print(f"{valid_equation_totals_2(input_list)}")