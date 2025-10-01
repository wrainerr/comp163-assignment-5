# COMP 163: Assignment 5 - Loop Mastery

This repository contains the Python solutions for the "Loop Mastery" assignment. The project includes three challenges, each designed to demonstrate proficiency with a different type of loop structure: `while` loops, `for` loops, and nested `for` loops.

## Challenge 1: Number Sequence Generator

[cite_start]This program implements the Collatz Conjecture sequence. [cite: 8]

### Loop Choice: `while` loop

A **`while` loop** was the ideal choice for this challenge. [cite_start]The Collatz Conjecture continues until the sequence reaches the number 1, but the number of steps required to get there is unknown from the start. [cite: 13, 21] A `while` loop is perfect for situations where the loop must run for an undetermined number of iterations, continuing as long as a specific condition (`current_number > 1`) is true.

### How It Works

1.  [cite_start]The program prompts the user for a positive integer to start the sequence. [cite: 15]
2.  [cite_start]It initializes a `step_count` variable to 0. [cite: 19]
3.  The `while` loop begins, checking if `current_number` is greater than 1.
4.  Inside the loop, it checks if `current_number` is even or odd.
    * [cite_start]If **even**, the number is divided by 2. [cite: 11]
    * [cite_start]If **odd**, it is multiplied by 3 and 1 is added. [cite: 12]
5.  The new number is printed to the sequence, and the `step_count` is incremented.
6.  [cite_start]The loop repeats until `current_number` equals 1, at which point the loop terminates and the final step count is displayed. [cite: 13, 16]

***

## Challenge 2: Prime Number Checker

[cite_start]This program determines if a given number is prime by testing all possible divisors. [cite: 24]

### Loop Choice: `for` loop

[cite_start]A **`for` loop** was used for this problem because the number of iterations is known and finite. [cite: 36] [cite_start]To check if a number `n` is prime, we only need to test for divisors in a specific, predictable range: from 2 up to `n-1`. [cite: 27] A `for` loop is designed for iterating over such a well-defined sequence.

### How It Works

1.  [cite_start]The program asks the user to enter a positive integer greater than 1. [cite: 30]
2.  A `for` loop is initiated to iterate through every number from 2 up to the input number (exclusive).
3.  [cite_start]In each iteration, the modulo (`%`) operator checks if the input number is evenly divisible by the current number in the loop. [cite: 35]
4.  [cite_start]If a divisor is found, the program immediately prints that the number is not prime (including the divisor it found) and the `break` statement terminates the loop. [cite: 28]
5.  [cite_start]If the loop completes without finding any divisors, an `else` block attached to the loop is executed, declaring that the number is prime. [cite: 29]

***

## Challenge 3: Multiplication Table Grid

[cite_start]This program generates and displays a formatted 10x10 multiplication table. [cite: 39]

### Loop Choice: Nested `for` loops

[cite_start]**Nested `for` loops** are required to create a two-dimensional grid like a multiplication table. [cite: 54]
* The **outer loop** is responsible for iterating through each **row** of the table (from 1 to 10).
* The **inner loop** is responsible for iterating through each **column** within the current row (also 1 to 10).

This structure allows us to systematically calculate the product for every `row` and `column` combination.

### How It Works

1.  The outer `for` loop begins, representing the current `row` number (from 1 to 10).
2.  Inside this loop, the `row` number is printed to serve as a row header.
3.  The inner `for` loop then begins, representing the current `col` number (from 1 to 10).
4.  [cite_start]The product of `row * col` is calculated and printed. [cite: 45] [cite_start]Formatted printing (`f-strings`) is used to ensure all the numbers align correctly in the grid. [cite: 52]
5.  The inner loop completes after printing all 10 products for the current row.
6.  [cite_start]A `print()` statement is then called to move the cursor to the next line, preparing for the next row. [cite: 47]
7.  The outer loop continues until all 10 rows have been generated and printed.

***

## AI Assistance

An AI (Gemini) was used to generate the text and structure for this `README.md` file. [cite_start]The process involved providing the AI with the assignment requirements document and the completed Python source code, then requesting it to create the documentation explaining the loop choices and solution logic as required. [cite: 60]