def spiral_traversal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    direction = 0
    output = []

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4

    return output


input_data = [[1, 6, 8, 6], [8, 17, 21, 14], [31, 18, 17, 11], [6, 5, 0, 9]]
output = spiral_traversal(input_data)

print(output)
