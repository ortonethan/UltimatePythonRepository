This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [2.1 - More Conditionals](#21---more-conditionals), [Exercises](#21-exercises)
- [2.2 - Compound Conditions](#22---compound-conditions), [Exercises](#22-exercises)
- [2.3 - While True Loops](#23---while-true-loops), [Exercises](#23-exercises)

## 2.1 - More Conditionals

The `elif` and `else` statements can be added to the end of an `if` statement to implement functionality similar to that in AppInventor. For example, code from the previous section:

```python
number = int(input("Please type in a number"))
if number > 0:
    print("number is positive")
if number < 0:
    print("number is negative")
if number == 0:
    print("number is zero")
```

can be re-written:

```python
number = int(input("Please type in a number"))
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")
```

There is no limit to how many `elif` branches are included, and the `else` branch is optional. The `else` branch is executed if none of the `if` or `elif` branches are executed.

## 2.1 Exercises

These exercises are to be done in the [1MoreConditionalsAssignment.py](1MoreConditionalsAssignment.py) file

1. The function `len` can be used to find out the length of a string. It returns the number of characters in a string.

   Some examples of how this works:

   ```python
   word = "abcd"
   print(len(word)) # prints 4

   print(len("hi there")) # prints 8

   word2 = "howdydoody"
   length = len(word2)
   print(length) # prints 10

   empty_string = ""
   length = len(empty_string)
   print(length) # print 0
   ```

   Write code which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

   Examples of expected behaviour:

   ```text
   Please type in a word: hey
   There are 3 letters in the word hey
   Thank you!
   ```

   ```text
   Please type in a word: banana
   There are 6 letters in the word banana
   Thank you!
   ```

   ```text
   Sample output
   Please type in a word: b
   Thank you!
   ```

2. When programming in Python, often we need to change the data type of a value. For example, a floating point number can be converted into an integer with the function `int`:

   ```python
   temperature = float(input("Please type in a temperature: "))

   print("The temperature is", temperature)

   print("...and rounded down it is", int(temperature))
   ```

   Try running this code typing in 5.15, and then 8.99. Notice the function always rounds down, and not according to the rounding rules in math.

   Write code which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python `int` function.

   You can assume the number given by the user is always greater than zero.

   An example of expected behaviour:

   ```text
   Please type in a number: 1.34
   Integer part: 1
   Decimal part: 0.34
   ```

3. Write code which asks the user for their age. The program should then print out a message based on whether they may vote or not in elections (you must be 18 or older to do so).

   Some examples of expected behaviour:

   ```text
   How old are you? 12
   You may not vote.
   ```

   ```text
   How old are you? 32
   You may vote!
   ```

4. Write code which asks for two integer numbers. Then print out whichever is greater. If the numbers are equal, the program should print a different message.

   Some examples of expected behaviour:

   ```text
   Please type in the first number: 5
   Please type in another number: 3
   The greater number was: 5
   ```

   ```text
   Please type in the first number:: 5
   Please type in another number: 8
   The greater number was: 8
   ```

   ```text
   Sample output
   Please type in the first number: 5
   Please type in another number: 5
   The numbers are equal!
   ```

5. Write code which asks for the names and ages of two people. It should then print out the name of the elder.

Some examples of expected behaviour:

```text
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada
```

```text
Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
```

6. Python comparison operators can also be used on strings. String `a` is smaller than string `b` if it comes alphabetically before `b`. It's only reliable if the characters compared are of the same case, i.e. both UPPERCASE or both lowercase, and only the standard English alphabet of a to z, or

Write code which asks the user for two words. Then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

```text
Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.
```

```text
Please type in the 1st word: zorro
Please type in the 2nd word: batman
zorro comes alphabetically last.
```

```text
Please type in the 1st word: python
Please type in the 2nd word: python
You gave the same word twice.
```

## 2.2 - Compound Conditions

You can combine conditions with the logical operators `and` and `or`. The operator `and` specifies that all the given conditions must be true at the same time. The operator `or` specifies that at least one of the given conditions must be true.

For example, `number >= 5 and number <= 8` asserts that `number` must simultaneously be at least 5 and at most 8. That is, it must be between 5 and 8.

```python
number = int(input("Please type in a number: "))
if number >= 5 and number <= 8:
    print("The number is between 5 and 8")
```

The condition `number < 5 or number > 8` determines that number must be either less than 5 or greater than 8. That is, it must not be within the range of 5 to 8.

```python
number = int(input("Please type in a number: "))
if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8")
```

The operator `not` can negate a condition. For example, another valid way to check if a number is not within the range of 5 to 8:

```python
number = int(input("Please type in a number: "))
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")
```

Conditions can be chained and combined, for example:

```python
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers.")
```

Conditional statements can also be nested within other conditional statements. For example, the following program checks whether a number is above zero, and then whether it is odd or even:

```python
number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")
```

Some examples of how this program behaves:

```text
Please type in a number: 3
The number is odd
```

```text
Please type in a number: 18
The number is even
```

```text
Please type in a number: -4
The number is negative or zero
```

## 2.2 Exercises

These exercises are to be done in the [2CompoundConditionsAssignment.py](2CompoundConditionsAssignment.py) file

1. Write code which asks for the user's age. If the age is not plausible (under 5, or something that can't be an actual human age), the program should print out a comment.

   See examples:

   ```text
   What is your age? 13
   Ok, you're 13 years old
   ```

   ```text
   What is your age? 2
   I suspect you can't write quite yet...
   ```

   ```text
   What is your age? -4
   That must be a mistake
   ```

2. Write code which asks for the user's name. If the name is "Huey", "Dewey" or "Louie", the program should recognise the user as one of Donald Duck's nephews.

   In a similar fashion, if the name is "Morty" or "Ferdie", the program should recognise the user as one of Mickey Mouse's nephews.

   For example:

   ```text
   Please type in your name: Morty
   I think you might be one of Mickey Mouse's nephews.
   ```

   ```text
   Please type in your name: Huey
   I think you might be one of Donald Duck's nephews.
   ```

   ```text
   Please type in your name: Ken
   You're not a nephew of any character I know of.
   ```

3. The following table gives the grade boundaries for a class:

   | percent | grade       |
   | ------- | ----------- |
   | < 0     | impossible! |
   | 0-59    | F           |
   | 60-69   | D           |
   | 70-79   | C           |
   | 80-89   | B           |
   | 90-100  | A           |
   | > 100   | impossible! |

   Write code which asks for the user's score and then prints out the grade. For example

   ```text
   Type in percent: 77
   Grade: C
   ```

   ```text
   Type in percent: 99
   Grade: A
   ```

   ```text
   Type in percent: 101
   Grade: impossible!
   ```

4. Ask the user for an integer number. If the number is divisible by three, the program should print out "Fizz". If the number is divisible by five, the program should print out "Buzz". If the number is divisible by both three and five, the program should print out "FizzBuzz".

   Some examples of expected behaviour:

   ```text
   Number: 9
   Fizz
   ```

   ```text
   Number: 7
   ```

   ```text
   Number: 20
   Buzz
   ```

   ```text
   Number: 45
   FizzBuzz
   ```

5. Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100 it is not a leap year. Unless it is also divisible by 400, then it is a leap year.

   Ask the user for a year, and then print out whether that year is a leap year or not.

   Some examples:

   ```text
   Please type in a year: 2011
   That year is not a leap year.
   ```

   ```text
   Please type in a year: 2020
   That year is a leap year.
   ```

   ```text
   Please type in a year: 1800
   That year is not a leap year.
   ```

6. Ask the user for three letters. Then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

   You may assume the letters will be either all uppercase, or all lowercase.

   Some examples of expected behaviour:

   ```text
   1st letter: x
   2nd letter: c
   3rd letter: p
   The letter in the middle is p
   ```

   ```text
   1st letter: C
   2nd letter: B
   3rd letter: A
   The letter in the middle is B
   ```

## 2.3 - While True Loops

This code asks the user to type in a number and then prints out the number squared. This continues until the user types in -1.

```python
while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")
```

This code is an infinite loop because it never gets another chance to exit from the loop

```python
number = int(input("Please type in a number, -1 to quit: "))
while True:
    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")
```

Sometimes you can create "helper variables" to help break from the loop at the right time. Suppose someone's PIN code was 1234. The following code gives three attempts to type in the correct PIN:

```python
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
```

This code instead keeps track of all the PIN codes that have been tried:

```python
codes = ""
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    codes += code + ", "

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")

print("Codes attempted were:", codes)
```

## 2.3 Exercises

These exercises are to be done in the [3WhileTrueLoopsIntroAssignment.py](3WhileTrueLoopsIntroAssignment.py) file.

1. Write code to print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then print out "okay then" and finish. For example:

   ```text
   hi
   Shall we continue? yes
   hi
   Shall we continue? oui
   hi
   Shall we continue? jawohl
   hi
   Shall we continue? no
   okay then
   ```

2. Ask the user for integer numbers. If the number is below zero, the program should print out the message "Invalid number". If the number is above zero, the program should print out the square root of the number using the Python `sqrt` function. In either case, the program should then ask for another number. If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

   Here's how to use the `sqrt` function in a python program:

   ```python
   # sqrt function will not work without this line in the beginning of the program
   from math import sqrt

   print(sqrt(9)) # should print 3.0
   ```

   An example of expected behaviour of your program:

   ```text
   Please type in a number: 16
   4.0
   Please type in a number: 4
   2.0
   Please type in a number: -3
   Invalid number
   Please type in a number: 1
   1.0
   Please type in a number: 0
   Exiting...
   ```

3. The code in the file should print out:

   ```text
   Countdown!
   5
   4
   3
   2
   1
   Now!
   ```

   However, the program doesn't quite work. Fix it.

4. Ask the user for a password. Then ask the user to type in the password again. If they type in something other than the password, keep asking until they type it correctly.

   For example:

   ```text
   Password: sekred
   Repeat password: secret
   They do not match!
   Repeat password: cantremember
   They do not match!
   Repeat password: sekred
   User account created!
   ```

5. Keeps asking the user for a PIN code until they type in the correct one, which is 4321. The code should print out the number of times the user tried different codes. If the user gets it right on the first try, it should print out something a bit different:

   ```text
   PIN: 3245
   Wrong
   PIN: 1234
   Wrong
   PIN: 0000
   Wrong
   PIN: 4321
   Correct! It took you 4 attempts
   ```

   ```text
   PIN: 4321
   Correct! It only took you a single attempt!
   ```

6. Ask the user for a year, and print out the next leap year. If the user types a year which is a leap year (such as 2024), the code should print out the following leap year.

   ```text
   Year: 2023
   The next leap year after 2023 is 2024
   ```

   ```text
   Year: 2024
   The next leap year after 2024 is 2028
   ```

7. Write code which keeps asking the user for words. If the user types in "end", print out the story the words formed, and finish.

   ```text
   Please type in a word: Once
   Please type in a word: upon
   Please type in a word: a
   Please type in a word: time
   Please type in a word: there
   Please type in a word: was
   Please type in a word: a
   Please type in a word: girl
   Please type in a word: end
   Once upon a time there was a girl
   ```

8. Like in the previous example, ask the user to type in words. However, in this case, the code should also end if the user types in the same word twice in a row.

   ```text
   Please type in a word: Once
   Please type in a word: upon
   Please type in a word: a
   Please type in a word: time
   Please type in a word: there
   Please type in a word: was
   Please type in a word: a
   Please type in a word: girl
   Please type in a word: end
   Once upon a time there was a girl
   ```

9. Ask the user for (integer) numbers until they type in the number 0. After this, print out how many numbers have been typed in, their sum, their mean (aka average), and how many positive and negative numbers have been typed in. For example:

   ```text
   Please type in integer numbers. Type in 0 to finish.
   Number: 5
   Number: 22
   Number: 9
   Number: -2
   Number: 0
   Numbers typed in: 4
   Sum of numbers: 34
   Mean of numbers: 8.5
   Positive numbers: 3
   Negative numbers: 1
   ```
