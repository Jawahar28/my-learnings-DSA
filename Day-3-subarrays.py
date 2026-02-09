# Subarrays :
# Q1. Given an array, si and ei. Print from si to ei.
# TC: O(N), Sc: O(1)

'''def subarray(arr,si,ei):
    return arr[si:ei+1]

print(subarray([4,2,10,3,12,2,15],2,5))
'''

# Q2. Print all possible subarrays.

# Brute Force :
# TC: O(N^3), SC:O(1)
'''def printsubarrays(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j+1):
                print(arr[k], end=' ')
            print()
    return

print(printsubarrays([5,3,7,2]))'''

# Optimised Solution:
# TC:O(N^3), SC: O(1)
'''def printsubarrays(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i:j+1]) # Here to print subarray it will take O(N) in Worst Case
        print()
    return

print(printsubarrays([4,2,10,3,12,-2,15]))'''

# Q3. Closest Min-Max 
# Given an array of N integers, return the length of smallest subarray which contains both maximum and minimum elements of the array.
# TC:O(N^2), SC:O(1)
'''def closestminmax(arr):
    max_val = max(arr)
    min_val = min(arr)

    ans = float('inf')

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (arr[i] == min_val and arr[j] == max_val)or (arr[i] == max_val and arr[j] == min_val):
                temp = j-i+1
                ans = min(ans,temp)
    return ans'''


# Optimised Solution:
# TC:O(N), SC:O(1)
def closestminmax(arr):
    max_val = max(arr)
    min_val = min(arr)

    last_max_idx, last_min_idx = -1,-1

    ans = float("inf")

    for i in range(len(arr)):
        if arr[i] == min_val:
            last_min_idx = i

            if last_max_idx != -1:
                size = i-last_max_idx+1
                ans = min(ans, size)

        if arr[i] == max_val:
            last_max_idx = i

            if last_min_idx != -1:
                size = i-last_min_idx+1
                ans = min(ans, size)
    return ans


print(closestminmax([2,2,6,4,5,1,5,6,4,1]))
print(closestminmax([1,2,3,1,3,4,6,4,6,3]))
print(closestminmax([8,8,8,8,8,8]))