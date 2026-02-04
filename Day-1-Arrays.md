# Introduction to Problem Solving

* Number vs Iterations vs Execution Time :

    10^8 - 10**8 - 1 sec
    10^9 - 10**8 * 10 -> 10 sec
    10^18 -> 10^8 * 10^10 -> 317 years

As the execution time increases -> Efficiency of the code is decreased.

* Iteration means Number of times the loop runs

---------------------------------------------------------------------------------------------------------------------------------------------------

# Range
[a,b] -> a to b (Both Inclusive or Both Included)
[a,b) -> a to b-1 ( 'a' is Inclusive and 'b' is Exclusive)
(a,b] -> a+1 to b ('a' is Exclusive and 'b' is Inclusive)
(a,b) -> a+1 to b-1 (Both are Exclusive or Both are Excluded)

* Number of Elements in a range : (b-a+1)

* Sum of N natural numbers : N*(N+1)//2


---------------------------------------------------------------------------------------------------------------------------------------------------

# How to compare two algorithms : Compare using "Number of Iterations".

* We cannot decide the "Algorithms perfomance" , using "Execution Time" as it depends on a lot factors like Operating Systems, Place of Execution, Language and many more.


---------------------------------------------------------------------------------------------------------------------------------------------------

# Analysis of Algorithms 

1.Log Basics + Iteration Problems

-> Logarithm: It is inverse of exponential function.
              log a base b : To what value we need to raise b, such that to get a.
 
* Number of steps required to reduce N to 1 : By repeatedly dividing with 2

---------------------------------------------------------------------------------------------------------------------------------------------------


2. Asymptotic Analysis of Algorithms

It is used to estimate the performance of Algorithms when the input is large.

* Big - O represents the Upper Boundary of Order of Growth


* Rules for calculating the Big-O Notation :
a. Calculate the number of Iterations
b. Ignore the Lower Order Terms
c. Ignore thr Constant Coefficients.

* Comparision Order :
1 < log log N < log N < sqrt(N) < N < N log N < N sqrt(N) < N**2 < N**3 < 2**N < N! < N**N

* As the input size increases, the contribution of lower order terms decreases , same goes with constants.

---------------------------------------------------------------------------------------------------------------------------------------------------

3. Issues with Big-O

a. We cannot say that one Algorithm will always be better than the other Algorithms.

b. If two Algorithms has same Higher Order , then Big-O is not capable of identifying the Algorithm with higher . lower order of iterations.

---------------------------------------------------------------------------------------------------------------------------------------------------

4. Time Limit Exceeded (TLE) :

a. Processing speed of the server is 1Ghz i.e., 10**9 iterations in 1 sec.
b. Code must be executed in 1sec.

* If no.of iterations > 10**9, then we get TLE.

* If for every iteration, we have 10 instructions, then we can have atmost 10**8 iterations.

* We can have 10**7 to 10**8 iterations only, else we will get TLE.

* We can also find the Time Complexity, by comparing the last term to the N.

---------------------------------------------------------------------------------------------------------------------------------------------------

5. Omega Notation : It is used to find the lower bound ,
                    f(n) = omega(g(n)) if there exists positive constraints C and N0.
                    where 0 <= g(n) <= f(n) for all n >= n0.

* It is useful when we have lower bound on time complexity.

---------------------------------------------------------------------------------------------------------------------------------------------------


6. Theta Notation : It is used to find the exact bound ,
                    f(n) = Theta(g(n)) if there exists constants C1, C2 and N0
                    such that c1(g(n)) <= f(n) <= c2(g(n)) for all n >= n0.


---------------------------------------------------------------------------------------------------------------------------------------------------

7. Analysis of Recursion:

a. We write non-recursive part as root of the tree and recursive parts as children.
b. We keep expanding children until we see a pattern.

* The height of the Recursion Tree is the Time Complexity by adding sum of series at every level.

---------------------------------------------------------------------------------------------------------------------------------------------------

8. Space Complexity : Space taken by the function depends upon how big is the input or extra space required by the function.

        (OR)
    Space Complexity is the max space(worst case) that is utilised at any point in time during running the algorithm.

* It is also called as Auxillary Space.

---------------------------------------------------------------------------------------------------------------------------------------------------

9. Importance of Constraints :

    It is used to check whether the code is working properly or not for the given input range.

---------------------------------------------------------------------------------------------------------------------------------------------------

10. Steps to approach a problem:

    a. Read the Question and Constraints Carefully.
    b. Formulate an Idea or Logic.
    c. Verify the correctness of the Logic.
    d. Mentally Develop a PseudoCode or rough idea of Loops.
    e. Determine the Time Complexity based on the PseudoCode.
    f. Assess if the TC is feasible and won't result in the TLE errors.
    g. In Worst Case we can only have 10^7 or 10^8 iterations.
    h. Re-evaluate the Idea/Logic if the time constarints are not otherwise proceed.
    i. Code the idea if it is deemed feasible.


---------------------------------------------------------------------------------------------------------------------------------------------------

11. Some Important Points:

    a. Time Complexity to access the ith element in an array is O(1).
    b. We can access the index array using "Memory Address(Reference)" in the array ,if it is Contingous Manner.

    c. Dynamic Arrays:  Size is not fixed.

---------------------------------------------------------------------------------------------------------------------------------------------------

# Problems to practice (Leetcode):

# 1. https://leetcode.com/problems/count-primes/description/?envType=problem-list-v2&envId=array& ( Count Primes)
# 2. https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array (Two Sum)
# 3. https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=array (Remove Duplicates from Sorted Array)
# 4. https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array (Remove Element)






                



