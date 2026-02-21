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



