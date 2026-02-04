# 1. Reverse the given array.
'''Approach 1: Slicing.
#TC : O(N), SC: O(!)
arr = [3,7,5,9,2,8]
print("Reversed Array:", arr[::-1])'''

'''# Approach 2: Using Loop.
#TC: O(N), SC: O(1)
arr = [3,7,5,9,2,8]
for i in range(len(arr)-1,-1,-1):
    print(arr[i], end=" ")'''

'''# Approach 3: Using Two pointers.
# TC: O(log N), SC: O(1)
arr = [3,7,5,9,2,8]
i,j = 0, len(arr)-1
while i<j:
    arr[i],arr[j] = arr[j],arr[i]
    i+=1
    j-=1
print(arr)'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Rotate Array K times
'''
# Approach 1: Using Slicing 
#TC : O(KN), SC: O(1)
arr = [3,7,5,9,2,8]
k = 4
k = k%len(arr)
print(arr[k:]+arr[:k]) # Rotate Left
print(arr[-k:]+arr[:-k]) # Rotate Right'''

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Revision :


# Q1: Reverse the array in 3 methods.

# Using Two pointers:
'''def reverse_arr(arr):
    i,j = 0, len(arr)-1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr'''

# Using slicing:
'''def reverse_arr(arr):
    return arr[::-1]'''

# Using loop:
'''def reverse_arr(arr):
    ans = []
    for i in range(len(arr)-1,-1,-1):
        ans.append(arr[i])
    return ans


print(reverse_arr([3,4,5,6,2]))'''


# Q2: Rotate array k times(left):
# Using Slicing
'''def rotate_arr(arr,k):
    k%=len(arr)
    return f"left rotated arr : {arr[k:]+arr[:k]}"

def rotate_arr(arr,k):
    k%=len(arr)
    return f"right rotated arr : {arr[-k:]+arr[:-k]}"'''


# Using functions:
'''def rotate_arr(arr,k):
    k%=len(arr)

    print("Rotate Right :")
    reverse_arr(arr,0,len(arr)-1)
    reverse_arr(arr,0,k-1)
    reverse_arr(arr,k,len(arr)-1)
    return arr

    print("Rotate Left :")
    reverse_arr(arr,0,k-1)
    reverse_arr(arr,k,len(arr)-1)
    reverse_arr(arr,0, len(arr)-1)
    return arr

def reverse_arr(arr,i,j):
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr


print(rotate_arr([2,4,2,1,5],2))'''


