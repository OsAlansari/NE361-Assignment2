#This program is used to find the multiplicative inverse of a number in a modulos system.
import math

#Getting the input from the user.
CorrectInput = False
while not CorrectInput:
    try:
        a = int(input("Enter a number \"a\" to find its multiplicative inverse:\t\t\t"))
        if a < 0:
            print("invalid input, the integer must be positive.\n")
            continue

        b = int(input("Enter a number \"b\" which is the modulos the system will work with:\t"))
        if b < 0:
            print("invalid input, the integer must be positive.\n")
            continue

        CorrectInput = True

    except ValueError:
        print("invalid input, it must be an integers.\n")

#Initialising the variables.
b0 = b
a0 = a
r0 = 0
r = 1
q = math.floor(b0 / a0)
s = b0 - q * a0

#Calculating GCM using the extended Euclidean algorithm.
while s > 0:
    temp = r0 - q * r

    if temp >= 0:
        temp = temp % b

    else:
        temp = b - ((-temp) % b)

    r0 = r
    r = temp
    b0 = a0
    a0 = s
    q = math.floor(b0 / a0)
    s = b0 - q * a0

#Checking if the multiplicative inverse exists.
if a0 != 1:
    print(f"\nThe multiplicative inverse of {a} does not exist in modulo {b}.\n")

else:
    r = r % b
    print(f"\nThe multiplicative inverse of {a} in modulo {b} is {r}.\n")