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

# Brute Force:
# TC: O(N*Q), SC:O(1)

'''def perform_queries(N, Q):
    arr = [0]*N

    for i in range(len(Q)):
        l = Q[i][0]
        r = Q[i][1]
        x = Q[i][2]

        for j in range(l, r+1):
            arr[j] =arr[j] + x
    return arr
print(perform_queries(7, [(1,5,2)]))''' 

# Difference Array Technique
# TC : O(Q), SC:O(N)
'''def dif_array(N, Q):
    arr = [0]*(N+1)

    for l,r,x in Q:
        arr[l] += x

        if r+1 < N:
            arr[r+1] -= x

    
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]
    return arr

print(dif_array(7, [(1,5,2), (2,4,1)]))'''



# Q3. Rain Water Trapping ****
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Brute Force
# TC :O(N^2), SC: O(1)
'''def rain_water_trapping(arr):
    stored = 0

    for i in range(1,len(arr)-1):
        left_max = max(arr[0:i+1])
        right_max = max(arr[i+1:len(arr)])

        stored += min(left_max, right_max) - arr[i]
    return stored'''

# Better Solution : Trade off Technique
# TC : O(N), SC : O(N)
'''def rain_water_trapping(arr):
    left_max = [0] * len(arr)
    left_max[0] = arr[0]

    right_max = [0] * len(arr)
    right_max[-1] = arr[-1]

    for i in range(1,len(arr)):
        left_max[i] = max(arr[i], left_max[i-1])
    
    for i in range(len(arr)-2, -1, -1):
        right_max[i] = max(arr[i], right_max[i+1])

    # print(f"left_max : {left_max}")
    # print(f"right_max : {right_max}")

    ans = 0

    for i in range(len(arr)):
        ans += min(left_max[i], right_max[i]) - arr[i]

    return ans'''

    

# Optimised Solution : Using Two Pointers
# TC : O(N), SC:O(1)

def rain_water_trapping(arr):
    n = len(arr)
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water


print(rain_water_trapping([10,6,2,7,5,8,12,7]))
print(rain_water_trapping([15,10,6,2,7,5,8,12,7,9,11]))