This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [3.1 - While Loops](#31---while-loops), [Exercises](#31-exercises)

## 3.1 - While Loops

Instead of (or in addition to) breaking out of a loop using the `break` statement, you can use a condition in the loop header (instead of just `True`). The code inside the loop executes as long as the condition is `True`. Once the condition is `False`, the loop stops, and code after the loop is executed.

A very common loop pattern involves:

- initializing a variable before the loop
- checking the variable in the loop header condition
- updating the variable inside the loop

For example:

```python
number = 1 # initialization

while number < 10: # condition
    print(number)
    number += 1 # update

print("loop finished")
```

## 3.1 Exercises

Complete these exercises in the [1WhileLoopsAssignment.py](1WhileLoopsAssignment.py) file.

1. Write code which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

2. The code in the file is intended to count down from the number, then say "Go!" as shown below:

   ```text
   Are you ready?
   Please type in a number: 5
   5
   4
   3
   2
   1
   Now!
   ```

   However, the code doesn't work properly. Fix it.

3. Ask the user for a number. Then print out all integer numbers greater than zero but smaller than the input. For example:

   ```text
   Upper limit: 5
   1
   2
   3
   4
   ```

4. Ask the user to type in an upper limit. Then starting at 1, print out all the powers of two in order that are no larger than the upper limit (this involves successively multiplying by 2). For example:

   ```text
   Upper limit: 8
   1
   2
   4
   8
   ```

   ```text
   Upper limit: 20
   1
   2
   4
   8
   16
   ```

   ```text
   Upper limit: 100
   1
   2
   4
   8
   16
   32
   64
   ```

5. The previous exercise printed all the powers of two below an upper limit. Now write code that allows the user to choose the base as well as the upper limit. (in the previous example the base was always two). For example:

   ```text
   Upper limit: 27
   Base: 3
   1
   3
   9
   27
   ```

   ```text
   Upper limit: 1234567
   Base: 10
   1
   10
   100
   1000
   10000
   100000
   1000000
   ```

6. Ask the user to type in a limit. Then calculate the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. For example:

   ```text
   Limit: 2
   3
   ```

   because 1 + 2 = 3 is when the consecutive sum gets to the limit.

   ```text
   Limit: 10
   10
   ```

   because 1 + 2 + 3 + 4 = 10 is when the consecutive sum gets to the limit.

   ```text
   Limit: 18
   21
   ```

   because 1 + 2 + 3 + 4 + 5 + 6 = 21 is when the consecutive sum gets to the limit.
