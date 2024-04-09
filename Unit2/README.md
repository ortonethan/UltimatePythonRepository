This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [2.1 - More Conditionals](#21---more-conditionals), [Exercises](#21-exercises)

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
