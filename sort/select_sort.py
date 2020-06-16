# coding=utf-8


def select_sort(lst):
    """Select Sort

    Use select sort to sort the list in place.

    Args:
        lst: the list to be sorted.

    Returns:
        the sorted list.
    """
    length = len(lst)
    idx = 0

    for i in range(0, length-1):
        smallest = lst[i]
        idx = i
        for j in range(i+1, length):
            # find the smallest item
            if lst[j] < smallest:
                smallest = lst[j]
                idx = j
        # exchange
        lst[idx] = lst[i]
        lst[i] = smallest
    return lst


