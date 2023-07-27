#!/usr/bin/python3
""""pascal triangle """
def pascal_triangle(n):
    """"checking if n is zero or negative"""
    if n <= 0:
        return []
    """the top row"""

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
if __name__ == "__main__":
    pascal_tringale()
