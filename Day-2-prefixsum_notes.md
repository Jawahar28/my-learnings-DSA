# Prefix Sum : It is a type of array where A cummulative sum array.

# How to create a prefix sum array:

    prefix_sum[i] = prefix_sum[i-1] + arr[i] if i > 0
    prefix_sum[0] = arr[0]

# Brute Force Approach :
    # TC : O(N^2) , SC : O(1)
    def prefx_sum(arr):
        ps = [0]*len(arr)

        for i in range(len(arr)):
            sum = 0
            for j in range(len(arr)):
                sum+=arr[j]
            ps[i] = sum
        return ps

# Formulae : 
    a. Sum of array in a range(L,R) : ps[r] - ps[l-1]
    b. ps[i] = sum of the elements from 0th index to ith index.
    c. Special Index :
        even_sum = Sum of even indices[0,i-1] + Sum of odd Indices[i+1,N-1]
        odd_sum = Sum of odd indices[0,i-1] + Sum of even indices[i+1, N-1]

* Whenever we use prefix sum , the SC would be O(N) in almost every cases.

# Leetcode Questions:
    1. Running Sum of 1d Array:
        https://leetcode.com/problems/running-sum-of-1d-array/description/
    
    2. Find Pivot Index :
        https://leetcode.com/problems/find-pivot-index/description/
    
    3. Find the Middle index in Array:
        https://leetcode.com/problems/find-the-middle-index-in-array/description/
    
    4. Binary Sums:
        https://leetcode.com/problems/binary-subarrays-with-sum/description/
    
    5. Number of subarrays with Odd Sum:
        https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/

    6. Subarray Sums Divisble by K:
        https://leetcode.com/problems/subarray-sums-divisible-by-k/

    7. Number of Submatrices That Sum to Target:
        https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/


