# Sliding Window 
# Q1. Find Sum of all subarrays

# Brute Force:
# TC: O(N^3), SC:O(1)
'''def findsum(arr):
    total = 0

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(i, j+1):
                total+=arr[k]
    return total'''

# Another Approach: Using Prefix Sum
# TC:O(N^2), SC:O(N)
'''def findsum(arr):
    total = 0

    ps = [0]*len(arr)
    ps[0] = arr[0]
    for i in range(len(arr)):
        ps[i] = ps[i-1]+arr[i]

    for i in range(len(arr)):
        currsum = 0
        for j in range(i, len(arr)):
            if i==0:
                currsum = ps[j]
            else:
                currsum = ps[j]-ps[i-1]
            total+=currsum 
    
    return total'''

# Optimised Approach: Using Carry Forward Technique
# TC:O(N^2), SC:O(1)
'''def findsum(arr):
    total = 0

    for i in range(len(arr)):
        currsum = 0
        for j in range(i, len(arr)):
            currsum += arr[j]
            total+=currsum 
    return total'''

# Best Optimised Solution: Using Contribution Technique
# TC: O(N), SC:O(1)
'''def findsum(arr):
    total = 0

    for i in range(len(arr)):
        total += arr[i]*(len(arr)-i) * (i+1)
    return total


print(findsum([3,2,5]))
print(findsum([-4,1,3,2]))'''

# Q2. Number of Subarrays of length K.
# Given arr[N], Print Maximum Subarray sum of length K.

# Brute Force:
# TC: O(K(N-k+1)), SC:O(1)
'''def subarraysum(arr,k):
    ans = -float('inf')
    s,e = 0, k-1

    while e < len(arr): # TC:O(N-K+1) , No of starting points
        currsum = 0
        for i in range(s,e+1): #TC:O(K)
            currsum+=arr[i]
        ans = max(ans, currsum)
        s+=1
        e+=1
    return ans
'''

# Another Approach : Using PrefixSum
# TC: O(N), SC: O(N)
'''def subarraysum(arr,k):
    ans = -float("inf")
    
    ps = [0]*len(arr)
    ps[0] = arr[0]

    for i in range(1,len(arr)):
        ps[i] = ps[i-1] + arr[i]
    
    s,e = 0, k-1
    currsum = ps[k-1]
    s+=1
    e+=1
    
    while e < len(arr):
        currsum = currsum - arr[s-1] + arr[e]
        ans = max(ans, currsum)
        s+=1
        e+=1
    return ans'''

# Optimised Solution: Sliding Window
# TC:O(N), SC:O(1)
'''def subarraysum(arr,k):
    ans = -float("inf")
    s,e = 0, k-1

    currsum = 0
    for i in range(s, e+1): # O(K)
        currsum+=arr[i]
    ans = max(ans,currsum)
    s+=1
    e+=1
    while e < len(arr): # O(N-K+1)
        currsum = currsum - arr[s-1]+arr[e]
        ans = max(ans, currsum)
        s+=1
        e+=1
    return ans

print(subarraysum([-3,4,-2,5,3,-2,8,2,-1,4],5))'''