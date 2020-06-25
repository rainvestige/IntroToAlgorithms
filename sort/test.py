from select_sort import select_sort
from insert_sort import insert_sort


if __name__ == '__main__':
    A = [31, 41, 59, 26, 41, 58]
    B = [1, 2, 3, 4, 5]
    print('B = {}'.format(B))
    sorted_B = select_sort(B)
    print('Sorted B by increasing order = {}'.format(sorted_B))
    #insert_sort(A, False)
    #print('Sorted A by decreasing order= {}'.format(A))
