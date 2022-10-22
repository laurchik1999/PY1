def get_count_char(str_):
    str_r = str_.lower()
    dict_ = {}
    if not str_r:
        return False
    for i in range(len(str_r)):
        if str_r[i].isalpha():
            count = dict_.setdefault(str_r[i], 0)
            count += 1
            dict_.update({str_r[i]:count})
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
