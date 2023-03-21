import scipy.sparse as sp


def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    """Multiplicates two sparse matrices together.

    Args:
        matrix_a (list): A sparse matrix.
        matrix_b (list): A sparse matrix.

    Returns:
        list: A sparse matrix.
    """
    # Check if matrices are multipliable
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    else:
        sp_a = sp.csr_matrix(matrix_a)
        sp_b = sp.csr_matrix(matrix_b)
        return sp_a.dot(sp_b).toarray().tolist()


matrix_a = [
    [0, 2, 0],
    [0, -3, 5],
]
matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4],
]

print(f'\n\n{sparse_matrix_multiplication(matrix_a, matrix_b)}\n\n')
