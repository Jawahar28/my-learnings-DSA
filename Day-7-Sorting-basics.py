# Q1. Elements Removal 
# Given N elements, at every step remove an array element
# Cost to remove an element = Sum of array of elements present in an array
# Find minimum cost to remove all elements.

# TC: O(N log N), SC:O(1)
'''def findcost(arr):
    arr.sort()
    cost = 0

    for i in range(len(arr)-1,-1,-1):
        cost += (arr[i] * (len(arr)-i)) # Contribution Technique
    return cost



print(findcost([2,1,4])) # Output : 11
print(findcost([3,5,1,-3])) # Output : 2'''

# Q2. Noble Integers.(Distinct Data)
# Given N array elements, calculate number of noble integers.
# An element ele in arr [] is said to be noble if (count of smaller elements = ele itself)

# TC:O(N log N), SC:O(1)
'''def noble(arr):
    arr.sort()
    noble = 0

    for i in range(len(arr)):
        if arr[i] == i:
            noble+=1
    return noble

print(noble([1,-5,3,5,-10,4])) # Output : 3
print(noble([-3,0,2,5])) # Output : 1'''

# Q3. Noble Integers( Data can Repeat)
# TC: O(NlogN), SC:O(1)
'''def noble(arr):
    arr.sort()

    noble = 0
    count = 0

    if arr[0] == 0:
        count+=1
    
    for i in range(1, len(arr)-1):
        if arr[i] != arr[i-1]:
            count = i
        if count == arr[i]:
            noble+=1
    return noble
    
print(noble([-10,1,1,3,100])) # Output : 3
print(noble([-10,1,1,2,4,4,4,8,10])) # Output : 5
print(noble([-3,0,2,2,5,5,5,5,8,8,10,10,10,14])) # Output: 7'''

