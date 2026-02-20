# BIT MANIPULATION BASICS

* Decimal Number System : Number with base-10,which there are 10 different values(0-9).

* Binary Number System : Number with Base-2, which consists of only 0 and 1.

* Conversions :
    1. Binary to Decimal : Multiply with powers of 2 starting from unit's place(or) first place to get decimal number.

    2. Decimal to Binary : Divide the decimal number with 2 and end with 0 as quotient and write the remainder in the reverse order to get binary number.

* To obtain binary of a number using in-built operation : s = format(n, '032b') # For all the bits of whatever the size is.

# BITWISE OPERATORS : Operators which are performed on individual bits.

* Bitwise operators :
    1. ! - Not (Inverse the bits i.e., '0' becomes '1' and '1' and becomes '0')

    2. & - And ( If both bits '1', then the resulting bit will be '1', else '0')

    3. | - Or ( If both bits '0', then the resulting bit will be '0', else '1')

    4. ^ - XOR(If both bits are same , then the resulting bit will be '0', else '1')

    5. << - Left Shift(Shifts every bit by 1 to the left and adds '0' to the last bit (or) 0th bit)

    6. >> - Right Shift(Shifts every bit by 1 to the right and adds '0' to the first bit)

* We can perform directly these operations on decimal numbers without acutally converting them into binary.

# REPRESENTATION OF NEGATIVE NUMBERS(2's Complement) :

* 1. Convert the absolute value of number to Binary representation.
  2. Invert all the bits of number obtained in step 1.
  3. Add 1 to the number obtaied in step 2.

* Signed number : The left-most significant bit is the signed bit.
                  It signifies not only the sign but also magnitude.
                  The last bit is '1' then it is negative decimal number.
                  It checks with the range(No of bits).

* 2's Complement : "s = format(n & 0xffffffff, '032b')"

# RANGE OF DATA TYPES :

* Number of Bits   -       Min Range      -       Max Range
         2                     -2                     1
         4                     -2^4                   2^3-1
         8                     -2^8                   2^7-1
         16                    -2^16                  2^15-1
         32                    -2^32                  2^31-1

* Range of bits = (-2^n-1) to (2^n-1)-1


