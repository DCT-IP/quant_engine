# Session Objective - BUild a production - quality implementation of 
#Gaussian elimination with Partial Pivoting to solve Ax=b
# This will lay the foundations for LU, Decomposition, Matrix Inversion,
# Det, LSS an Lin Regression

from numbers import Real

def _validate_input(
    A: list[list[float]],
    b: list[float]
) -> None:
    """
Validate the coefficient matrix and RHS vector.

Raises:
    ValueError
    TypeError
"""
    if not A:
        raise ValueError("Matrix empty!!!")
    if not b:
        raise ValueError("Vector Empty")
    row_count = len(A)
    column_count = len(A[0])
    
    for row in A:
        if len(row) != column_count:
            raise ValueError("Matrix A must be rectangular.")
        
    if row_count != column_count:
        raise ValueError("Matrix A must be square.")
    
    if len(b) != row_count:
        raise ValueError(
            "The dimensions of matrix A and vector b do not match."
        )
    
    for row in A:
        for value in row:
            if not isinstance(value, Real):
                raise TypeError("Matrix A must contain only numeric values.")
            
    for value in b:
        if not isinstance(value, Real):
            raise TypeError("Vector b must contain only numeric values.")


def _create_augmented_matrix(A, b) -> list[list[float]]:
    augmented_matrix = []
    for i in range(len(A)):
        copy_row = A[i].copy()
        copy_row.append(b[i])
        augmented_matrix.append(copy_row)
    return augmented_matrix

def _partial_pivot(matrix: list[list[float]],pivot_row: int) -> None:
    """
    Perform partial pivoting on the current pivot column.
    Args:
        matrix: Augmented matrix.
        pivot_row: Current pivot row.
    Raises:
        ValueError: If a valid pivot cannot be found.
    """

    max_row = pivot_row
    max_value = abs(matrix[pivot_row][pivot_row])
    for row in range(pivot_row + 1, len(matrix)):
        current_value = abs(matrix[row][pivot_row])

        if current_value > max_value:
            max_value = current_value
            max_row = row

    if max_value == 0:
        raise ValueError("Matrix is singular.")
    
    if max_row != pivot_row:
        matrix[pivot_row], matrix[max_row] = (
            matrix[max_row],
            matrix[pivot_row],
        )

def _forward_elimination(
    matrix: list[list[float]]
) -> list[list[float]]:
    """
    Perform forward elimination to convert augmented matrix into Upper Triangle Form
    Args:
        Augmented Matrix - [A|b]
    Variables:
        n
        pivot_row
        target_row
        column
        pivot
        factor
    """
    n = len(matrix)
    for pivot_row in range(n-1):
        _partial_pivot(matrix, pivot_row)
        pivot = matrix[pivot_row][pivot_row]
        if pivot == 0 :
            raise ValueError("There are trivial solution to this!!!\n")
        for target_row in range(pivot_row+1, n):
            factor = matrix[target_row][pivot_row] / pivot

            for column in range(pivot_row, n + 1):
                matrix[target_row][column] -= (
                    factor * matrix[pivot_row][column]
                )

    return matrix

def _back_substitution(
    matrix: list[list[float]]
) -> list[float]:
    """
    Solve an upper triangular system using back substitution.
    Args:
        matrix: Upper triangular augmented matrix.
    Returns:
        Solution vector.
    """
    n = len(matrix)
    solution = [0.0] * n
    for row in range(n - 1, -1, -1):
        known_sum = 0.0
        for column in range(row + 1, n):
            known_sum += (
                matrix[row][column] * solution[column]
            )
        diagonal = matrix[row][row]

        if diagonal == 0:
            raise ValueError("Matrix is Singular.")
        solution[row] = (
            matrix[row][n] - known_sum
        ) / matrix[row][row]

    return solution

def solve(A : list[list[float]], b:list[float]) -> list[float]:
    _validate_input(A, b)
    aug_matrix = _create_augmented_matrix(A, b)
    _partial_pivot(aug_matrix, 0)
    _forward_elimination(aug_matrix)
    solution = _back_substitution(aug_matrix)
    return solution

