This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [1.1 - Print Statements](#11-print-statements), [Exercises](#11-exercises)
- [1.2 - Input From User](#12-input-from-user), [Exercises](#12-exercises)
- [1.3 - Variables](#13-variables), [Exercises](#13-exercises)

## 1.1 Print Statements

Try running the following code:

- printing with quotes

  ```python
  print("Hello world")
  ```

- printint without any quotes

  ```python
  print(Hello World)
  ```

- multiple lines of print statements

  ```python
  print("a")
  print("bc")
  print("de")
  ```

- printing arithmetic operations

  ```python
  print(2 + 5)
  print(3 * 3)
  print(2 + 2 * 10)
  print("2 + 2 * 10")
  ```

- using comments (ignored by computer, for humans to document their code to others/themselves)

  ```python
  print("Hours in a year:")
  print(365*24) # 365 days, 24 hours in each day
  ```

- using single quotes, so that you can print double quotes

  ```python
  print('Polonius advises, "To thine own self be true."')

  ```

## 1.1 Exercises

These exercises are to be done in the [1PrintingAssignment.py](1PrintingAssignment.py) file

1. Write code to print an emoji to the terminal

2. Modify the code so that the seven dwarf names are printed in alphabetical order.

3. Write code which prints out the following lines exactly as they are written here, punctuation and all:

   ```text
   Row, row, row your boat,
   Gently down the stream.
   Merrily, merrily, merrily, merrily,
   Life is but a dream.
   ```

4. Write code which prints out the number of minutes in a year. Use Python code to perform the calculation.

5. Write a code that shows the following, verbatim:

   ```text
   print("Hello world")
   ```

## 1.2 Input From User

The following program reads in the name of the user with the input command. It then prints it out with the print command. Try running this program a couple of times with different input.

```python
name = input("What is your name? ")
print("Hi there, " + name)
```

The word `name` in this program is a variable. Like in AppInventor, a variable can store a value, such as some text or a number. This value can be used later, and it can also be changed.

A variable can be used multiple times in a program. For example:

```python
name = input("What is your name? ")

print("Hi, " + name + "!")
print(name + " is quite a nice name.")
```

Inside the first `print` command, the three strings (pieces of text) `"Hi,"`, `name`, and `"!"` are _concatenated_ (joined together) to make a single string. This is similar to the `join` block in AppInventor.

A program can ask for more than one input; each input command stores the received value in a different variable in the example below:

```python
name = input("What is your name? ")
email = input("What is your email address? ")
nickname = input("What is your nickname? ")

print("Let's make sure we got this right")
print("Your name: " + name)
print("Your email address: " + email)
print("Your nickname: " + nickname)
```

If the same variable is used to store more than one input, each new value will replace the previous one. For example:

```python
address = input("What is your address? ")
print("So you live at address " + address)

address = input("Please type in a new address: ")
print("Your address is now " + address)
```

This means that if the same variable is used to store two inputs in succession, there is no way to access the first input value after it has been replaced by the second:

```python
address = input("What is your address? ")
address = input("Please type in a new address: ")

print("Your address is now " + address)
```

## 1.2 Exercises

These exercises are to be done in the [2InputAssignment.py](2InputAssignment.py) file

1.  write a program which asks for the user's name and then prints it twice, on two consecutive lines.
    An example of the how the program should function:

    ```text
    What is your name? Paul
    Paul
    Paul
    ```

2.  write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.

    The program should function as follows:

    ```text
    What is your name? Paul
    !Paul!Paul!
    ```

3.  write a program which asks for the user's name and address. The program should then print out the information in the format shown:

    ```text
    Enter your first name: Maize
    Enter your last name: South
    Enter your street address: 3701 N Tyler Rd
    Enter your address city: Wichita
    Enter your address state: KS
    Enter your zip code: 67205
    Maize South
    3701 N Tyler Rd
    Wichita, KS 67205
    ```

4.  Here is how your code should function: it should ask for three utterances and then print them in the specified format. Fix the code in the exercises file.

    ```text
    The 1st part: hickory
    The 2nd part: dickory
    The 3rd part: dock
    hickory-dickory-dock!
    ```

5.  Write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.

    ```text
    Please type in a name: Mary
    Please type in a year: 1572

    Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.
    ```

## 1.3 Variables

### Setting and Changing Variables

So far, variables have been stored from the `input` command:

```python
name = input("What is your name? ")
print("Hi, " + name)
```

They can also be "hard-coded" into the program:

```python
first_name = "Alice"
last_name = "Cooper"
```

And variables can be used to set other variables:

```python
full_name = first_name + " " + last_name
```

Variables can be completely overwritten like here:

```python
letter = "a"
letter = "b"
```

Or they can be modified like this:

```python
word = "python"
word = word + "!!!"
```

### Variable Types

Different data types may look the same:

```python
number1 = 100
number2 = "100"

print(number1)
print(number2)
```

But may act differently:

```python
print(number1 + number1)
print(number2 + number2)

print(number1 / 2)
print(number2 / 2)
```

### Printing With Types

This doesn't work:

```python
secret_number = 42
print("The secret number is: " + secret_number)
```

So we can:

- use `str` to convert the number to a string:
  ```python
  print("The secret number is: " + str(secret_number))
  ```
- use commas to separate the strings and variables:
  ```python
  print("The secret number is:", secret_number)
  ```
- use f-strings:
  ```python
  print(f"The secret number is: {secret}")
  ```

### Floating Point Numbers

In programming, these are numbers with decimal points. They can be used very similarly to integers:

```python
num1 = 2.5
num2 = -1.25
num3 = 3.62

mean = (num1 + num2 + num3) / 3
print(f"Mean: {mean}")
```

## 1.3 Exercises

These exercises are to be done in the [3VariablesAssignment.py](3VariablesAssignment.py) file

1. A friend is working on a resume job-seeking app. They want the information to print _exactly_ like this (down to how many space characters are displayed):

   ```text
   my name is Tim Tester, I am 20 years old

   my skills are
   - python (beginner)
   - java (veteran)
   - programming (semiprofessional)

   I am looking for a job with a salary of 2000-3000 dollars per month
   ```

   Fix the code in the file so the formatting is exactly right.

2. Keep the `x = 27` and `y = 15` statements in the code. Below those lines, write code so that the program prints out the following:

   ```text
   27 + 15 = 42
   27 - 15 = 12
   27 * 15 = 405
   27 / 15 = 1.8
   ```

   The code should still work if we change the values of `x` and `y`. For example, if we changed them to `x = 4` and `y = 9`, the program should display:

   ```text
   4 + 9 = 13
   4 - 9 = -5
   4 * 9 = 36
   4 / 9 = 0.4444444444444444
   ```

3. Each print command usually prints out a line of its own, complete with a new line at the end. However, if the print command is given an additional argument `end = ""`, it will not start a new line.

   For example:

   ```python
   print("Hi ", end="")
   print("there!")
   ```

   will print

   ```text
   Hi there!
   ```

   Fix the code in the file so that the entire calculation, complete with result, is printed out on a single line. Do not change the number of `print` commands used.
