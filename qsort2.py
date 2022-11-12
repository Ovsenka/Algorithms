# quicksort from book

def qsort(lst: list) -> list[int]:
    if len(lst) < 2:
        return lst 
    pivot = lst[0]
    less = [i for i in lst[1:] if i < pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)

#better
def qsort_2(lst: list) -> list[int]:
    if len(lst) < 2:
        return lst 
    pivot = len(lst) // 2
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    eq = [pivot] * lst.count(pivot)
    return qsort(less) + eq + qsort(greater)


print(qsort([4, 3, 8, 9, 10, 11]))
print(qsort_2([4, 3, 8, 99, 10, 11]))