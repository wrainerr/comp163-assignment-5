# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")

# Get the starting number from the user and convert it to an integer.
current_number = int(input("Enter starting number: "))
# Initialize a counter for the number of steps.
step_count = 0

# Print the initial part of the output sequence.
print("Sequence:", current_number, end=" ")

# Loop continues as long as the current number is not 1.
while current_number > 1:
    # Check if the number is even.
    if current_number % 2 == 0:
        # If even, divide it by 2.
        current_number //= 2
    # If the number is not even, it must be odd.
    else:
        # If odd, multiply by 3 and add 1.
        current_number = (current_number * 3) + 1
    
    # Increment the step counter after each operation.
    step_count += 1
    # Print the next number in the sequence on the same line.
    print(current_number, end=" ")

# Print a newline character to move to the next line for the final output.
print() 
# Display the total number of steps taken.
print("Steps:", step_count)
print()


# === Challenge 2: Prime Number Checker ===
print("=== Challenge 2: Prime Number Checker ===")

# Get the number to check from the user.
prime_input = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {prime_input-1}...")

# Loop through all possible divisors from 2 up to the number itself (but not including it).
for i in range(2, prime_input):
    # If the number is evenly divisible by any 'i', it's not prime.
    if prime_input % i == 0:
        # Print the result and the factor that proves it's not prime.
        print(f"{prime_input} is not prime (divisible by {i})")
        # Exit the loop immediately since we've found a divisor.
        break
# The 'else' block runs ONLY if the 'for' loop completes without hitting a 'break'.
else:
    # If the loop finishes, no divisors were found, so the number is prime.
    print(f"{prime_input} is prime!")
print()


# === Challenge 3: Multiplication Table ===
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# This first loop incorrectly prints a header row from 1-10.
# The main loop below also prints row headers, making this part redundant.
for i in range (1, 11):
    print(f"{i:2}", end="")

# Outer loop to iterate through each row number from 1 to 10.
for row in range(1, 11):
    # Print the current row number, formatted to take up 2 spaces.
    print(f"{row:2}", end="")
    # Inner loop to iterate through each column number from 1 to 10.
    for col in range(1, 11):
        # Calculate the product of the current row and column.
        product = row * col
        # Print the product, formatted to take up 4 spaces for alignment.
        print(f"{product:4}", end="")
    # An extra space is printed here before the newline.
    print(" ",end="")
    # After the inner loop completes a row, print a newline to start the next row.
    print()