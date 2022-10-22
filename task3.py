def delete(list_, index=None):
    if index == None:
        for i, x in enumerate(list_):
            if list_.count(x) > 1:
                index = i
    copy_list = list_[:index] + list_[index+1:]
    return copy_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
