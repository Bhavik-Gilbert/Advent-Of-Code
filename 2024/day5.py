from inputs.day5 import INPUT_PAGE_ORDERS_STR, INPUT_PRINTING_PRODUCTION_STR

def generate_input_page_ordering_rules(input_str):
    rules_list =  input_str.split("\n")
    rule_mappings = {}

    for rule_str in rules_list:
        rule_list = rule_str.split("|")
        v = int(rule_list[0])
        k = int(rule_list[1])

        if k in rule_mappings.keys():
            rule_mappings[k].add(v)
        else:
            rule_mappings[k] = set([v])
    
    return rule_mappings

def generate_input_page_productions(input_str):
    orders_str_list = input_str.split("\n")
    orders_list = []
    for order_str in orders_str_list:
        order_list = []
        for order in order_str.split(","):
            order_list.append(int(order))
        orders_list.append(order_list)
    return orders_list

def get_middle_value(l):
    l_len = len(l)
    if l_len % 2 == 1:
        return l[int((l_len/2) - 0.5)]
    else:
        return l[int(l_len/2)]
    
def sum_middle_valid_productions(page_ordering_rules, page_productions):
    middle_sum = 0
    for page_production in page_productions:
        if valid_production(page_ordering_rules, page_production):
            middle_sum += int(get_middle_value(page_production))

    return middle_sum

def sum_middle_invalid_productions(page_ordering_rules, page_productions):
    middle_sum = 0
    invalid_productions = []
    for page_production in page_productions:
        if not valid_production(page_ordering_rules, page_production):
            invalid_productions.append(page_production)
    
    for page_production in invalid_productions:
        fixed_production = fix_production(page_ordering_rules, page_production)
        middle_sum += int(get_middle_value(fixed_production))
        
    return middle_sum

def fix_production(page_ordering_rules, page_production):
    page_production_copy = page_production.copy()
    fixed_page_production = []

    while len(page_production_copy) > 0:
        page = page_production_copy.pop(0)
        page_rule_set = page_ordering_rules.get(page)
        if page_rule_set is None:
            continue
        
        fix_pages = []
        for b_page in page_rule_set:
            if b_page in page_production_copy:
                fix_pages.append(b_page)

        fix_pages = fix_production(page_ordering_rules, fix_pages)
        for a_page in fix_pages:
            fixed_page_production.append(a_page)
            page_production_copy.remove(a_page)
        fixed_page_production.append(page)
    
    if fixed_page_production != page_production:
        fixed_page_production = fix_production(page_ordering_rules, fixed_page_production)
    
    return fixed_page_production
    

def valid_production(page_ordering_rules, page_production):
    page_production_copy = page_production.copy()

    while len(page_production_copy) > 0:
        page = page_production_copy.pop(0)
        page_rule_set = page_ordering_rules.get(page)
        if page_rule_set is None:
            continue
        
        for b_page in page_rule_set:
            if b_page in page_production_copy:
                return False
            
    return True

if __name__ == "__main__":
    page_ordering_rules = generate_input_page_ordering_rules(INPUT_PAGE_ORDERS_STR)
    page_productions = generate_input_page_productions(INPUT_PRINTING_PRODUCTION_STR)
    print(f"Valid middle sum: {sum_middle_valid_productions(page_ordering_rules, page_productions)}")
    print(f"Fixed invalid middle sum: {sum_middle_invalid_productions(page_ordering_rules, page_productions)}")

