# coding=utf-8
import random
import sys
sys.path.append('../sort/')

from merge_sort import merge_sort

def binary_search(A, p, q, v):
    """Binary Search the value v in the array A

    Args:
        A: the sorted array (incremental order)
        p: the start index of A
        q: the end index of A
        v: the searched value

    Returns:
        the index i such that A[i] = v or the special value "NIL" if v does not
        appear in A.
    """
    if A[p] > v or A[q] < v:
        return "NIL"

    mid = (p + q) // 2
    if A[mid] < v:
        return binary_search(A, mid+1, q, v)
    elif A[mid] > v:
        return binary_search(A, p, mid-1, v)
    else:
        return mid


if __name__ == '__main__':
    random.seed(1996)
    A = [random.randint(-100, 100) for _ in range(100)]
    A = merge_sort(A, 0, len(A)-1)
    print('Original array: {}'.format(A))

    ret = binary_search(A, 0, len(A)-1, 70)
    print('Search result index: {}'.format(ret))
