def operation(col, row):
    new_matrix = []
    for item in range(col):
        matrix = [(i * item + i) for i in range(1, row + 1)]
        new_matrix.append(matrix)
        print(matrix)


def print_operation_table(operate, rowes, columnes):
    return operate(rowes, columnes)


column = 6
rows = 6

print_operation_table(operation, column, rows)
