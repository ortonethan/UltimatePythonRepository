This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [3.1 - While Loops](#31---while-loops), [Exercises](#31-exercises)
- [3.2 - Basic String Operations](#32---basic-string-operations), [Exercises](#32-exercises)

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

## 3.2 - Basic String Operations

### + and \* operators

Strings can be concatenated (joined) using the `+` operator:

```python
begin = "ex"
end = "ample"
word = begin+end
print(word)
```

Strings can be repeated using the `*` operator:

```python
word = "banana"
print(word*3)
```

### len of a string

The `len` function returns the length of a string. So this snippet prints a word underlined:

```python
word = input("Type in a word: ")
print(word)
print("-"*len(word))
```

### indexing strings to get individual characters

The `[]` operator can get a single character from the string when passed in an index (or position). Indexing starts at 0, so `[0]` will get the first letter, `[1]` the second, and so on.

```python
word = input("Type in a word: ")
print(word[0])
print(word[1])
print(word[2])
### ...
print(word[len(word) - 1])
```

Python also allows negative indexing, which starts from the end of the string. `[-1]` gets the last character, `[-2]` the second last, and so on. So this code prints the first and last character of a word:

```python
word = input("Type in a word: ")
print(word[0])
print(word[-1])

```

## 3.2 Exercises

These exercises are to be done in the [2BasicStringAssignment.py](2BasicStringAssignment.py) file

1. Ask the user for a string, and an amount. Then print out the string as many times as specified by the amount. The printout should all be on one line. For example:

   ```text
   Please type in a string: hiya
   Please type in an amount: 4
   hiyahiyahiyahiya
   ```

2. Ask the user for two strings and then print out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

   ```text
   Please type in string 1: hey
   Please type in string 2: hiya
   hiya is longer
   ```

   ```text
   Please type in string 1: howdy doody
   Please type in string 2: hola
   howdy doody is longer
   ```

   ```text
   Please type in string 1: hey
   Please type in string 2: bye
   The strings are equally long
   ```

3. Ask the user for a string. Print out the input string in reversed order, from end to beginning. Each character should be on a separate line.

   ```text
   Please type in a string: hiya
   a
   y
   i
   h
   ```

4. Ask the user for a string. Print a message about whether the second character and the second to last character are the same or not. See the examples below.

   ```text
   Please type in a string: python
   The second and the second to last characters are different
   ```

   ```text
   Please type in a string: pascal
   The second and the second to last characters are a
   ```

5. Print a line of hash characters (`#`), the width of which is chosen by the user.

   ```text
   Width: 3
   ###
   ```

   ```text
   Width: 8
   ########
   ```

6. Ask for a width and a height, and print a rectangle of hash characters accordingly.

   ```text
   Width: 10
   Height: 3
   ##########
   ##########
   ##########
   ```

7. Keep asking the user for strings using a loop. Print each string underlined as shown in the examples below. Stop when the user enters an empty string - that is, just presses Enter at the prompt.

   ```text
   Please type in a string: Hi there!

   Hi there!
   ---------

   Please type in a string: This is a test

   This is a test
   --------------

   Please type in a string: a

   a
   -

   Please type in a string:
   ```

8. Ask the user for a string and then print it so that exactly 20 characters are displayed. If the string is shorter than 20 characters, the beginning of the line is filled in with `*` characters.

   You may assume the input string is at most 20 characters long.

   ```text
   Please type in a string: python

   **************python
   ```

   ```text
   Please type in a string: alongerstring

   *******alongerstring
   ```

   ```text
   Please type in a string: averyverylongstring

   *averyverylongstring
   ```

9. Ask the user for a string and then print a frame of `*` characters with the word in the center. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

   If the length of the input string is an odd number, the word can be in either of the two possible center locations.

   ```text
   Word: testing

   ******************************
   *          testing           *
   ******************************
   ```

   ```text
   Word: python

   ******************************
   *           python           *
   ******************************
   ```
