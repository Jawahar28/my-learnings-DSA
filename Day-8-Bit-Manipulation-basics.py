# Addition of Two binary numbers
# TC:O(s1+s2), SC:O(1)

'''def binaryaddition(s1, s2):
    ans = ""
    i,j = len(s1)-1, len(s2)-1
    carry = 0

    while i >= 0 and j >= 0: # if len(s1) == len(s2) this will work
        curr_sum = carry + int(s1[i]) + int(s2[j])
        ans += str(curr_sum%2)
        carry = curr_sum//2
        i-=1
        j-=1
    if carry > 0:
        ans+=str(carry)
    return ans[::-1]

print(binaryaddition('110101','100110'))'''

# Doing Bitwise Operations directly
'''print("Bitwise AND of :", 5 & 6)
print("Bitwise OR of :", 20 | 45)
print("Bitwise XOR of :",20 ^ 45)'''

# Representing the Negative number.

def negative(n):
    s = format(n, '08b')
    print(s)
    return

print(negative(5))