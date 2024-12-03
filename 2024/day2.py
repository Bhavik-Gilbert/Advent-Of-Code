from inputs.day2 import INPUT_STR

def is_safe_report(report):
    prev_level = report[0]
    safe_lower = 1
    safe_higher = 3
    safe_report = True
    level_direction = None
    report_len = len(report)
    fail_index = report_len
    for level_i in range(1, report_len):
        level = report[level_i]
        level_diff = level - prev_level
        if level_direction is None:
            if level_diff == 0:
                level_direction = 0
            else:
                level_direction = level_diff / abs(level_diff)

        direction_level_diff = level_diff * level_direction
        if direction_level_diff > safe_higher or direction_level_diff < safe_lower:
            safe_report = False
            fail_index = level_i
            break
            
        prev_level = level
    
    return safe_report, fail_index

def safe_reports(reports):
    safe_report_count = 0
    for report in reports:
        safe_report, fail_index = is_safe_report(report)
        if safe_report:
            safe_report_count += 1

    return safe_report_count

def safe_reports_with_dampen_v1(reports):
    safe_report_count = 0
    for report in reports:
        safe_report = safe_reports([report]) > 0

        if not safe_report:
            for level_i in range(len(report)):
                report_perm = report.copy()
                report_perm.pop(level_i)
                safe_report = safe_reports([report_perm]) > 0
                if (safe_report):
                    break
        
        if safe_report:
            safe_report_count += 1

    return safe_report_count

def safe_reports_with_dampen_v2(reports):
    safe_report_count = 0
    for report in reports:
        safe_report, fail_index = is_safe_report(report)
        if not safe_report:
            for level_i_diff in [-2, -1, 0]:
                new_level_i = fail_index + level_i_diff
                report_perm = report.copy()
                report_perm.pop(new_level_i)
                safe_report, _ = is_safe_report(report_perm)
                if safe_report:
                    break
        
        if safe_report:
            safe_report_count += 1

    return safe_report_count

def generate_input_list(input_str):
    unclean_list = input_str.split("\n")
    input_list = []
    for s in unclean_list:
        i_list = []
        s_list = s.split(" ")
        for i in s_list:
            i_list.append(int(i))
        input_list.append(i_list)

    return input_list

if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)
    print(f"Safe reports: {safe_reports(input_list)}")
    print(f"Safe reports with dampening: {safe_reports_with_dampen_v2(input_list)}")