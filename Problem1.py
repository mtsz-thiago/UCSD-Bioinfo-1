from thiago_lib import KmersStats

with open("./data/dataset_2_6.txt") as f:
    lines = f.readlines()
    text = lines[0]
    pattern = lines[1]

    print(KmersStats(text).pattern_count(pattern))