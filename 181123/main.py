# Recriar todos estes metodos de array na mão:
# Clear
# Count
# Index
# Copy
# Insert
# Pop (delete last)
# Pop (delete return by index)
# Len


def my_clear():
    return []


def my_count(array, counting):
    ocurrences = 0
    i = 0
    while i < len(array):
        if array[i] == counting:
            ocurrences += 1
        i += 1
    return ocurrences


def my_index(array, indexing):
    i = 0
    while i < len(array):
        if array[i] == indexing:
            return i
        i += 1


def my_copy(array):
    return array


def my_insert(array, element, position):
    new = []
    i = 0
    while len(new) < (len(array) + 1):
        if i == position:
            new.append(element)
        new.append(array[i])
        i += 1
    return new


def my_pop(array, element=-1):
    array.remove(array[element])
    return array


def my_len(array):
    lenght = 0
    for i in range(len(array)):
        lenght += 1
    return lenght
