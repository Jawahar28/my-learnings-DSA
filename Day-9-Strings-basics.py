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


