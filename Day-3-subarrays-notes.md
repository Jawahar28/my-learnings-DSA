# Subarrays :
    A subarray is a continguous part and same order/pattern of an array. 
    It is formed by selecting a range of elements from the array.
    A subarray can have one or more elements and must be continguous part of array.

# Example :
    arr = [4,1,2,3,-1,6,9,8,12]
    Subarrays = [9,8,12], [9], [-1,6], [4,1,2,3,-1,6,9,8,12]
    Not Subarrays = [4,-1,6,9],[4,8,12,4]

# Representation of an subarray :

    A subarray can be uniquely represented in following ways:

    a. By specifying the start and end index of the subarray.
        ex: arr = [4,1,2,3,-1,6,9,8,12]
            sub = arr[2:5]
    b. By specifying the start index and length of the subarray.

# Some important formulae:

    a. Number of Subarrays starting from index 'i' = (N-i)
    b. Total Number of subarrays in an array of size "N" = N*(N+1)//2
    c. Number of times the index 'i' element present in subarrays = (N-i)*(i+1)
