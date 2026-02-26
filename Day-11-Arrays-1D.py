# Arrays 1-Dimensional

# Q1. Maximum Subarray Sum
# Given an array, Consider all the subarrays and find the maximum sum of them.

# Brute Force: Traverse with 2 loops.
# TC:O(N^3), SC:O(1)

'''def max_subarray(arr):
    ans = -float('inf')

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            curr_sum = sum(arr[i:j+1])
            if ans < curr_sum:
                ans = curr_sum
                subarray = arr[i:j+1]
    return ans, subarray

print(max_subarray([10,6,9,8,-1000,1,2,3]))'''

# Better Solution : Using Prefix Sum
# TC : O(N^2), SC:O(N)
'''def max_subarray(arr):
    ans = -float('inf')

    ps = [0]*len(arr)
    ps[0] = arr[0]

    for i in range(1,len(arr)):
        ps[i] = ps[i-1] + arr[i]
    
    for i in range(len(ps)):
        curr_sum = 0
        for j in range(i, len(ps)):
            curr_sum = ps[j] - (ps[i] if i > 0 else 0) 
            ans = max(curr_sum, ans)
    return ans

print(max_subarray([10,6,9,8,-1000,1,2,3]))
print(max_subarray([-4,-10,-2,-1,0]))'''



# Better Solution : Using Carry Forward
# TC : O(N^2), SC:O(1)

'''def max_subarray(arr):
    ans = -float('inf')

    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            ans = max(ans, curr_sum)
    return ans
print(max_subarray([10,6,9,8,-1000,1,2,3]))
print(max_subarray([-4,-10,-2,-1,0]))'''

# Optimised Solution : Using Kadane's Algorithm
# TC : O(N), SC:O(1)

'''def max_subarray(arr):
    ans = -float('inf')
    curr_sum  = 0
    for i in range(len(arr)):
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += arr[i]
        ans = max(ans, curr_sum)
    return ans

print(max_subarray([-4,-10,-2,-1,0]))
print(max_subarray([10,6,9,8,-1000,1,2,3]))'''

# Q2. Given an array of size N, in which all elements are 0. Also Given Queries Q, with l and r indices and perform the queries.

# TC: O(N*Q), SC:O(1)

def perform_queries(N, Q):
    arr = [0]*N

    for i in range(len(Q)):
        l = Q[i][0]
        r = Q[i][1]
        x = Q[i][2]

        for j in range(l, r+1):
            arr[j] =arr[j] + x
    return arr
print(perform_queries(7, [(1,5,2)])) 

