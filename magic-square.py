#!/usr/bin/env python
# -*- coding: utf-8 -*-

# magic-square.py, rcampbel@purdue.edu, 2022-10-27
# See https://en.wikipedia.org/wiki/Magic_square & https://en.wikipedia.org/wiki/Magic_constant

NOT_SQUARE = 'not square'
FAILED_SUMS = 'failed sums'
NOT_UNIQUE = 'not unique'
SUM_IS = ' sum is '
LEN_IS = ' length is '
ROW = ', row #'
COL = ', col #'
MAIN = ', main diag'
ANTI = ', anti diag'
VALID = 'This is a valid magic square: '
NOT_VALID = 'This is NOT a valid magic square '
TEST_SQUARES = [
    [[2, 7, 6],  # Valid
     [9, 5, 1],
     [4, 3, 8]],

    [[2, 7, 6],  # Not unique
     [2, 7, 6],
     [4, 3, 8]],

    [[2, 7, 6],  # Bad sums
     [9, 5, 1],
     [4, 3, 0]],

    [[2, 7, 6],  # Not square
     [9, 5, 1],
     [4, 3, 8, 0]],

    [[1, 14, 4, 15],  # Valid, 4x4
     [8, 11, 5, 10],
     [13, 2, 16, 3],
     [12, 7, 9, 6]]
    ]


def check_magic_square(sq):
    """Return None if given list of lists is a magic square, else problem string."""
    order = len(sq)  # Num rows in square
    magic_constant = order * ((order**2 + 1) / 2)  # Target sum of rows, cols, both diags
    main_sum = anti_sum = 0

    # Unique values? NOTE sum() Inefficiently "flattens" list of lists, set() returns unique values
    # See https://stackoverflow.com/a/952946 & https://stackoverflow.com/a/12897477
    if len(set(sum(sq, []))) != len(sum(sq, [])):
        return NOT_UNIQUE

    # Each row...
    for r in range(order):
        row_sum = col_sum = 0
        main_sum += sq[r][r]
        anti_sum += sq[r][-1 * (r + 1)]  # NOTE Using negative indexing

        # Square? (num rows equals num cols?)
        if len(sq[r]) != order:
            return NOT_SQUARE + ROW + str(r+1) + LEN_IS + str(len(sq[r]))

        # Each col in current row...
        for c in range(order):
            row_sum += sq[r][c]
            col_sum += sq[c][r]  # NOTE Switching row & col index

        # Correct row/col sums?

        if row_sum != magic_constant:
            return FAILED_SUMS + ROW + str(r+1) + SUM_IS + str(row_sum)

        if col_sum != magic_constant:
            return FAILED_SUMS + COL + str(r+1) + SUM_IS + str(col_sum)

    # Correct diagonal sums?

    if main_sum != magic_constant:
        return FAILED_SUMS + MAIN + SUM_IS + str(main_sum)

    if anti_sum != magic_constant:
        return FAILED_SUMS + ANTI + SUM_IS + str(anti_sum)

    return None


if __name__ == "__main__":

    for square in TEST_SQUARES:
        problem = check_magic_square(square)

        if problem is None:
            print(VALID)
        else:
            print(NOT_VALID + '('+problem+'): ')

        for row in square:
            print('   ', row)
