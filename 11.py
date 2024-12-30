matrix = []
upto = 4
largest = 0
with open('./11.txt', 'r') as file:
  for line in file:
    row = line.strip().split()
    matrix.append(list(map(int, row)))
  

# straight
def straight(matrix, largest=largest):
  for row in matrix:
    for i in range(len(row) - upto + 1):
      product = row[i] * row[i+1] * row[i+2] * row[i+3]
      if product > largest:
        largest = product

  return largest


# diagnoal
def diagonal(matrix, largest=largest):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - upto + 1):
        for j in range(cols - upto + 1):
            product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
            if product > largest:
                largest = product

    return largest


def rotate_matrix(matrix):
  new_matrix = [[] for _ in range(len(matrix[0]))]

  for row in matrix:
    for i in range(len(row)):
      new_matrix[i].append(row[i])

  return new_matrix


def reverse_matrix(matrix):
    return [row[::-1] for row in matrix]



# horizontal
largest = straight(matrix)
# vertical
largest = straight(rotate_matrix(matrix))
# right to bottom
largest = diagonal(matrix, largest)
# left to bottom
largest = diagonal(reverse_matrix(matrix))

print(largest)
