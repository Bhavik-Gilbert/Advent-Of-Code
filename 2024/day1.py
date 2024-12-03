from inputs.day1 import INPUT_STR

def listdiff(l1, l2):
    l1.sort()
    l2.sort()

    list_len = len(l1)
    if (list_len != len(l2)):
        raise Exception("Lists are not the same length")
    
    diff = 0
    for i in range(list_len):
         diff += abs(l1[i] - l2[i])

    return diff

def listsim(l1, l2):
    sim_dict = {}
    sim = 0

    for v in l1:
        v_sim = sim_dict.get(v)
        if v_sim is None:
            v_sim = (l2.count(v) * v)
            sim_dict[v] = v_sim
        sim += v_sim
    
    return sim

def generate_input_lists(input_str):
    input_list = input_str.replace("\n", "   ").split("   ")

    l1 = []
    l2 = []
    for i, v in enumerate(input_list):
        v = int(v)
        if i % 2 == 0:
            l1.append(v)
        else:
            l2.append(v)
    
    return l1, l2

if __name__ == "__main__":
    list1, list2 = generate_input_lists(INPUT_STR)
    print(f"List difference: {listdiff(list1, list2)}")
    print(f"List similarity: {listsim(list1, list2)}")