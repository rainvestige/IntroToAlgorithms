# coding=utf-8
import random

def linear_search(A, v):
    """Linear search the value v in the array A

    Args:
        A: the array to be searched
        v: the searched value

    Returns:
        the index i such that A[i] = v or "NIL" if not finded
    """
    output = 'NIL'
    for i in range(len(A)):
        if A[i] == v:
            output = i
            break

    return output



if __name__ == '__main__':
    random.seed(1996)
    A = [random.randint(-100, 100) for _ in range(100)]
    print('Original array: {}'.format(A))

    ret = linear_search(A, 70)
    print('Search result index: {}'.format(ret))
        
