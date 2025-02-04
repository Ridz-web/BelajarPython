matrix = [[1,2,3], [4,5,6], [7,8,9]]
M = len(matrix)
N = len(matrix[0])

for i in range(M):
    for j in range(N):
        print(matrix[i][j], end='')
    print()


matrix = [["X", "O", "O"], ["O", "X", "O"], ["O", "O", "X"]]
def count_x_in_matrix(matrix: list[list[int]]) -> int:
    no_of_rows = len(matrix)
    no_of_cols = len(matrix[0])
    count = 0
    
    for row in range(no_of_rows):
        for cols in range(no_of_cols):
                if matrix[row][cols] == "X":
                    count += 1
    return count
print(f"\nX = {count_x_in_matrix(matrix)}")

matrix =  [('a', 1), ('b', 2), ('a', 3)]
print(matrix[0][1])