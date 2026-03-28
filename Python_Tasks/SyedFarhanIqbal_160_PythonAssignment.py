# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
Lst : list = []
for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
        Lst.append(i)
print(Lst)

#Write a program that prints Factorial of a user given integer without using math.factorial() function.

num = int(input("Enter a number: "))
factorial = 1   
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")        
    
elif num == 0:
   print("The factorial of 0 is 1")
else:  
    for i in range(1,num + 1):
       factorial = factorial*i
    print("The factorial of",num,"is",factorial)


#Write a Python program that prints each item and its corresponding type from the following list.Output (sample): Value: 1452 | Type: int


Lst  = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in Lst:
    print("Value:", item, "| Type:", type(item))

#Write a Python program to find numbers between 100 and 400 (both included) where each digit of anumber is an even number. The numbers obtained should be printed in a comma-separated sequence.

numbers = []
for num in range(100, 401):
    str_num = str(num)
    if all(int(digit) % 2 == 0 for digit in str_num):
        numbers.append(str_num)
print(", ".join(numbers))


#Write a program that takes input an integer number and prints all of its Divisors.

Lst1=[]
num = int(input("Enter an Integer: "))
for i in range(1,num+1):
    if num%i==0:
        Lst1.append(i)
print("The Divisors of", num, "are:", Lst1)

#Write a program that takes input two integer numbers and prints all the common divisors.Example 1: Numbers 100 and 80 → common divisors are 1, 2, 5, 20Example 2: Numbers 72 and 90 → common divisors are 1, 2, 3, 6, 18Test 1: 100 & 80 → [1, 2, 5, 20] | Test 2: 72 & 90 → [1, 2, 3, 6, 18]


num1 = int(input("Enter first number for common divisor : "))
num2 = int(input("Enter first number for common divisor : "))

limit = min(num1, num2)
lst1= [i for i in  range(1,limit+1) if num1%i==0 and num2%i==0]
print("The common divisors of", num1, "and", num2, "are:", lst1)


#Extend the logic of last object: write a program that takes input two integer numbers and prints theHighest Common Factor (also called Greatest Common Divisor).Example 1: Numbers 100 and 80 → HCF = 20Example 2: Numbers 72 and 90 → HCF = 18Test 1: 100 & 80 → HCF = 20 | Test 2: 72 & 90 → HCF = 18

num1 = int(input("Enter first number for HCF : "))
num2 = int(input("Enter first number for HCF : "))
limit = min(num1, num2)
hcf = 1
for i in range(1, limit - 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
       
print("The HCF of", num1, "and", num2, "is:", hcf)


#Write a function that takes length and width as parameters and returns the area of a rectangle.
def area_of_rectangle(length, width):
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
result = area_of_rectangle(length, width)
print("The area of the rectangle is:", result)

#Write a function that takes radius as a parameter and returns the area of a circle. (Use 3.14 for π)
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
result = area_of_circle(radius)
print("The area of the circle is:", result)

#Write a function that accepts a string and returns its reverse.

def reverse_string(s):
    return s[::-1]
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print("The reversed string is:", reversed_string)


#Write a function that takes an integer and returns the sum of all its digits.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
number = int(input("Enter an integer: "))
result = sum_of_digits(number)  
print("The sum of digits of", number, "is:", result)


#Write a function that takes a number and returns True if it is prime, otherwise False.

def num_is_prime(n):

    for i in range(2,int((n/2)+1)):
        if n%i==0:
            return False
    
    return True

num = int(input("Find num is prime or not : "))
is_prime = num_is_prime(num)

print(is_prime)

#Write a function that takes n and prints the first n Fibonacci numbers.

num = int(input("Enter how many numbers to print: "))

def print_fibonacci(n):
    
    a, b = 0, 1
    for i in range(n):
        print(a, end=", ") 
        a, b = b, a + b

print_fibonacci(num)


#Write a function that accepts a string and returns the count of vowels in it.
def count_vowels(s):

    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("The number of vowels in the string is:", vowel_count)


#Write a function that computes base^exponent without using the ** operator or pow().


def power(base, exponent):

    result = 1
    for _ in range(exponent):
        result *= base
    return result   

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))   
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")