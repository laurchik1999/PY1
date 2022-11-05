from random import randint

def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    size = 15
    uni = []
    while len(uni) != size:
        r = randint(start, stop)
        if r not in uni:
            uni.append(r)
    return uni


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
