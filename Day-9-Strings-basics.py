# Strings :

#Q1: Toggle Case :Given a string consisting of lower-case and upper-case alphabets.
#    Convert lower to upper and vice versa.

# Using In-built Functions
# TC : O(s), SC:O(1)
'''def togglecase(s):
    ans = ""
    for i in s:
        if i.islower():
            ans += i.upper()
        if i.isupper():
            ans += i.lower()
    return ans'''


# Using ASCII values
# TC :O(s^2)
'''def togglecase(s):
    result = ""
    
    for ch in s:
        ascii_val = ord(ch)
        
        # If lowercase (a-z)
        if 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        
        # If uppercase (A-Z)
        elif 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)
        
        # If not alphabet
        else:
            result += ch
    
    return result'''

# Using swapcase()
# TC : O(s)

'''def togglecase(s):
    return s.swapcase()


print(togglecase("Jello"))'''


# Q2. Check Palindrome or not.
# Given a string , start index and end index. Check for substring if its a palindrome or not.

# TC : O(N), SC:O(1)
'''def palindrome(s,si,ei):
    while si <= ei:
        if s[si] != s[ei]:
            return "Not a palindromic Substring"
        si+=1
        ei-=1
    return "Palindromic Substring"

print(palindrome('abmadamtam',2,6))
print(palindrome('xjsnnf',1,4))'''


# Q3 : Given a string s. Find the length of longest palindromic substring in s.

# Brute Force :
# TC : O(N^3), SC: O(1)
'''def palindrome(s,si,ei):
    while si <= ei:
        if s[si] != s[ei]:
            return False
        si+=1
        ei-=1
    return True

def longestpalindrome(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if palindrome(s,i,j):
                ans = max(ans, (j-i+1))
    return ans'''

# Optimised Solution
# TC: O(N^2), SC:O(1)
def longestpalindrome(s):
    ans = 0


    for i in range(len(s)):
        # Odd Length Palindrome
        left, right = i,i

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            ans = max(ans, (right-left+1))
            left-=1
            right+=1
        
        # Even Length Palindrome
    
        left, right = i,i+1

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            ans = max(ans, (right-left+1))
            left-=1
            right+=1
    
    return ans    

print(longestpalindrome('anmadamm'))
print(longestpalindrome('feacabacabgf'))
print(longestpalindrome('adaebcdfdcbetggte'))


