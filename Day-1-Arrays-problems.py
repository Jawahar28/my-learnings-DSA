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