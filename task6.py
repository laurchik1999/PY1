list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = 0
max_v = list_numbers[max_i]

for i in range(len(list_numbers)):
    max_r = list_numbers[i]
    if max_r > max_v:
        max_i = i
        max_v = list_numbers[max_i]

max_val = list_numbers
max_val[-1], max_val[max_i] = max_val[max_i], max_val[-1]

print(max_val)
