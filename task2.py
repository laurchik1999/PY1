def get_count_char(str_):
    str_r = str_.lower()
    c = 0
    dict_ = {}
    if not str_r:
        return False
    for i in str_r:
        if i.isalpha():
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
            #count = dict_.setdefault(i, c)
            #count += 1
            #dict_.update({i:count})
    print("Исходный словарь:", dict_)
    dict_p = proc(dict_)
    print("Словарь с процентами:", dict_p)

def proc(dict_p):
    sum_ = 0
    dict_proc = dict_p
    for key_ in dict_p:
        sum_ += dict_p.get(key_)
    for key_p in dict_proc:
        dict_proc[key_p] = round(dict_proc.get(key_p) / sum_ * 100, 2)
    return dict_proc

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
