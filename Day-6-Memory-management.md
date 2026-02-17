# MEMORY MANAGEMENT :

# INTRO TO STACK : Stack is like a container which stores and removes elements using push(add) and pop(remove) methods.

* Principle of Stack : Last In First Out(LIFO)

* a. Insert and delete from top only.
  b. Only access to top element.

# Intro to Call Stack :

* Eg:   def add(x,y):
            return x+y
        
        def prod(x,y):
            return x*y
        
        def sub(x,y):
            return x-y
        
        def main():
            x,y = 10,20
            temp1 = add(x,y)
            temp2 = prod(x,y)
            temp3 = sub(x,y)
            print(temp1+temp2+temp3)
        
        if __name__ == "__main__":
            main()

    * Here "NAME" fucntion will get executed first, so that a separate associated block will be assigned.

    * How blocks are created in Call Stack :
        1. For name function, it will first create a block.
        2. All the elements will be represented in a single block.
        3. If there are any function calls , then new memory blocks are created.
        4. After executing all the functions calls, the call stack will get erased.
        5. If there are no "return statements/ all the statements are executed" then the block will remain the call stack only.
        6. If the memory is removed , we can't reuse the space. 

* Eg:   def add(x,y):
            return x+y
        
        def fun(a,b):
            sum = add(a,b)
            ans = sum * 10
            return ans
        
        def extra(w):
            print("Hello)
            print(w)
        
        def main():
            x,y = 10,20
            z = fun(x,y)
            print(z)
            extra(z)
        
        if __name__ == "__main__":
            main()
        
    * Here first main function will be called and assign a block for it.

        1. In this block, the elements x,y and z(function) will be present.

        2. Since fun() is called, a new block will be created for it and assign the variables with values.
            a. In this function, there is "add function call" is present , so a "new block" will be created for add function with variables x and y.

            b.It will execute the operation and return the result.

            c. As soon as, all the executions are perfomed, this block will get removed/ erased.
            
            c. This result will be stored in the "sum" variable.

            d. Now there is another variable "ans" with some operation and it will get performed.

            e. After, it returns a result and check if there any methods/executions are left to perform. If not, then it will return result in the main block and this memory block will get erased.
        
        3. After returning the resukt, it prints the result and check if there any function calls or methods are left.

        4. There is one more function call present called extra().

        5. So again it will a create memory block for extra() and perform it methods. 

        6. In extra():
            a. It prints Hello and w(value of z).
            b. The memory block gets erased.
        
        7. At last, the main() memory block will be removed.

# REFERENCE VARIABLE : The address of a variable, which tells us where the element is stored.


# TYPES OF MEMEORY:

* 1. Stack : All the primitive data type and reference variables stored.
* 2. Heap : The data pointed by that reference variable is stored in Heap like Arrays, ArrayLists etc., are created inside a Heap.
            * Heap stored complex data.


* Eg : Shallow copy and Deep copy :

        def main():
            x = 10
            arr = [0]*3 // Creating a list of size.
            ar = arr // Assigning arr to ar
            print(arr)
            print(ar)

        if __name__ == "__main__":
            main()

    * Explanation :
        So here we will be having both memories :

            In stack : 
                        a. We will have block for main.

                        b. Variable x is also stored.

                        c. arr is also stored but with no values. with some reference address.

                        d. ar is also stored but with no values and same reference as of arr.
            
            In Heap :
                        a. We will have the address of arr with "#4k", with values a '0,0,0'

                        b. Now for "ar" array, there will be no new space in the heap, since we are assigning the exisiting array to the new one. So the address of this array "ar" will have same reference/address as of array "arr". (This is called Shallow Copy)

* Eg : Changing the reference : Call by value

            def main():
                arr = [0]*3 // Initally #4k
                arr[1] = 5
                arr[2] = 9

                arr = [0]*5
                print(arr) // prints #7k

    * Explanation :
                1. Initially we create a heap of #4k address
                2. Now we assign some values to the arr indices.
                3. Now we assign the exisiting arr to new size with new reference
                4. The previous address will be lost.

* Eg : Both heap and stack memory (Call By Reference)
            def fun(a):
                print(a)
                a[1] = 5
            
            def main():
                ar = [0]*3
                print(ar)
                ar[0] = 90
                ar[1] = 50
                fun(ar)
                print(ar)
            
            if __name__ == "__main__":
                main()

    * Explanation :
                1. Start with main function block in the call stack.
                2. In main block , we have ar(#9k) in the heap.
                3. Now, update the values given, which will get updated in the heap memory.
                4. Now fun() call will appear in the call function.
                5. fun() has a parameter, which will have same reference as of ar in the main functiom.
                6. Now, update a[1] in the heap and after execution , in the call stack this block will get removed but in the heap it will remain same.

                    * This is because there is another pointer referencing to the same address. If not, that heap memory will also get removed.
                
                