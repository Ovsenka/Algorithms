''' Быстрая сортировка O(n*logn)'''
''' '''

from random import choice,randint
from datetime import datetime as dt

def partition(A: list[int], start, end):
    pivot = A[(start+end)//2]
    i = start
    j = end
    while True:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]
        i +=1
        j -= 1

def quicksort(A: list[int]):
    if len(A) <= 1:
        return A
    P = choice(A)
    L = [el for el in A if el < P]
    M = [P] * A.count(P)
    H = [el for el in A if el > P]
    
    return quicksort(L) + M + quicksort(H)

def quicksort_(A: list[int], start, end):
    if start < end:
        p = partition(A, start, end)
        quicksort_(A, start, p)
        quicksort_(A, p+1, end)

A = [randint(1, 10000) for _ in range(10000)]

''' Effective'''
t = dt.now()
quicksort_(A, 0, len(A)-1)
print(A)
print("Time: ", dt.now() - t)


''' Non-effective'''
t = dt.now()
print(quicksort(A))
print("Time: ", dt.now() - t)


