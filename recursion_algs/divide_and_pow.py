# count of items (Task 4.2)

def arr_len(lst: list, length=0) -> int:
    if len(lst) == 1:
        return length+1
    lst.pop()
    length += 1
    return arr_len(lst, length)

print(arr_len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

