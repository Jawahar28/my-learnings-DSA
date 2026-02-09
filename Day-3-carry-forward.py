# Carry Forward Technique
# Q1. Count 'a-g' pairs
# Given a string s of lowercase characters, return the count of pairs(i,j) such that i < j and s[i] is 'a' and s[j] is 'g'

# Brute Force :
# TC : O(N^2), SC: O(1)
'''def countag(s):
    pairs = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == 'a' and s[j] == 'g':
                pairs+=1
    return pairs
'''

# Optimised Solution
# TC : O(N), SC: O(1) 
'''def countag(s):
    count_a = 0

    count_g = 0
    for i in s:
        if i == 'a':
            count_a+=1
        if i == 'g':
            count_g+=count_a
    return count_g

print(countag('abegag'))'''