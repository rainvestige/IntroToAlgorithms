# coding=utf-8


def evaluating_polynomial(A, x):
    """Compute the naive polynomial

    Args:
        A: the polynomial coefficient array A[0, ..., n]
        x: the variable

    Returns:
        the result (y = \sum_{k=0}^n A[k]x^k)
    """

    # the real length of coefficient array is (n+1)
    n = len(A) - 1
    y = 0
    for k in range(0, n+1):
        temp = 1
        j = k
        while(j > 0):
            # temp = x^k
            temp = x * temp
            j -= 1
        y += A[k] * temp

    return y


def horner_rule(A, x):
    """Evaluate the polynomial using Horner's rule

    Args:
        A: the polynomial coefficient array A[0, ..., n]
        x: the variable

    Returns:
        the result (y = \sum_{k=0}^n A[k]x^k)
    """
    n = len(A) - 1
    y = 0
    i = n
    while i >= 0:
        y = A[i] + x * y
        i -= 1

    return y

if __name__ == '__main__':
    A = [1, 2, 1]
    x = 8
    y = evaluating_polynomial(A, x)
    y_horner_rule = horner_rule(A, x)
    assert y == y_horner_rule
    print('The coefficient array A = {0}\nx = {1}'.format(A, x))
    print('\nThe result y = {}'.format(y))

