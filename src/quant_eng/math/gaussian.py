"""
Gaussian Elimination with Partial Pivoting.

Provides a production-quality implementation for solving
linear systems of the form Ax = b.

Algorithm:
1. Validate input.
2. Construct augmented matrix [A | b].
3. Perform Gaussian Elimination with Partial Pivoting.
4. Solve using Back Substitution.

This module serves as the foundation for:

- LU Decomposition
- Matrix Inversion
- Determinant Computation
- Least Squares
- Linear Regression
"""

from numbers import Real

EPSILON = 1e-12


def _validate_input(
    A: list[list[float]],
    b: list[float],
) -> None:
    """
    Validate coefficient matrix and RHS vector.

    Raises
    ------
    ValueError
        If dimensions are invalid.
    TypeError
        If non-numeric values are supplied.
    """

    if not A:
        raise ValueError("Coefficient matrix cannot be empty.")

    if not b:
        raise ValueError("Right-hand side vector cannot be empty.")

    rows = len(A)
    cols = len(A[0])

    for row in A:
        if len(row) != cols:
            raise ValueError("Matrix A must be rectangular.")

    if rows != cols:
        raise ValueError("Matrix A must be square.")

    if len(b) != rows:
        raise ValueError(
            "Dimensions of A and b do not match."
        )

    for row in A:
        for value in row:
            if not isinstance(value, Real):
                raise TypeError(
                    "Matrix A must contain numeric values."
                )

    for value in b:
        if not isinstance(value, Real):
            raise TypeError(
                "Vector b must contain numeric values."
            )


def _create_augmented_matrix(
    A: list[list[float]],
    b: list[float],
) -> list[list[float]]:
    """
    Construct augmented matrix [A | b].
    """

    augmented = []

    for row, value in zip(A, b):
        augmented.append(row.copy() + [value])

    return augmented


def _partial_pivot(
    matrix: list[list[float]],
    pivot_row: int,
) -> None:
    """
    Perform partial pivoting.

    Swaps the current pivot row with the row
    containing the largest absolute pivot element.
    """

    max_row = pivot_row
    max_value = abs(matrix[pivot_row][pivot_row])

    for row in range(pivot_row + 1, len(matrix)):
        current = abs(matrix[row][pivot_row])

        if current > max_value:
            max_value = current
            max_row = row

    if max_value < EPSILON:
        raise ValueError("Matrix is singular.")

    if max_row != pivot_row:
        matrix[pivot_row], matrix[max_row] = (
            matrix[max_row],
            matrix[pivot_row],
        )


def _forward_elimination(
    matrix: list[list[float]],
) -> None:
    """
    Convert augmented matrix into upper triangular form.
    """

    n = len(matrix)

    for pivot_row in range(n - 1):

        _partial_pivot(matrix, pivot_row)

        pivot = matrix[pivot_row][pivot_row]

        for target_row in range(pivot_row + 1, n):

            factor = (
                matrix[target_row][pivot_row]
                / pivot
            )

            for column in range(pivot_row, n + 1):

                matrix[target_row][column] -= (
                    factor * matrix[pivot_row][column]
                )


def _back_substitution(
    matrix: list[list[float]],
) -> list[float]:
    """
    Solve an upper triangular system.
    """

    n = len(matrix)

    solution = [0.0] * n

    for row in range(n - 1, -1, -1):

        diagonal = matrix[row][row]

        if abs(diagonal) < EPSILON:
            raise ValueError("Matrix is singular.")

        sum_ax = 0.0

        for column in range(row + 1, n):

            sum_ax += (
                matrix[row][column]
                * solution[column]
            )

        solution[row] = (
            matrix[row][n] - sum_ax
        ) / diagonal

    return solution


def solve(
    A: list[list[float]],
    b: list[float],
) -> list[float]:
    """
    Solve Ax = b using Gaussian Elimination
    with Partial Pivoting.

    Parameters
    ----------
    A : list[list[float]]
        Coefficient matrix.

    b : list[float]
        Right-hand side vector.

    Returns
    -------
    list[float]
        Solution vector.

    Raises
    ------
    ValueError
        If the system is singular or dimensions
        are invalid.

    TypeError
        If non-numeric values are supplied.
    """

    _validate_input(A, b)

    augmented = _create_augmented_matrix(A, b)

    _forward_elimination(augmented)

    return _back_substitution(augmented)