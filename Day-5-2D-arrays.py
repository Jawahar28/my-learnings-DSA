# 2D - Arrays

#Q1. Given arr[N][M], print row-wise sum.
# TC: O(N*M), SC:O(1)

'''def rowsum(arr):
    n = len(arr)
    m = len(arr[0])
    for row in range(n):
        row_sum = 0
        for col in range(m):
            row_sum+=arr[row][col]
        print(f"row {row} : {row_sum}")
    return

print(rowsum([[10,2,7,3],[9,5,-1,6],[3,11,15,20]]))'''

#Q2. Given arr[N][M], print column-wise sum.
# TC:O(N*M), SC:O(1)
'''def columnsum(arr):
    n = len(arr)
    m = len(arr[0])

    for col in range(m):
        column_sum = 0
        for row in range(n):
            column_sum+=arr[row][col]
        print(f"column {col} : {column_sum}")
    return

print(columnsum([[10,2,7,3],[9,5,-1,6],[3,11,15,20]]))'''

#Q3. Given arr[N][N], print Diagonals
# TC:O(N), SC:O(1)
'''def printdiag(arr):
    n = len(arr)
    m = len(arr[0])
    print("Diagonal:")
    for row in range(len(arr)):
        print(arr[row][row], sep=" ")
    
    row, col = 0, m-1
    print("Anti-Diagonal:")
    while col >= 0:
        print(arr[row][col], sep=" ")
        row+=1
        col-=1
    
    return

print(printdiag([[1,5,8,7],[2,11,3,9],[15,20,-3,18],[30,40,50,60]]))'''

# Q4. Given arr[N][M]Print all Anti-Diagonals from right to left.
# TC:O(N*M), SC:O(1)
'''def antidiagonals(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(m-1,-1,-1):
        row,col = 0, i
        while col >= 0 and row < n:
            print(arr[row][col], end=" ")
            row+=1
            col-=1
        print()

    for j in range(1, n):
        row,col = j, m-1
        while row < n and col >= 0:
            print(arr[row][col], end=" ")
            row+=1
            col-=1
        print()
    return

print(antidiagonals([[1,5,8,7,2],[2,11,3,9,1],[15,20,-3,28,18],[30,40,50,45,60]]))'''

#Q5. Transpose of a square matrix.
# TC:O(N*M), SC:O(1)
'''def transpose(arr):
    n = len(arr)
    m = len(arr[0])
    
    for row in range(n-1):
        for col in range(row+1, m):
            arr[row][col], arr[col][row] = arr[col][row],arr[row][col]
    return arr

print(transpose([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))'''

#Q6. Rotate a matrix arr[N][N] by 90 deg clockwise.

def rotate(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    # Transpose the matrix.
    for row in range(row_len):
        for col in range(row+1, col_len):
            arr[row][col], arr[col][row] = arr[col][row], arr[row][col]
    
    # Reverse each row.
    for i in range(row_len):
        arr[i] = arr[i][::-1]
    return arr

print(rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))