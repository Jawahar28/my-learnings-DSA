# Interview Problems

# Q1: Max Consecutive is :  Atmost 1's replace.
# Given an binary array [], We can almost replace a single 0 with 1. Find the maximum consecutive 1's we can get in the array[] after the replacement.

# Brute Force
# TC : O(N^2), SC:O(1) 
'''def max_ones(arr):

    if sum(arr) == 0:
        return 1
    max_ones_len = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            left, right = i-1,i+1
            count_left, count_right= 0,0

            while left >= 0 and right <= len(arr)-1:
                if arr[left] == 1:
                    count_left+=1
                if arr[right] == 1:
                    count_right+=1

                    max_ones_len = max(max_ones_len, count_right+count_left+1)

                left-=1
                right+=1
    if max_ones_len == 0:
        return len(arr)
    return max_ones_len'''

# Optimised Solution
# TC: O(N), SC:O(1)

'''def max_ones(arr):
    ones_count = 0
    for i in arr: #O(N)
        if i == 1:
            ones_count+=1
    
    if ones_count == len(arr):
        return len(arr)
    
    max_ones_len = 0

    for i in range(len(arr)): # O(N)
        if arr[i] == 0:
            left_count, right_count = 0,0

            # Every 1 will be accessed 3 times, counting left, counting right and for loop.

            #Right Side ones count
            j = i+1
            while j < len(arr) and arr[j] == 1: #O(3)
                right_count+=1
                j+=1

            # Left Side ones count
            j=i-1
            while j >= 0 and arr[j] == 1: # O(3) : 
                left_count+=1
                j-=1
            
            max_ones_len = max(max_ones_len, right_count+left_count+1)
    return max_ones_len
        

print(max_ones([0,0,0,0]))
print(max_ones([1,1,1,1,1]))
print(max_ones([1,1,0,1,1,0,1,1]))
print(max_ones([0,1,1,1,0,1,1,0,1,1,0]))'''

# Q2: Max Consective 1's : after swaping.
# Given a binary array[]. We can swap a single 0 with 1. Find the maximum consecutibe 1's we can get in the array[] after atmost 1 swap.
# TC : O(N), SC: O(1)
'''def consecutive_ones(arr):
    ones_count = 0
    for i in arr: #O(N)
        if i == 1:
            ones_count+=1
    
    if ones_count == len(arr):
        return len(arr)
    
    max_ones_len = 0

    for i in range(len(arr)): # O(N)
        if arr[i] == 0:
            left_count, right_count = 0,0

            # Every 1 will be accessed 3 times, counting left, counting right and for loop.

            #Right Side ones count
            j = i+1
            while j < len(arr) and arr[j] == 1: #O(3)
                right_count+=1
                j+=1

            # Left Side ones count
            j=i-1
            while j >= 0 and arr[j] == 1: # O(3) : 
                left_count+=1
                j-=1
            
            if left_count + right_count == ones_count:
                max_ones_len = max(max_ones_len, right_count+left_count)
            else:
                max_ones_len = max(max_ones_len, right_count+left_count+1)
    return max_ones_len


print(consecutive_ones([1,0,1,1,0,1]))
print(consecutive_ones([1,1,0,1,1,1]))
print(consecutive_ones([1,1,0,1,1,1,0,1]))'''

# Q3. Majority Element:
# Given an array of N integers, Find the mojority element(Element which occurs more than N/2)
# Brute Force
# TC :O(N^2), SC:O(1)
'''def majority_ele(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count+=1
            
            if count > len(arr)//2:
                return arr[i]
    return "No Majority Element"'''

# Optimised Solution
# TC : O(N), SC:O(N)
'''def majority_ele(arr):
    freq = {}

    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i]+=1
    
    for key in freq:
        if freq[key] > len(arr)//2:
            return key
    return "No Majority Element"'''

# Optimised Solution : (Boyer - Moore's Voting Algorithm)
# TC :O(N), SC:O(1)
'''def majority_ele(arr):
    candidate = None
    count = 0

    for i in arr:
        if count == 0:
            candidate = i

        if candidate == i:
            count+=1
        else:
            count-=1

    if arr.count(candidate) > len(arr)//2:
        return candidate
    return "No Majority Element"   
 
print(majority_ele([3,4,3,3,6,1,3,2,5,3,3]))
print(majority_ele([2,1,4]))
print(majority_ele([5,5,5,5]))


# Practice Leetcode 229'''


# Q3: Row Column to Zero
# Given array [N][M], Make all elements in a row and column zero if any arr[i][j] == 0.
# TC : O(N*M), SC:O(1)
def rowcolzero(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    for row in range(row_len):
        is_zero = False
        for col in range(col_len):
            if arr[row][col] == 0:
                is_zero = True
                break
        if is_zero ==  True:
            for col in range(col_len):
                if arr[row][col] != 0:
                    arr[row][col] = -1
    
    for col in range(col_len):
        is_zero = False
        for row in range(row_len):
            if arr[row][col] == 0:
                is_zero = True
                break
        if is_zero == True:
            for row in range(row_len):
                if arr[row][col] != 0:
                    arr[row][col] = -1
    

    for row in range(row_len):
        for col in range(col_len):
            if arr[row][col] == -1:
                arr[row][col] = 0
    return arr


print(rowcolzero([[1,2,3,4],[5,6,7,0],[9,2,0,4]]))



