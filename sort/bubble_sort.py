# coding=utf-8
import random


def bubble_sort(A):
    """Bubble Sort the array A

    Args:
        A: the array to be sorted

    Returns:
        the sorted array A
    """
    n = len(A)
    for i in range(0, n-1):
        j = n - 1
        while (j > i):
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
            j = j - 1

    return A


if __name__ == '__main__':
    A = [random.randint(-200, 200) for _ in range(100)]
    print('Original array: {}'.format(A))
    print('*'*80)
    bubble_sort(A)
    print('Sorted array: {}'.format(A))
