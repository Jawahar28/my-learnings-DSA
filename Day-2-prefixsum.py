# Prefix Sum:

# Q1. Given an araay of N integers and Q queries. For each query calculate the sum of elements in the range -  [L,R]
# TC : O(NQ)
# Sc : O(1)
def prefix_sum(arr,q):
    ans = []
    ps = [0]*len(arr)
    ps[0] = arr[0]

    for i in range(1,len(arr)-1):
        ps[i] = ps[i-1]+arr[i]
    print(ps)
    for l,r in q:
        ans.append(ps[r]-ps[l-1])

    return ans

print(prefix_sum([-3,6,2,4,5,2,8,-9,3,1],[[4,8],[3,7],[1,3],[0,4],[7,7]]))
