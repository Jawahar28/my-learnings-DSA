# 2D-Matrices

# Matrix : Matrix is a 2D Array that has a grid of numbers, where each number is called as an element.

* Representation of a matrix : mat = [[0]*M for _ in range(N)] where M is the number of columns and N is the number of rows.

* Number of Elements in arr[N][M] matrix are N*M.

* When both number of rows and number of columns are equal, then we call it is as "Square Matrix"

* Given a matrix of arr[N][M], then the number of right to left diagonals are N-M+1.
    No of Diagonals = 
            no of diag starting from 0th col to M-1 col +
            no of diag starting from 1st row to N-1 row
        = M + N - 1.

# Problems on Basic 2D matrices :
    1. Print the matrix row-wise
    2. Print the matrix column-wise
    3. Find the sum of all elements in the matrix
    4. Find the maximum element in the matrix
    5. Count how many even numbers are present
    6. Find the sum of each row
    7. Find the sum of each column
    8. Count how many times a given number appears
    9. Check if a matrix is a square matrix
    10. Find the transpose of a matrix
