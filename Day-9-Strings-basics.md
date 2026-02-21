# STRING : SEQUENCE OF CHARACTERS.

* Representation : str = "" (or) name = ''

* Strings are immutable(cannot change the contents of the string).

# CHARACTER : A symbol that represents a number or letter or special Symbol or anything.

* Every character stores some value using ASCII Value.

* ASCII of 'a' to 'z' - 97 to 122

* ASCII of 'A' to 'Z' - 65 to 90

* ASCII of '0' to '9' - 48 to 57

* ord() - used to find the ASCII value of the character.

# SUBSTRINGS:

* 1. Continguous part of string.
* 2. A single chaacter is also a substring.
* 3. Whole string is a substring.
* 4. Empty string is not a substring.
* 5. String of length N, total number of subsrtings = N*(N+1)//2.


# String Interning ( String Pooling) :

* Python uses a memory optimization technique called string interning, often referred to as string pooling, where identical immutable string objects are reused to save memory and speed up string comparisons. This happens automatically for certain strings, but it is an implementation detail of the CPython interpreter and should not be relied upon for guaranteed behavior.

* How String Interning Works
    1. String Pool: Python maintains an internal "pool" or dictionary of common strings in memory.
    
    2. Reuse: When a new string is created, Python checks if an identical string already exists in the pool. If it does, the existing object's reference is reused, and no new memory is allocated.
    
    3. Immutability: String interning is possible because strings in Python are immutable. This ensures that if multiple variables point to the same string object, changing the value of one variable is impossible; instead, a new string object is created, which prevents unintended side effects