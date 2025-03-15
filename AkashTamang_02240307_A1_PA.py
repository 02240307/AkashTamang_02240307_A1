import math

# Simple functions for various utilities
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def prime_sum(a, b):
    sum = 0
    for i in range(a, b+1):
        if is_prime(i): sum += i
    return sum

def convert_length(value, ft):
    if ft == 'M': return round(value * 3.28084, 2)
    if ft == 'F': return round(value / 3.28084, 2)
    return None

def count_consonants(text):
    count = 0
    for c in text:
        if c.lower() in "bcdfghjklmnpqrstvwxyz": count += 1
    return count

def find_min_max(nums):
    return min(nums), max(nums)

def is_palindrome(text):
    clean = ""
    for c in text:
        if c.isalnum(): clean += c.lower()
    return clean == clean[::-1]

# Main program
while True:
    print("\nSelect a function (1-6): ")
    print("\nMenu: 1 Calculate the sum of prime Number, \n2. Convert Length Unit, \n3. Count The Consonants in String, \n4. Find the min and max numbers, \n5 Check for Palindrome, \n6. Exit the program")
    choice = input("Enter your choose between(1-6): ")
    
    if choice == '1':
        a = int(input("Start: "))
        b = int(input("End: "))
        print(f"Sum of primes: {prime_sum(a, b)}")
        
    elif choice == '2':
        val = float(input("Value: "))
        ft = input("M (meters→feet) or F (feet→meters): ").upper()
        result = convert_length(val, ft)
        print(f"Result: {result}" if result is not None else "Invalid input")
        
    elif choice == '3':
        text = input("Enter a string: ")
        print(f"Number of Consonants: {count_consonants(text)}")
        
    elif choice == '4':
        nums = []
        n = int(input("How many numbers? "))
        for i in range(n):
            nums.append(float(input(f"Number {i+1}: ")))
        small, large = find_min_max(nums)
        print(f"Min: {small}, Max: {large}")
        
    elif choice == '5':
        text = input("Text: ")
        print("Palindrome!" if is_palindrome(text) else "Not a palindrome")
        
    elif choice == '6':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice")
        
    if input("Would you like to try another Function? (Y/N): ").upper() != 'Y':
        print("Goodbye!")
        break

