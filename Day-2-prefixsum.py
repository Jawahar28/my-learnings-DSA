# Prefix Sum:

# Q1. Given an araay of N integers and Q queries. For each query calculate the sum of elements in the range -  [L,R]
# TC : O(N+Q)
# Sc : O(N)
'''def query_sum(arr,q):
    ans = []
    ps = [0]*len(arr)
    ps[0] = arr[0]

    for i in range(1,len(arr)-1):
        ps[i] = ps[i-1]+arr[i]
    print(ps)
    for l,r in q:
        ans.append(ps[r]-ps[l-1])

    return ans

print(query_sum([-3,6,2,4,5,2,8,-9,3,1],[[4,8],[3,7],[1,3],[0,4],[7,7]]))'''


# Q2. Sum of Even indexed Elements :
#     Given an arr[N] and Q queries with start(s) and end(e) index. For every query print sum of all even indexed elements from s to e.
# TC : O(N+Q), SC: O(N)
'''def even_indexed_sum(arr, Q):
    ans = []
    ps = [0]*len(arr)
    ps[0] = arr[0]

    for i in range(1,len(arr)):
        ps[i] = ps[i-1] + (arr[i] if i%2==0 else 0)
    print(ps)
    
    for s,e in Q:
        if s != 0:
            ans.append(ps[e]-ps[s-1])
        else:
            ans.append(ps[e])
    return ans

print(even_indexed_sum([2,3,1,6,4,5],[[1,3],[2,5],[0,4],[3,3]]))'''


# Q3.Sum of Odd indexed Elements :
#     Given an arr[N] and Q queries with start(s) and end(e) index. For every query print sum of all odd indexed elements from s to e.
# TC : O(N+Q), SC: O(N)
'''def odd_indexed_sum(arr, Q):
    ans = []
    ps = [0]*len(arr)

    for i in range(1,len(arr)):
        ps[i] = ps[i-1] + (arr[i] if i%2!=0 else 0)
    print(ps)
    
    for s,e in Q:
        if s != 0:
            ans.append(ps[e]-ps[s-1])
        else:
            ans.append(ps[e])
    return ans

print(odd_indexed_sum([2,3,1,6,4,5],[[1,3],[2,5],[0,4],[3,3]]))'''


# Q4. Special Index : Given an arr[N], count the number of special indices in the array.
#     Special Index means : Index after removing which sum of even indexed elements =  sum of odd indexed elements.
# TC: O(N), SC: O(N)
def special_index(arr):
    pse = [0]*len(arr)
    pse[0] = arr[0]

    for i in range(1, len(arr)):
        pse[i] = pse[i-1] + (arr[i] if i%2==0 else 0)
    print(pse)

    pso = [0]*len(arr)
    for i in range(1, len(arr)):
        pso[i] = pso[i-1] + (arr[i] if i%2!=0 else 0)
    print(pso)
    
    special_idx = []
    for i in range(len(arr)):
        if i != 0:
            even_sum = pse[i-1] + pso[-1] - pso[i] 
            odd_sum = pso[i-1] + pse[-1] - pse[i]
        else:
            even_sum = pso[-1] - pso[i]
            odd_sum = pse[-1] - pse[i]

        if even_sum == odd_sum:
            special_idx.append(i)
    return special_idx, len(special_idx)


      

#print(special_index([4,3,2,7,6,-2]))
# print(special_index([2,3,1,4,0,-1,2,-2,10,8]))
print(special_index([1,1,1]))
