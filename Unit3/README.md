This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [3.1 - While Loops](#31---while-loops), [Exercises](#31-exercises)
- [3.2 - Basic String Operations](#32---basic-string-operations), [Exercises](#32-exercises)
- [3.3 - Slices and Searching](#33---slices-and-searching), [Exercises](#33-exercises)
- [3.4 - Functions Intro](#34---functions-intro), [Exercises](#34-exercises)

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

## 3.3 - Slices and Searching

### Slices

By using indexes, we've extracted single letters from strings. It's also possible to extract a part of the string longer than one letter, by "slicing":

```python
original = "presumptious"

slice1 = original[0:3]
print(slice1) # left index is included, right is not
slice2 = original[4:10]
print(slice2) # left index is included, right is not
slice3 = original[:3]
print(slice3) # omitted left index defaults to zero
slice4 = original[4:]
print(slice4) # omitted right index defaults to length
```

### Checking _if_ a substring appears using `in`

```python
string = "test"

print("t" in string)
print("x" in string)
print("es" in string)
print("ets" in string)
```

### Checking _where_ a substring appears using `find`

```python
string = "test"

print(string.find("t"))
print(string.find("x"))
print(string.find("es"))
print(string.find("ets"))
```

## 3.3 Exercises

Complete these exercises in the [3SlicesAndSearchingAssignment.py](3SlicesAndSearchingAssignment.py) file.

1. Ask the user to type in a string. Print all the substrings which begin with the first character, from the shortest to the longest.

   ```text
   Please type in a string: test
   t
   te
   tes
   test
   ```

2. Ask the user to type in a string. Print all the substrings which end with the last character, from the shortest to the longest.

   ```text
   Please type in a string: test
   t
   st
   est
   test
   ```

3. Ask the user to enter a string. Report whether the vowels a, e, or o are found.

   You may assume the input will be in lowercase

   ```text
   Please type in a string: hello there
   a not found
   e found
   o found
   ```

   ```text
   Please type in a string: hiya
   a found
   e not found
   o not found
   ```

4. Ask the user to type in a string and then a single character. Print the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

   Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

   ```text
   Please type in a word: mammoth
   Please type in a character: m
   mam
   ```

   ```text
   Please type in a word: banana
   Please type in a character: n
   nan
   ```

   ```text
   Please type in a word: tomato
   Please type in a character: x
   ```

   ```text
   Please type in a word: python
   Please type in a character: n
   ```

5. Make an extended version of the previous part, which prints out _all_ the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

   ```text
   Please type in a word: mammoth
   Please type in a character: m
   mam
   mmo
   mot
   ```

   ```text
   Please type in a word: banana
   Please type in a character: n
   nan
   ```

   Hint: the following python code may give you some inspiration as to how this exercise could be tackled:

   ```python
   word = input("Word: ")
   while True:
   if len(word) == 0:
   break
   print(word)
   word = word[2:]
   ```

   ```text
   Word: mammoth
   mammoth
   mmoth
   oth
   h
   ```

6. Write code which finds the second occurrence of a substring. If there is no second (or first) occurrence, print out a message accordingly.

   ```text
   Please type in a string: abcabc
   Please type in a substring: ab
   The second occurrence of the substring is at index 3.
   ```

   ```text
   Please type in a string: methodology
   Please type in a substring: o
   The second occurrence of the substring is at index 6.
   ```

   ```text
   Please type in a string: aybabtu
   Please type in a substring: ba
   The substring does not occur twice in the string.
   ```

## 3.4 - Functions Intro

We have already used functions such as len, print and input in our programs. We can also define our own functions using the `def` keyword:

```python
def message():
   print("This is my very own function!")
```

This function is called `message`. But if you run the code, nothing will appear to happen. The is because we have to "call" the function to run the code inside it:

```python
message()
```

It can be called multiple times:

```python
message()
message()
message()
```

We can pass "arguments" to functions. These are values that the function can use when it runs. For example:

```python
def hello(name):
   print("Hello", name, "!")

hello("Alice")
hello("world")
```

Here are other examples:

```python
def squared(x):
    print(f"The square of the number {x} is {x * x}")

squared(2)
squared(5)
```

```python
def sum(x, y):
    result = x + y
    print(f"The sum of the arguments {x} and {y} is {result}")

sum(1, 2)
sum(5, 24)
```

## 3.4 Exercises

Complete these exercises in the [4FunctionsIntroAssignment.py](4FunctionsIntroAssignment.py) file.

1. Write a function named `seven_dwarves`. When the function is called, it should print out the names of the seven dwarves in alphabetical order as shown:

   ```text
   Bashful
   Doc
   Dopey
   Grumpy
   Happy
   Sleepy
   Sneezy
   ```

2. Write a function called `first_character` that takes one argument, and prints out the first character of that argument.

   ```python
   first_character('python')
   first_character('yellow')
   first_character('tomorrow')
   first_character('heliotrope')
   first_character('open')
   first_character('night')
   ```

   ```text
   p
   y
   t
   h
   o
   n
   ```

3. Write a function named `mean`, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.

   ```python
   mean(5, 3, 1)
   mean(10, 1, 1)
   ```

   ```text
   3.0
   4.0
   ```

4. Write a function named `print_many_times(text, times)`, which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out:

   ```python
   print_many_times("hi", 5)

   print()

   text = "All Pythons, except one, grow up"
   times = 3
   print_many_times(text, times)
   ```

   ```text
   hi
   hi
   hi
   hi
   hi

   All Pythons, except one, grow up.
   All Pythons, except one, grow up.
   All Pythons, except one, grow up.
   ```

5. Write a function named `hash_square(length)`, which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

   ```python
   hash_square(3)
   print()
   hash_square(5)
   ```

   ```text
   ###
   ###
   ###

   #####
   #####
   #####
   #####
   #####
   ```

6. Write a function named `chessboard`, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board.

   ```python
   chessboard(3)
   print()
   chessboard(6)
   ```

   ```text
   101
   010
   101

   101010
   010101
   101010
   010101
   101010
   010101
   ```
