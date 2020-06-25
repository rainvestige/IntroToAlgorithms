# coding=utf-8
import math
import time

COUNTER = 0

def  merge(A, p, q, r):  # p = 0 to ...
    """Merge two subarrays(A[p, q], A[q+1, r]) into one sorted array A[p, r]

    Args:
        A: the main Array 
        p: the start index of first subarray
        q: the end index of first subarray and start index right before the 
           second subarray
        r: the end index of second subarray

    Returns:
        the merged array A
    """
    n1 = q - p + 1
    n2 = r - q
    L = [0 for _ in range(n1+1)] 
    R = [0 for _ in range(n2+1)]
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    global COUNTER
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            COUNTER += n1 - i
            A[k] = R[j]
            j = j + 1

    return A


def merge_without_sentinel(A, p, q, r):
    """Merge two subarrays(A[p, q], A[q+1, r]) into one sorted array A[p, r]
        without sentinels

    Args:
        A: the main Array 
        p: the start index of first subarray
        q: the end index of first subarray and start index right before the 
           second subarray
        r: the end index of second subarray

    Returns:
        the merged array A
    """
    n1 = q - p + 1
    n2 = r - q
    L = [A[p+i] for i in range(n1)]
    R = [A[q+j+1] for j in range(n2)]
    i = 0
    j = 0
    k = p
    global COUNTER
    # either array L and R has had all its elements copied back to A
    while (i < n1) & (j < n2):
        if L[i] > R[j]:
            COUNTER = COUNTER + (n1 - i)
            A[k] = R[j]
            j += 1
        else:
            A[k] = L[i]
            i += 1
        k += 1

    # coping the reminder of the other array back into  A
    if i == n1:
        while (j < n2):
            A[k] = R[j]
            j += 1
            k += 1
    else:
        while (i < n1):
            A[k] = L[i]
            i += 1
            k += 1

    return A


def merge_sort(A, p, r):
    """Merge sort A[p...r]

    Args:
        A: the array to be sorted
        p: the start index of the array A
        r: the end index of the array A

    Return:
        sorted A[p...r]
    """
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        #merge(A, p, q, r)
        merge_without_sentinel(A, p, q, r)

    return A
        

if __name__ == '__main__':
    A = [3, 5, 3, 89, 543, 1, 6, 8, 11, 39]
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30]
    print('Original array [0, len(A)-1]: {}'.format(A))
    t1 = time.time()
    sorted_A = merge_sort(A, 0, len(A)-1)
    t2 = time.time()
    print(f'Merge sort took {1000*(t2-t1):.3} ms')
    print('Sorted A: {}'.format(sorted_A))
    print(f'The number of inversions in array A: {COUNTER}')
