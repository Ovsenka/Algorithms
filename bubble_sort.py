''' Алгоритм пузырьковой сортировки (простыми обменами)'''
''' Эффективен только для небольших массивов '''
''' Сложность O(n^2) '''
from datetime import datetime as dt
from random import randint

a = [randint(1, 10000) for _ in range(2000)]
N = len(a)
t = dt.now()

for I in range(0, N):
    flag = 0
    for J in range(1, N-I):
        if a[J] > a[J+1]:
            a[J], a[J+1] = a[J+1], a[J]
            flag = 1
    if flag == 0:
        break
    
tt = dt.now() - t
print(a)
print("Time:", tt)
