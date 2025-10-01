print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0
print("Sequence:", current_number, end=" ")
while current_number > 1:
    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = (current_number * 3) + 1
    step_count += 1
    print(current_number, end=" ")
print()
print("Steps:", step_count)
print()
