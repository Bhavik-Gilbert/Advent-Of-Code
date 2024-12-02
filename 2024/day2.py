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

INPUT_STR = """20 21 24 25 27 29 27
60 61 62 64 64
15 18 21 22 25 26 30
5 8 11 14 16 19 20 26
20 22 20 23 24
89 91 92 95 98 95 96 95
3 5 7 10 11 14 13 13
82 85 83 84 86 90
82 83 84 81 86
27 28 28 30 33
2 4 4 6 9 10 13 11
64 65 65 68 69 72 72
60 63 63 64 65 67 71
14 17 17 20 21 27
16 19 21 25 26
57 59 63 65 62
86 89 91 95 95
2 5 8 10 14 18
10 13 14 17 19 23 29
17 18 24 26 29
28 29 36 38 35
53 56 58 61 68 69 70 70
7 10 13 16 22 24 28
68 70 73 80 81 84 89
28 27 28 30 33 35 37
90 89 91 93 95 94
6 5 7 8 11 11
33 32 34 35 39
20 18 19 21 22 23 26 33
27 26 24 27 28
10 8 5 8 7
10 8 10 13 15 17 14 14
77 75 78 79 80 77 81
9 8 9 6 12
9 8 10 11 14 14 17 18
6 3 4 5 7 7 9 6
92 90 92 94 94 94
88 87 87 90 93 97
58 55 56 57 57 62
12 11 14 15 18 19 23 25
85 82 86 88 86
57 55 58 60 64 64
27 25 28 32 35 36 40
20 19 20 24 29
42 40 41 46 49
4 2 5 12 14 17 15
9 6 8 9 11 17 17
32 31 32 34 40 43 45 49
10 8 14 17 18 24
62 62 65 68 69 72 75
16 16 17 18 21 24 22
4 4 5 8 11 13 13
40 40 42 43 46 49 53
16 16 19 22 29
44 44 46 47 48 46 47 50
26 26 29 31 29 30 32 30
80 80 82 85 84 85 85
6 6 3 4 6 9 13
44 44 46 45 48 51 58
68 68 68 69 72
78 78 79 79 82 79
6 6 8 10 10 10
47 47 50 50 52 54 55 59
2 2 2 4 7 9 10 17
17 17 20 24 26 27 30
84 84 86 90 87
37 37 41 43 43
50 50 51 55 57 60 64
11 11 15 16 18 20 26
27 27 29 31 33 39 41
36 36 43 44 41
51 51 53 55 58 64 64
51 51 56 59 61 63 64 68
70 70 77 79 80 82 83 88
60 64 65 66 67
49 53 54 57 56
80 84 85 86 89 92 92
26 30 32 33 35 38 42
28 32 34 37 39 41 43 48
79 83 84 85 83 86
5 9 11 12 15 12 14 11
58 62 64 62 62
25 29 28 31 34 35 39
38 42 43 40 43 46 52
85 89 91 91 93 95 96
8 12 15 15 12
18 22 24 27 27 30 32 32
33 37 39 40 40 43 45 49
19 23 23 26 31
66 70 71 73 75 76 80 83
46 50 52 55 59 57
46 50 51 53 56 60 62 62
79 83 87 89 91 95
22 26 30 31 34 39
19 23 26 28 31 33 40 41
11 15 17 18 20 25 26 25
45 49 54 55 57 59 62 62
57 61 63 68 69 73
43 47 48 54 59
72 77 79 82 83 84 87 88
6 11 12 13 15 18 21 20
76 81 82 84 87 87
17 23 26 29 30 34
70 75 77 80 83 86 89 94
61 67 65 67 69
77 84 86 89 90 92 89 87
23 30 27 28 29 29
24 29 31 28 32
15 22 24 21 26
15 21 22 23 23 26
84 91 92 93 96 97 97 96
23 28 28 30 31 31
9 14 15 15 16 18 22
50 57 59 60 60 65
79 85 89 91 94 95
6 11 14 18 16
71 76 80 82 84 84
17 24 28 30 33 34 38
40 45 46 50 53 60
70 76 78 81 86 87 88
44 51 56 57 60 63 60
13 18 19 24 26 28 28
81 86 93 94 95 99
1 6 8 11 12 17 22
12 9 8 7 8
65 62 60 58 58
58 55 52 49 47 43
99 98 95 92 91 84
20 17 15 14 11 9 12 9
15 13 11 8 11 10 9 12
86 83 80 81 79 79
76 74 71 69 67 68 64
45 44 41 40 38 37 38 32
48 46 45 45 43 42
92 90 88 85 83 82 82 83
68 66 66 63 60 60
44 41 41 38 37 34 30
90 87 84 84 82 80 77 72
19 18 16 15 11 10
98 97 96 95 91 88 89
54 53 51 50 49 45 45
57 56 52 50 49 45
60 58 56 53 52 48 45 39
89 88 87 81 79 76 75 73
92 89 88 86 83 78 75 78
50 49 47 40 38 36 36
53 50 48 43 42 38
93 90 85 82 77
23 26 25 23 20
68 71 69 68 67 70
38 40 37 35 33 31 29 29
79 81 78 76 74 71 69 65
97 99 98 95 88
10 11 8 6 8 7
79 80 83 81 82
5 8 5 2 3 1 1
47 49 48 50 46
33 34 32 33 30 25
24 27 27 24 22
15 17 14 12 12 13
29 30 27 27 27
93 96 94 94 92 89 85
18 19 16 14 14 9
55 57 56 52 50 48 47
41 44 40 39 36 38
52 55 52 48 45 43 41 41
17 20 18 14 10
70 72 70 66 60
86 87 84 77 75 73
46 47 45 44 41 36 35 36
78 79 78 73 73
80 83 81 74 72 70 68 64
17 18 11 9 4
14 14 11 9 8 6
89 89 86 85 83 81 83
72 72 69 66 66
99 99 97 96 94 90
87 87 85 84 82 81 74
55 55 57 55 52 49
89 89 90 87 88
30 30 27 24 27 26 26
77 77 78 76 75 74 70
67 67 66 69 67 64 57
76 76 75 75 74 73 72 70
24 24 23 23 20 19 20
51 51 51 48 47 44 42 42
92 92 89 86 83 83 79
74 74 74 71 68 62
89 89 87 84 80 78 76 75
79 79 76 72 73
48 48 47 43 43
91 91 88 87 86 84 80 76
90 90 89 85 83 77
29 29 27 26 23 17 14
92 92 86 84 85
38 38 32 30 29 26 24 24
24 24 17 15 11
55 55 48 45 38
83 79 76 74 73 71 70
85 81 79 78 77 79
54 50 48 45 45
50 46 45 44 41 37
85 81 80 79 76 74 68
83 79 78 77 80 78
56 52 55 53 55
43 39 38 41 39 39
51 47 46 48 44
20 16 13 12 14 8
99 95 93 92 92 89
95 91 88 85 83 83 82 84
87 83 82 82 79 77 76 76
91 87 85 84 82 82 80 76
17 13 12 11 9 9 4
43 39 38 37 33 32 30 28
58 54 53 49 48 47 49
93 89 88 84 81 78 78
83 79 78 76 75 71 70 66
89 85 81 79 76 70
91 87 82 81 80 79 77
87 83 76 75 73 75
28 24 18 16 15 13 12 12
77 73 72 66 63 62 58
85 81 79 72 69 66 61
34 28 26 25 23 20
81 76 74 71 68 67 66 69
94 87 85 82 79 77 77
93 86 83 80 76
44 38 35 32 30 24
45 39 36 39 38
18 13 14 11 14
51 44 46 44 44
33 27 30 29 27 23
44 38 35 34 36 30
38 31 28 28 26 23 21
90 83 82 80 80 82
51 46 45 42 40 37 37 37
17 10 9 6 6 2
83 77 76 73 73 72 71 66
64 58 54 52 51 50
58 52 49 45 42 44
35 30 26 23 23
35 28 24 22 21 20 16
31 26 22 21 18 17 14 9
20 13 11 6 3 2 1
92 86 83 80 77 71 72
78 72 69 62 60 59 59
56 51 48 41 38 34
72 65 63 61 58 52 50 45
36 34 34 35 39
62 62 59 61 61
23 17 16 15 15 14 11 10
16 20 22 24 31 34 38
1 7 9 8 10 11
81 78 80 79 81 82 87
15 18 20 21 23 26 30 34
20 20 17 14 13 16 14 10
7 11 13 16 15 15
39 39 39 36 33 33
39 43 45 46 51 53 60
21 15 13 11 8 7 6 2
15 20 22 23 25 22 23 29
34 34 28 25 28
32 30 27 27 24 25
52 54 51 49 47 46 45 46
46 49 49 48 47 43
42 43 44 46 48 50 54
90 90 91 91 93 94 94
96 93 90 83 82 80 78 76
49 56 57 59 62 66 66
71 69 70 74 75 76 83
54 52 54 57 63 64 65 70
78 71 66 65 62 61
67 71 73 74 81 82 82
23 17 16 16 11
88 84 83 79 73
59 59 63 66 66
66 62 62 59 55
69 71 68 66 63 62 55 50
48 48 45 43 41 35 32 26
19 15 14 11 9 9 9
60 59 58 55 51 45
10 14 17 17 20 23 27
77 77 74 72 73 71 70 63
73 73 72 75 75
15 22 24 23 25 27 28 28
90 90 92 91 93
64 67 67 65 64 62
97 93 91 89 85 88
42 42 38 35 32 32
76 74 77 74 71
71 68 67 64 63 62 64
13 15 13 11 7 6 5 2
67 67 71 72 73 70
20 17 19 19 20 21
69 74 75 76 79
39 35 33 30 28 26 29 29
68 66 63 62 59 52 52
25 19 17 14 13 9 7 10
53 53 56 63 63
43 39 37 34 33 31 27
31 33 35 35 36
32 35 38 39 39
28 30 33 36 42 39
51 49 52 55 58 63
20 16 12 9 5
38 33 30 29 26 23
56 56 57 61 64 66 68
57 60 63 62 65 72
26 19 18 17 16 13 9 7
27 33 36 41 43 46 50
85 85 86 89 92 94 92
43 44 51 54 57
68 74 78 81 84 86 88 92
54 58 60 62 64 64 66 66
32 28 26 24 26 24 22 15
4 3 4 7 7 10 17
6 11 13 15 17 23
30 34 36 40 40
83 87 90 91 93 91
58 58 56 55 54 51 52 54
64 66 65 63 56
14 17 15 15 16
22 18 16 14 13 11
66 61 62 61 63
68 67 64 66 67 71
25 31 34 32 31
58 62 63 64 65 67 69 75
44 45 43 36 35 34 31 27
55 60 67 69 68
31 29 28 31 33
69 75 77 79 82 82 89
90 90 92 94 94 98
57 57 55 53 56 54
42 36 35 38 37 36 33 26
57 57 60 65 67 68 72
55 58 57 52 49 47
88 88 90 91 91
51 51 54 54 55 56
18 22 25 27 30 33 37 43
58 65 66 69 72 74 78 76
40 39 36 32 29 28 25
70 66 64 61 60 63
13 15 18 21 24 27 34 34
76 79 72 71 70 73
72 68 66 64 64 61
13 12 13 15 17 18 22 26
86 82 82 81 80 79 77 71
37 37 35 34 29 28 28
61 62 65 68 68 68
24 25 23 24 24
81 81 80 77 71 70 69 65
27 27 34 36 37 40 43 50
52 49 47 50 49 48 47 47
66 69 76 79 83
54 54 52 47 44 43 40
85 87 87 86 84 82 80 75
21 15 11 8 7 3
54 54 53 53 51 49 45
56 49 52 50 47 44 44
85 83 80 82 78
53 54 58 60 62 63
86 89 88 89 85
44 50 53 53 56 58
44 48 50 53 53 56 62
14 16 14 12 10 6
57 56 58 59 62 66 67 67
83 82 84 87 89 91 91 91
20 13 9 7 4 2 2
3 4 6 6 8 9 11 16
83 83 87 88 93
60 61 64 67 70 73 76 74
37 36 41 44 46 48 49 49
91 91 88 87 86 86 84 81
66 68 61 59 56 56
11 9 12 14 18 19
39 34 31 31 30 33
33 33 31 30 28 26 19
25 27 24 22 18 17 15 17
52 52 54 53 52
20 25 25 26 30
33 36 35 32 29 27 27
34 30 27 25 25
10 8 9 10 13 10 11 14
34 41 44 45 51 51
4 4 6 7 10 14
34 31 34 38 40 41 44 43
17 13 10 9 10 9 6 5
75 71 70 65 61
56 55 53 52 49 46 42 38
56 52 45 42 40 39 38 39
17 21 24 24 25 28
59 53 51 50 51 48 47 43
95 89 86 82 76
12 12 10 7 5 3 3
22 24 23 24 23
82 80 79 78 75 75 75
64 65 66 69 72 76 82
93 87 85 85 85
22 22 22 20 18 20
73 72 74 77 80 83 85 88
42 44 46 45 43
15 15 18 17 18 19 24
39 43 44 43 42
79 83 84 88 85
16 20 23 20 24
16 13 11 8 9 8
22 25 25 26 28 32
43 47 49 50 52 51 52 57
19 16 15 13 13 9
76 83 84 82 86
24 24 25 28 30 30 33 38
20 16 15 10 7 7
19 24 27 31 34 36 41
43 47 51 52 53 55 56
63 62 64 66 72 73 77
10 8 11 12 14 16 18 18
70 70 69 68 65 61
6 10 12 16 20
81 85 86 87 89 92 92
51 48 46 45 42 41 38 34
24 29 31 32 33 30
68 68 68 71 74 77 80 77
5 7 8 10 12 16 18 15
59 59 62 63 66 67 68 71
18 21 24 31 32 33 36 42
22 26 29 30 34
38 42 44 45 47 49
44 38 35 32 25 20
20 14 12 11 11 9 7 3
57 61 62 64 66 71 70
75 75 71 69 66
30 25 22 17 16 15 11
34 34 30 27 25 22 25
13 16 15 12 10 6 2
35 34 36 35 30
11 11 10 9 8
53 51 48 42 41 42
84 83 84 82 82
90 92 90 89 89 89
72 76 76 78 80 78
81 86 88 91 94 95 95 92
30 32 34 36 33 35
22 26 28 31 32 38 40
79 73 66 63 62 65
47 43 40 34 32
20 17 18 21 25
63 60 66 69 72 73
71 76 78 81 85
29 31 31 32 34 31
35 36 35 33 30 26 19
64 68 70 71 68 70 72 73
66 60 55 53 50 49 46 46
17 18 15 12 10 6 6
79 75 72 69 65 62
7 12 15 19 22 25
42 42 38 37 33
12 8 5 5 4 3 2 5
71 68 66 65 64 63 62 62
6 3 5 8 10 12 11
93 86 85 84 82 84
31 32 30 31 31
53 53 56 59 62 61 65
26 26 29 35 37
13 14 13 15 19
33 30 31 33 35 35 34
53 60 67 68 71 72
93 91 87 85 84 83 84
38 38 40 42 43 46 48 53
33 39 41 44 51 58
43 43 40 36 34 29
50 52 54 53 52 45
26 19 17 14 14
66 62 59 60 61
9 12 16 19 22 22
89 88 86 83 82 80 78
25 26 29 32 33
61 58 56 54 52
15 12 10 7 6 5
44 41 39 37 35 33
80 79 76 75 72
55 54 51 48 45
72 69 66 63 62 61
49 50 53 54 57 59 61
88 86 84 81 78 76 74 73
45 44 41 38 37 36 35 32
77 80 83 86 88 90 92
92 89 88 85 84
48 49 51 54 56 58
92 91 88 85 83 82 80 77
28 27 26 23 22 19 17
28 27 24 21 19 18 16
58 61 63 64 66 67 69 71
52 55 57 60 62 64 65 67
20 19 16 15 12
28 27 26 23 20 17
66 64 61 58 57
27 24 22 19 16 14 13 10
16 18 20 23 25 28 30 32
85 87 88 90 91 92
81 79 77 76 74 72
30 31 33 35 38 40 41
9 10 12 13 16 17 19
32 30 28 26 24 22
40 43 46 49 50 51 53
15 16 19 22 23 25 28 31
53 51 48 46 43 41
65 66 69 72 75
33 34 35 36 37 39 42
67 70 72 74 77 78
23 22 20 19 18 16 15 14
22 21 18 17 15 14 12
14 13 10 9 8 5
35 34 32 29 26 23 22 19
86 84 82 79 78 77 76 74
34 37 39 40 41 44 46 48
66 68 71 74 77 78 79
73 71 70 69 67
47 46 44 43 41 40
22 21 19 17 16 15
78 80 83 86 89 90 91 93
41 38 36 33 32 29 27
70 72 73 76 79 80 83 86
63 64 66 69 70 73 74
26 25 22 19 16 14 13
42 39 37 35 34 31
3 6 8 9 12 15 18
58 56 55 52 51 48 46 44
9 10 12 14 16 18 19 21
93 91 90 88 86 85 82 79
86 84 83 80 78 77 76
71 68 65 64 61
53 51 50 48 46 43
34 37 38 41 42
63 60 58 55 54 52 49
40 37 36 35 33 30
36 37 40 42 45 47 49 50
58 60 63 66 69
8 10 13 15 18 19 21 23
3 4 7 8 10 12 13 15
26 23 22 21 20
85 87 90 93 94
12 15 18 21 22 23 24
89 91 93 95 96 97
50 49 46 44 42 41 38 35
43 41 40 38 35 34 33
65 66 68 70 72 73 74
20 17 15 14 11
63 65 68 69 70 72 74
66 65 64 63 61 59
31 32 33 35 37 38 39
48 47 44 42 41 39
38 40 41 44 47 48
92 90 89 87 85
62 61 60 59 57 54 51
17 20 22 24 27 29 31
89 87 86 83 81 78
47 50 53 54 57
22 19 16 13 11 10
50 48 45 44 41 39 36 33
75 78 81 82 85
78 76 75 72 69
45 43 42 41 39 38
45 48 50 53 54 56
35 34 31 30 28 27 24
54 57 60 62 63
50 51 52 55 57 58 59 61
49 47 46 44 43
51 49 46 43 41 38 37 34
43 42 39 37 35 33 31 28
31 33 36 37 39
24 25 27 28 29 31 33 34
6 9 10 13 14 17 20 21
79 80 82 83 86 89 90
29 28 25 22 19 17
56 53 52 51 50 49 48 47
10 7 6 5 4 3 1
87 88 90 91 92
12 9 6 4 3 1
19 17 14 12 10
22 24 26 29 31
96 94 91 90 87 86
37 40 41 42 43 46 49 51
39 36 35 33 32 29
24 27 28 29 32 33 35 38
42 39 36 33 31
68 69 71 73 74 76 79 80
43 44 46 47 49 51 53
44 41 40 38 37 35
66 67 69 71 73 74
48 46 43 40 38 35
24 23 22 20 19 18 16
27 30 31 33 34 35
74 77 78 79 80 81
7 10 13 16 19
7 9 11 12 13 16
50 48 47 44 43 40 38 36
24 22 19 18 15 14 13
31 30 27 26 25 23
65 62 60 58 55 53 50 49
68 66 63 62 60 59 58 55
36 33 31 30 27 26 23
42 41 40 37 34 31 29 26
31 29 27 25 24
86 84 81 78 77 75 73 72
9 12 14 17 19 20 22
64 65 67 69 71 74 77 79
94 93 90 87 86
50 47 44 41 40 38 37
15 13 12 11 10 8
36 33 30 27 26 25 22 19
80 81 82 83 84 87
14 11 10 9 6
12 11 9 8 6 4
37 40 43 44 46 49 50
34 35 37 39 41 44
80 81 82 85 87
55 58 59 60 63
57 59 61 63 66 67
83 84 85 87 89 90
86 84 82 80 78 75 74
60 59 56 53 51
27 26 23 21 20 19
13 14 17 19 20
66 65 64 61 60 57 56 54
62 63 65 67 69
85 86 89 91 94
6 7 9 11 12 15 17
9 11 14 17 20 21
86 83 80 79 78 75 72 71
52 53 56 57 60 63 64 66
38 35 33 31 30 28 25
47 44 42 39 37 34 31
97 94 93 91 89 88
68 69 72 74 76 77 79
69 66 65 64 61 58 57
38 36 33 30 27 25 22
11 14 16 18 20 22
35 32 30 27 24 21 19 16
86 87 89 90 91 92 93
7 9 11 13 15
78 81 83 85 87 88 91
48 49 51 52 53 56 57 59
36 39 42 43 44 45 46 47
48 51 52 53 55 56
79 76 75 73 71 68 65 63
15 14 13 10 7 5 4 2
83 82 80 78 77 74
19 18 16 15 12 9 7 4
95 93 90 87 84 82 79 76
49 46 44 42 41 39 37 36
49 48 47 46 44
35 36 39 41 43
2 4 5 8 9 10 12 14
25 22 20 18 16 14
67 64 61 59 56
64 67 70 73 75 76 78 81
54 51 49 46 43 42 39 38
95 94 93 91 88 87 84 81
64 65 68 70 71 74 76 77
73 71 68 66 63 61 59
81 79 78 75 74 71 69 67
62 60 58 55 54 53 50
79 82 83 84 85
52 55 56 58 59 60 62 65
44 45 46 47 48 50 52 55
42 44 47 48 51
54 52 50 49 48
17 15 13 11 9 8 6 3
76 79 81 82 84 85
60 63 64 67 69 70 73 75
18 19 20 22 24
25 28 30 32 35 38 40 42
66 67 69 71 72 73 75
17 20 23 26 29 32 34 37
78 76 75 72 70
53 51 48 46 43 40 37
94 91 88 86 85 82 81 78
71 73 74 75 76 78 80 82
80 78 75 73 71 69 66 63
37 36 33 31 30 29 28
35 38 40 43 46 47
35 38 41 42 44
34 33 31 28 27 24
82 79 78 77 76 74
27 29 31 33 36 37 40
17 18 19 22 25 27 30 31
75 77 78 79 82 84
21 19 18 15 12 10
49 52 54 57 60 61 62
51 54 55 58 60 62
69 68 65 62 59 57 55
64 61 60 57 55 53 50
74 71 69 66 64 61 59
55 53 50 49 47 46 45 43
69 72 73 76 78 81 82
74 72 71 69 66 64 61 58
32 29 28 25 23 21 18 17
79 82 85 88 89 92 93 95
49 52 54 55 58 60 62 65
88 85 84 81 78 77
25 26 29 31 32
66 69 70 71 73 76
49 51 53 54 57 58
36 38 41 43 44 45 48 49
97 96 93 90 88 86 85 83
41 40 39 37 35 32 29
57 59 60 61 62 64 67
37 35 34 32 29
52 51 48 45 44 43
12 13 14 15 16 19
8 9 11 12 13 14 17 18
71 73 74 76 77 80
34 32 30 28 27 24
41 43 44 46 49 51
17 19 21 24 27 29 32
22 20 19 16 13 10 9 6
94 92 90 89 86
38 35 33 32 30 28 25
28 29 30 33 36 37 38
91 88 87 86 83 82 81 79
37 38 39 41 44 46
80 77 75 73 72 70 69
76 77 79 82 84 85
22 25 27 29 32 33
57 55 54 52 51 49 46 45
66 67 70 71 74
65 62 60 59 58 57 56
10 9 8 6 3 2
66 63 61 59 57 54 52
42 45 47 49 52
86 83 80 79 77
57 59 62 63 66 68 69
13 14 17 20 21 22
60 58 56 55 52
89 88 86 83 81 79
76 73 72 69 67 66
42 39 38 36 35
72 74 77 80 82 83 84 87
56 57 59 62 65 67
45 46 47 48 49 51 54
76 77 80 83 86 87
14 11 9 6 3
75 78 81 84 87 89
57 59 62 63 66 67 68 69
54 57 60 62 63 65 66 69
29 30 32 34 37 40 41
77 79 81 84 86 88
37 39 40 42 43
82 79 76 74 71 70 68
46 44 43 42 41 40 39 38
9 10 12 14 17 20
48 49 51 52 53 54
44 46 49 51 52 55
32 31 29 28 26
44 46 48 50 52 54
57 58 61 63 65
40 42 45 46 49 51
62 59 56 53 52
52 53 55 56 58
64 65 66 69 71 72 73 74
31 29 26 24 23
48 46 45 43 40
29 31 34 35 38
67 68 69 72 74 76 78
66 64 62 61 60 57 54
38 37 34 33 32 29 28
7 9 12 14 17 20 21
73 72 71 69 68 65 62
15 16 18 19 20 21 23 25
90 89 86 84 81 78 76
75 78 79 80 81 82
95 94 91 90 89
90 92 94 95 96 97 99
73 70 68 67 64
19 17 15 13 11 10 7 4
76 79 82 85 87 90
75 76 78 81 83 85
77 79 81 83 85
89 87 86 84 81 80 79 76
58 61 62 63 66 67 69
20 23 25 27 30
42 40 38 36 34 32
68 65 64 63 62
35 37 40 41 44 45
35 36 39 41 42
66 63 61 60 58 57 54
70 67 64 61 58 55
88 90 93 95 97 98 99
75 76 79 82 84 85 86
83 80 77 75 72 70 69
76 74 72 70 68 67
14 15 18 20 22 25 26 27
15 17 18 19 22
10 9 8 7 4
16 19 21 24 27
36 35 32 30 27 25
40 37 34 32 31
42 39 38 36 34
76 74 73 70 67 65 64 62
30 28 25 22 19 17 15 14
58 57 54 51 49 48 45 42
18 17 16 15 14 13
30 29 26 25 22
62 63 66 67 68 69 72
69 72 75 76 79
23 21 20 17 14 13 11 8
35 34 31 30 27
90 88 85 84 81 78
98 95 93 91 88
81 80 78 76 73 70 68
77 78 81 82 83 86
75 77 78 79 81
21 20 17 15 13 12
41 43 44 46 49 51 53 56
32 34 35 38 41 43 44
89 87 84 82 79 77
35 38 39 40 43 46 47
35 37 40 42 45
80 79 77 74 72 70 69
67 68 71 72 73 75 76 79
9 10 13 15 16 19 22
31 32 34 36 37 39
81 78 76 75 72 69 68 66
10 11 13 16 19 21 24
57 60 61 64 66
62 59 58 56 55 54 51
1 3 6 7 9 10 12
13 16 17 18 19 20 21 23
51 50 48 46 45
32 35 38 41 43 45
91 90 87 84 81 79 77 74
64 67 69 70 72 73
37 40 42 43 45
48 51 54 55 58 61
46 49 51 53 54
43 46 49 50 53
51 54 56 59 61
57 60 62 63 64 66 67 69
44 42 41 40 38
53 51 48 47 45 42 40 38
72 73 74 76 79 81
25 22 19 17 15 13 10
22 19 18 17 15 14 12
37 35 34 32 31
76 74 72 70 67 64 61 59
60 61 64 66 68 70
8 10 12 13 16
99 97 95 92 89 86 84
87 84 83 82 80 79
80 78 75 74 72 70 68
86 84 81 79 78 77 74 73
87 88 89 91 92 94 97
39 36 35 33 31
52 49 47 45 44 43
45 42 40 39 37 34
68 70 72 74 77
87 89 90 91 94
61 58 56 53 51 48 45 43
75 78 81 84 87 90
44 47 50 52 54 57
82 85 88 91 93 94
3 5 8 11 14 17 18 19
53 50 49 46 43
87 85 82 80 77 75 72 71
70 67 65 64 63 60 59
28 29 31 33 36 38
76 77 78 80 83 86 87 89
41 42 45 46 48 51
47 46 43 42 40 37 36
86 85 82 80 79 78 77 75
32 29 28 27 24 21
3 5 8 9 10 12
11 14 15 18 20 21
28 31 34 36 39
25 24 22 21 20 17
67 68 69 71 73 75 77
48 46 43 42 39 38 37
23 26 27 30 33 36
68 70 73 74 75 76 77
83 85 88 91 93 96
55 54 51 50 48
46 48 49 51 52 55 58 59
35 37 40 41 44
61 64 65 66 67 68 70 73
3 4 7 10 11 13 16
99 97 94 93 91 90
45 42 40 37 34
26 27 30 32 33 36 37
34 32 31 28 25 22
91 92 94 97 98 99
55 58 60 63 64 66 67 70
15 17 18 21 22
58 60 63 64 65 66
28 31 34 35 37 40 42
63 66 69 70 71 72 75
51 53 54 55 57 58 59
79 82 85 88 91 93 94
20 22 24 27 28
67 66 63 61 60 58 55
46 43 41 40 37 34 31 30
38 35 33 32 29 28 26 23
58 56 55 54 53 50
83 86 89 92 95 96
12 14 16 17 18 20 21
68 65 63 62 60 59 57 54
90 88 85 84 82 81 80 79
59 56 53 52 50 48 47
27 28 31 32 35 36 37
81 79 77 74 73 70
56 55 54 53 52 50 49
40 41 44 46 49
71 74 77 80 82 84 85 86
40 43 46 49 50
69 67 66 63 60 59
35 36 38 40 42 43 45
20 18 17 15 13 11 10 7
32 29 27 24 23 22 20 18
77 78 80 81 82
25 23 21 19 16 15
85 86 87 88 90
18 20 21 24 26 27 30
1 4 5 7 10
81 82 85 87 90 93 96 98
27 24 21 18 15
82 85 87 89 92 94 96 99
49 51 52 53 56 59 60
80 79 76 73 71 69 66
66 63 62 59 56
65 64 61 58 56 55 52
45 48 49 52 54 55 58
82 81 78 77 75 73 71 70
66 64 63 60 58 57 55
62 59 56 54 51 49 46
7 6 5 4 2
32 31 28 25 22 19 18
78 80 83 84 85 88 89
56 57 59 61 63
53 50 48 47 46 45 44 42
83 82 81 80 78
28 31 32 35 37 38 40
4 5 7 9 10 12 15
44 47 48 50 53 54
51 53 54 56 57 60
2 5 7 10 13 15 17 20
24 25 26 28 31 33
24 27 29 32 35 37
87 88 90 92 95 98
47 49 50 53 55 57 60
87 85 83 82 81 80 78
3 5 8 10 12 14 16 17
27 29 31 34 35 36 37 39
10 12 15 16 18 20 21
36 37 39 42 43 44
75 76 77 80 82 83
76 77 78 80 81 84 85 86
23 21 20 17 15 12 10 8
86 83 80 78 77 74 72
82 80 79 76 73 72
62 65 66 67 70
94 92 90 88 85 83 81 80
47 45 43 42 40 37 36
32 35 37 40 41 42 43
77 78 81 83 85 86 89 90
20 19 18 16 13
37 40 42 45 46 49
31 32 35 36 38 39
62 64 66 68 69 70 71 73
83 84 87 90 91
4 5 7 9 12 13 16
59 60 61 64 65 68
61 59 56 54 52 49 48 45
26 25 23 22 19 16
69 72 74 76 77
75 78 79 82 83 85 86
67 68 69 70 72 74 75 78
68 65 62 61 59
20 21 22 23 24 25 27 29
30 28 26 25 23 21
72 70 68 65 62 59 56
69 70 72 75 78 79
12 14 17 18 20 21 22
13 16 18 20 21 22 24 27
82 83 86 87 89 90 93
45 48 51 54 55 58
77 78 81 82 85 88 90 93
87 88 89 91 94 97
44 42 41 38 35 33
39 36 34 32 31
37 39 41 42 45 48 51 54
72 75 78 79 81
64 67 70 71 73 76
60 57 55 54 51 48 46
29 28 26 23 21 18 15
16 15 12 9 8
71 70 67 64 62 61
6 8 9 10 12 13 16 19
42 40 38 35 34 33
80 82 83 85 87
41 38 37 35 34 33 30
54 57 59 61 64 65 67"""

if __name__ == "__main__":
    input_list = generate_input_list(INPUT_STR)
    print(f"Safe reports: {safe_reports(input_list)}")
    print(f"Safe reports with dampening: {safe_reports_with_dampen_v2(input_list)}")