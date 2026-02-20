# SORTING : RE-ARRANGING OF DATA IN PARTICULAR ORDER ON THE BASIS OF SOME PARAMETER.

* Sorting is essential for oraganizing, analyzing, searching and presenting data efficiently in various applications and contexts.

* Sorting Libraries :
    arr.sort() // Increasing Order
    arr.sort(reverse = False) // Decreasing

# Types of Sorting Algorithms:

* 1. Selection Sort : selecting the max or min element and sorting the array on the some basis.
    * Code : # TC: O(N^2), SC:O(1)
            def selection_sort(arr):
                for i in range(len(arr)-1):
                    min_idx = i
                    for j in range(i+1, len(arr)):
                        if arr[j] < arr[min_idx]:
                            min_idx = j
                    arr[i], arr[min_idx] = arr[min_idx],arr[i]
                
* 2. Insertion Sort : Arrangement of Playing Cards.
    * Code : #TC:O(N^2) ,SC:O(1)
             def insertion_sort(arr):
                for i in range(1, len(arr)):
                    curr_ele = arr[i]
                    j = i-1
                    while j >= 0 and arr[j] > curr_ele:
                        arr[j+1] = arr[j]
                        j-=1
                    arr[j+1] = curr_ele

* 3. Quick Sort :
* 4. Merge Sort :
* 5. 
