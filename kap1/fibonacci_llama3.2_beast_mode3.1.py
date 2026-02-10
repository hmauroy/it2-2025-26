def multiply_matrices(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(multiply_matrices(half_pow, half_pow), matrix)

def fibonacci(n):
    """
    Calculates the nth Fibonacci number using matrix exponentiation.

    Args:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n-1)
    return result_matrix[0][0]

print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765
print(fibonacci(30))  # Output: 832040
print(fibonacci(100))  # Output: 354224848179261915075