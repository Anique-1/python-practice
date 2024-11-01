# 1. Print numbers from 1 to 20
print("1. Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# 2. Print even numbers from 1 to 50
print("2. Even numbers from 1 to 50:")
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
print("\n")

# 3. Sum of numbers from 1 to 100
sum_numbers = sum(range(1, 101))
print(f"3. Sum of numbers from 1 to 100: {sum_numbers}\n")

# 4. Multiplication table
def print_multiplication_table(n):
    print(f"4. Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
print_multiplication_table(5)
print()

# 5. Odd numbers between 1 and 100
print("5. Odd numbers between 1 and 100:")
for i in range(1, 101, 2):
    print(i, end=" ")
print("\n")

# 6. Print characters of string
test_string = "Python"
print("6. Characters in string 'Python':")
for char in test_string:
    print(char, end=" ")
print("\n")

# 7. Factorial using while loop
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
print(f"7. Factorial of 5: {factorial(5)}\n")

# 8. Numbers from 10 to 1
print("8. Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# 9. First 10 Fibonacci numbers
print("9. First 10 Fibonacci numbers:")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)
print("\n")

# 10. Count digits in integer
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count
print(f"10. Number of digits in 12345: {count_digits(12345)}\n")

# 11. Reverse of a number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n //= 10
    return reversed_num
print(f"11. Reverse of 12345: {reverse_number(12345)}\n")

# 12. Prime numbers between 1 and 50
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("12. Prime numbers between 1 and 50:")
for i in range(1, 51):
    if is_prime(i):
        print(i, end=" ")
print("\n")

# 13. Pyramid pattern
print("13. Pyramid pattern:")
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
print()

# 14. Break loop example
print("14. Break loop when number is 5:")
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print("\n")

# 15. Sum of even and odd numbers
def sum_even_odd(n):
    even_sum = sum(i for i in range(2, n+1, 2))
    odd_sum = sum(i for i in range(1, n+1, 2))
    return even_sum, odd_sum

even_sum, odd_sum = sum_even_odd(10)
print(f"15. For numbers up to 10:\nEven sum: {even_sum}\nOdd sum: {odd_sum}\n")

# 16. Sum of digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(f"16. Sum of digits in 12345: {sum_of_digits(12345)}\n")

# 17. Number guessing game
def guess_number(target=7):
    print("17. Guess the number game (simplified version):")
    guess = 0
    attempts = 0
    while guess != target and attempts < 3:  # Limited to 3 attempts for demonstration
        guess = int(input(f"Guess a number (attempt {attempts + 1}/3): "))
        attempts += 1
    return guess == target

# 18. Reverse range
print("18. Numbers in reverse (20 to 15):")
for i in range(20, 14, -1):
    print(i, end=" ")
print("\n")

# 19. Squares from 1 to 10
print("19. Squares of numbers 1 to 10:")
for i in range(1, 11):
    print(f"{i}² = {i**2}")
print()

# 20. Countdown timer
def countdown(n):
    print(f"20. Countdown from {n}:")
    for i in range(n, -1, -1):
        print(i, end=" ")
        # In a real timer, you would use time.sleep(1)
countdown(5)
print("\n")