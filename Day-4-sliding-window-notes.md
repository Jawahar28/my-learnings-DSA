# Contribution Technique : 
    The Contribution Technique is a very important pattern in DSA, especially in arrays, stacks, and combinatorics.
    Instead of calculating the answer by iterating over all subarrays/subsequences, we calculate how much each element contributes to the final answer.

* Instead of:

    “For each subarray, compute its value”

    We do:

    “For each element, compute how many subarrays it affects, and add its total contribution.”

    This often reduces:

    O(n²) → O(n) or O(n log n)

# Some important Formaule:
    a.Contribution of an element / Index i element present in the subarrays : (N-i) * (i+1)

    b. Total Sum of all subarrays : arr[i] * ((N-i)*(i+1))


# Some Practice Problems:

    1. Sum of all subarrays.
    2. Count subarrays containing element at index i.
    3. Total Contribution of each element.
    4. Sum of Subarray Maximums.
    5. Count subarrays where element is the maximum.
    6. Sum of absolute difference of all pairs

# Leetcode :

    1. Sum of Subarray miimums: 
        https://leetcode.com/problems/sum-of-subarray-minimums/description/
    
    2. Sum of Subarrays in a range: 
        https://leetcode.com/problems/sum-of-subarray-ranges/description/

    3. Total Strength of Wizards:
        https://leetcode.com/problems/sum-of-total-strength-of-wizards/description/


# Number of Subarrays with Length K: N-k+1
    No of starting points of all subarrays of length k = [0, N-k]
    No of starts = [0, N-k]
                 = N-K-0+1
                 = N-k+1