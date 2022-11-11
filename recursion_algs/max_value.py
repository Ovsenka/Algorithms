# get max_value (Task 4.3)

def max_elem(lst: list, max_num: int = 0) -> int:
    if deleted:= lst.pop() > max_num:
        max_num = deleted 
    if len(lst) == 0:
        return max_num
    return max_elem(lst, max_num)

print(max_elem([1, 2, 33, 4, 5, 6, 7, 10, 9, 6]))