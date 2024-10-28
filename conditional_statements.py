#q1
num=int(input("enter the number"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")

#q2
num1=int(input("enter the age"))
if num1<18:
    print("you is minor")
elif num1==18:
    print("you is adult")
else:
    print("you is senior citizen")


#q3
num3=int(input("enter the year"))
if (num3 % 4 == 0 and num3 % 100 != 0) or (num3 % 400 == 0):
    print("year is leap year")
else:
    print("year is not leap year")

#q4
num4=int(input("enter the integer"))
if (num4%2)==0:
    print("integer is even")
else:
    print("integer is odd")


#q5
num5=int(input("enter the grade % "))
if num5>90:
    print("A+ grade")
elif num5>80:
    print("B+ grade")
elif num5>60:
    print("C grade")
elif num5>50:
    print("d grade")
elif num5>40:
    print("e grade")
else:
    print("f garde")
#q6
num6=int(input("enter the number"))
num61=int(input("enter the number"))
if num6>num61:
    print("maximum number is",num6)
elif num61>num6:
    print("number is maximum", num61)
#q7
num6=int(input("enter the number"))
num61=int(input("enter the number"))
num62=int(input("enter the number"))
if num6>(num61 and num62):
    print("maximum number is",num6)
elif num61>(num6 and num62):
    print("number is maximum", num61)
elif num62>(num6 and num61):
    print("number is maximum", num62)
#q8
str_1 = input("Enter the string to check if it is a palindrome: ")
str_1 = str_1.casefold ()
rev_str = reversed (str_1)
if str_1 == list (rev_str):
    print ("The string is a palindrome.")
else:
     print ("The string is not a palindrome.")
#q9
a=int(input("enter the side of triangle"))
s=int(input("enter the side of triangle"))
c=int(input("enter the side of triangle"))
b=int(input("enter the side of triangle"))
d = (s-a) * (s-b) * (s-c)
if d>0:
    print("side from a triangle")
else:
    print("side does not triangle")
#q10
char = input("Enter a character: ")
if char.lower() in 'aeiou':
    print(f"{char} is a vowel")
elif char.isalpha():
    print(f"{char} is a consonant")
else:
    print(f"{char} is not a letter")
#q11
num = int(input("Enter a number to check if it's multiple of 3 and 5: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is a multiple of both 3 and 5")
else:
    print(f"{num} is not a multiple of both 3 and 5")
#q12
celsius = float(input("Enter temperature in Celsius: "))
if celsius <= 0:
    print("Freezing")
elif celsius <= 25:
    print("Moderate")
else:
    print("Hot")

#q12
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

#q13
year = int(input("Enter a year: "))
if year % 100 == 0:
    print(f"{year} is a century year")
else:
    print(f"{year} is not a century year")

#q14
number = float(input("Enter a number: "))
start = float(input("Enter range start: "))
end = float(input("Enter range end: "))

if start <= number <= end:
    print(f"{number} is within the range {start}-{end}")
else:
    print(f"{number} is outside the range {start}-{end}")

#q15
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#q16
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3")
elif num % 2 == 0:
    print(f"{num} is divisible by 2 only")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 only")
else:
    print(f"{num} is not divisible by either 2 or 3")
#q17
score = float(input("Enter your score: "))
if score >= 50:
    print("Pass")
else:
    print("Fail")
#q18
text = input("Enter a string: ")
if text.isupper():
    print("Uppercase")
elif text.islower():
    print("Lowercase")
else:
    print("Mixed case")
#q19
num = int(input("Enter a number to check if it's prime: "))
is_prime = True

if num < 2:
    is_prime = False
elif num == 2:
    is_prime = True
elif num % 2 == 0:
    is_prime = False
else:
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

