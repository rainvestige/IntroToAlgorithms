# coding=utf-8

def insert_sort(lst):
    """Insert Sort

    Use insert sort to sort the list in place.

    Args:
        lst: the list to be sorted.

    Returns:
        the sorted list.    
    """
    length = len(lst)
    # the index `j` begin at 1 (not 0).
    for j in range(1, length):
        key = lst[j]
        # Insert lst[j] into the sorted sequence lst[1...j-1].
        # `i`: sorted sequence index (from right to left).
        i = j - 1
        while (i >= 0) & (lst[i] > key):
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1] = key

    return lst


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3, 12, 487, 8, -1]
    print('A = {}'.format(A))
    sorted_A = insert_sort(A)
    print('Sorted A = {}'.format(sorted_A))

