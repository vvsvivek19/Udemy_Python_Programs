import statistics as s

large_sample_list = [
    4, 5, 1, 2, 7, 5, 3, 6, 5, 8, 6, 5, 2, 4, 5, 7, 5, 3, 2, 4, 6, 5, 8, 6, 5,
    10, 9, 3, 4, 5, 2, 7, 8, 5, 6, 1, 9, 3, 7, 5, 2, 6, 10, 8, 4, 5, 7, 3, 9, 2,
    4, 6, 8, 5, 1, 7, 3, 2, 9, 6, 5, 4, 10, 8, 3, 7, 5, 2, 6, 9, 1, 4, 5, 8, 7, 3,
    6, 2, 9, 5, 4, 7, 8, 3, 6, 5, 2, 10, 4, 7, 5, 3, 8, 6, 9, 2, 4, 5, 7, 1, 8, 3,
    6, 9, 2, 4, 5, 10, 7, 3, 8, 6, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10,
    6, 2, 8, 4, 9, 5, 7, 3, 6, 1, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3,
    6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3,
    10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 1, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7,
    3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7,
    3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7,
    3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7,
    3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5,
    7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5,
    7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5,
    7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5,
    7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4,
    5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4,
    5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4,
    5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9,
    5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9,
    4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9,
    4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9,
    4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4,
    9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2, 9, 4, 5, 7, 3, 10, 6, 8, 2,
    9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5, 7, 3, 6, 10, 8, 2, 9, 4, 5, 7, 3, 1, 6, 8, 2,
    9, 4, 5, 7, 3, 10, 6, 8, 2, 9, 4, 5, 7, 3, 6, 2, 8, 4, 9, 5]

print(len(large_sample_list))
print(s.stdev(large_sample_list))
