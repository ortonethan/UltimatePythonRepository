This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [1.1 - Print Statements](#11-print-statements), [Exercises](#11-exercises)
- [1.2 - Input From User](#12-input-from-user), [Exercises](#12-exercises)
- [1.3 - Variables](#13-variables), [Exercises](#13-exercises)
- [1.4 - Arithmetic Operators](#14-arithmetic-operators), [Exercises](#14-exercises)
- [1.5 - Conditionals](#15-conditionals), [Exercises](#15-exercises)

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

## 1.4 Arithmetic Operators

### Available operators:

```python
print("Adding: 5 + 3 =", 5 + 3)
print("Subtracting: 7 - 2.5 =", 7 - 2.5)
print("Multiplying: -1.5 * 3 =", -1.5 * 3)
print("Dividing (producing decimal): 11 / 4 =", 11 / 4)
print("Dividing (rounding down to produce whole number): 11 // 4 =", 11 // 4)
print("Modulo (calculates the remainder of the first number divided by the second): 11 % 4 =", 11 % 4)
print("Exponentiation (powers): 2 ** 3 =", 2 ** 3)
```

### Reading integers and floats from input

You need to convert the input to a number type before using arithmetic operators:

```python
year_str = input("What year were you born in? ")
year = int(year_str)
print("You are", 2024 - year, "or", 2024 - year - 1, "years old")
```

```python
height = float(input("What is your height in meters?"))
weight = float(input("What is your weight in kilograms?"))
bmi = weight / height ** 2
print("Your BMI is", bmi)
```

### Arithmetic to existing variables

Python code to take three numbers from input and calculate their sum:

```python
number1 = int(input("Please enter a number"))
number2 = int(input("Please enter a number"))
number3 = int(input("Please enter a number"))

sum = number1 + number2 + number3
print("The sum of the numbers is", sum)
```

Using two variables instead:

```python
sum = 0
number = int(input("Please enter a number"))
sum = sum + number
number = int(input("Please enter a number"))
sum = sum + number
number = int(input("Please enter a number"))
sum = sum + number

print("The sum of the numbers is", sum)
```

Using the `+=` shorthand:

```python
sum = 0
number = int(input("Please enter a number"))
sum += number
number = int(input("Please enter a number"))
sum += number
number = int(input("Please enter a number"))
sum += number

print("The sum of the numbers is", sum)
```

## 1.4 Exercises

These exercises are to be done in the [4ArithmeticAssignment.py](4ArithmeticAssignment.py) file

1. Write a code which asks the user for a number. The program then prints out the number multiplied by five. It should look like this:

   ```text
   Please type in a number: 3
   3 times 5 is 15
   ```

2. Write code which asks the user for their name and year of birth. The program then prints out a message as follows:

   ```text
   What is your name? Frances Fictitious
   Which year were you born? 1990
   Hi Frances Fictitious, you will be 34 years old at the end of the year 2024
   ```

3. Write code which asks the user for a number of days. The code then prints out the number of seconds in the amount of days given.

   Examples:

   ```text
   How many days? 1
   Seconds in that many days: 86400

   How many days? 7
   Seconds in that many days: 604800
   ```

4. The code asks the user for three numbers. It then prints out their product, that is, the numbers multiplied by each other. There is, however, something wrong with the code - it doesn't work quite right, as you can see if you run it. Fix it.

   An example of the expected execution of the program:

   ```text
   Please type in the first number: 2
   Please type in the second number: 3
   Please type in the third number: 5
   The product is 30
   ```

5. Write code which asks the user for two numbers. It will then print out the sum and the product of the two numbers.

   The program should function as follows:

   ```text
   Number 1: 3
   Number 2: 7
   The sum of the numbers: 10
   The product of the numbers: 21
   ```

6. Write code which asks the user for four numbers. It then prints out the sum and the mean of the numbers.

   The program should function as follows:

   ```text
   Number 1: 2
   Number 2: 1
   Number 3: 6
   Number 4: 7
   The sum of the numbers is 16 and the mean is 4.0
   ```

7. Write a program which estimates a user's typical food expenditure.

   The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

   Based on this information the program calculates the user's typical food expenditure both weekly and daily.

   The program should function as follows:

   ```text
   How many times a week do you eat at the student cafeteria? 4
   The price of a typical student lunch? 2.5
   How much money do you spend on groceries in a week? 28.5

   Average food expenditure:
   Daily: $5.5
   Weekly: $38.5
   ```

8. (+) Write code which asks for the number of students on a course and the desired group size. It will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

   Hint: the integer division operator `//` could come in handy here.

   ```text
   How many students on the course? 8
   Desired group size? 4
   Number of groups formed: 2

   How many students on the course? 11
   Desired group size? 3
   Number of groups formed: 4
   ```

## 1.5 Conditionals

Just like in AppInventor, we can use `if` statements to make decisions:

```python
age = int(input("How old are you? "))
if age >= 18:
   print("You are old enough to vote.")
   print("Here is a ballot")
print("Next, please")
```

Note the colon (`:`) following the `if` statement, and the indented code block.

We used the greater than or equals operator (`>=`) in the example above. Here are some other comparison operators:

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `a == b` |
| `!=`     | Not equal to             | `a != b` |
| `<`      | Less than                | `a < b`  |
| `<=`     | Less than or equal to    | `a <= b` |
| `>`      | Greater than             | `a > b`  |
| `>=`     | Greater than or equal to | `a >= b` |

Here's code using some of these:

```python
number = int(input("Please type in a number: "))
if number < 0:
   print("The number is negative")
if number > 0:
   print("The number is positive")
if number == 0:
   print("The number is zero")
```

The results of comparison operators are always either `True` or `False`. These are called _boolean values_, and you can save them in variables and use them just like other variables.

```python
a = 3
a_test = a > 5
print("The result of the comparison is: ", a_test)

if a_test:
   print("a is less than 5")
```

You can also directly assign `True` or ``False` to a variable:

```python
result = True
if result:
   print("This prints every time")
```

This isn't useful just now, but the idea will be later.

## 1.5 Exercises

1. Ask the user for an integer number. The program should print "Orwell" if the number is exactly 1984, and otherwise do nothing. For example:

   ```text
   Please type in a number: 1984
   Orwell
   ```

   ```text
   Please type in a number: 2020
   ```

2. Ask the user for an integer number. If the number is less than zero, print out the number multiplied by -1. Otherwise print the number as-is. Intended behavior:

   ```text
   Please type in a number: -7
   The absolute value of this number is 7
   ```

   ```text
   Please type in a number: 1
   The absolute value of this number is 1
   ```

   ```text
   Please type in a number: -99
   The absolute value of this number is 99
   ```

3. Ask for the user's name. If the name is anything but "Jerry", ask for the number of portions and print out the total cost. The price of a single portion is 5.90. Two examples of the intended behavior:

   ```text
   What is your name? Kramer
   How many portions of soup? 2
   The total cost is 11.8
   Next please!
   ```

   ```text
   What is your name? Jerry
   Next please!
   ```

4. Ask the user for an integer number. Print out the magnitude of the number according to the following examples.

   ```text
   Type in a number: 950
   This number is smaller than 1000
   Thank you!
   ```

   ```text
   Type in a number: 59
   This number is smaller than 1000
   This number is smaller than 100
   Thank you!
   ```

   ```text
   Type in a number: 2
   This number is smaller than 1000
   This number is smaller than 100
   This number is smaller than 10
   Thank you!
   ```

5. Ask the user for two numbers and an operation. If the operation is add, multiply or subtract, calculate and print out the result of the operation with the given numbers. If the user types in anything else, print out nothing. Some examples of expected behaviour:

   ```text
   Number 1: 10
   Number 2: 17
   Operation: add

   10 + 17 = 27
   ```

   ```text
   Number 1: 4
   Number 2: 6
   Operation: multiply

   4 * 6 = 24
   ```

   ```text
   Number 1: 4
   Number 2: 6
   Operation: subtract

   4 - 6 = -2
   ```

6. Ask the user for a temperature in degrees Fahrenheit, and print that temperature in degrees Celsius. If the converted temperature falls below zero degrees Celsius, also print out "Brr! It's cold in here!".

   Look up the conversion formula in a search engine.

   Two examples of expected behaviour:

   ```text
   Type in a temperature (F): 101
   101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius
   ```

   ```text
   Type in a temperature (F): 21
   21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
   Brr! It's cold in here!
   ```

7. Ask for the hourly wage, hours worked, and the day of the week. Print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled. For example:

   ```text
   Hourly wage: 8.5
   Hours worked: 3
   Day of the week: Monday
   Daily wages: $25.5
   ```

   ```text
   Hourly wage: 12.5
   Hours worked: 10
   Day of the week: Sunday
   Daily wages: $250.0
   ```

8. The code in the file calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

   - If there are less than a hundred points on the card, the bonus is 10 %
   - In any other case the bonus is 15 %

   It should work like this:

   ```text
   How many points are on your card? 55
   Your bonus is 10 %
   You now have 60.5 points
   ```

   But there is a problem with the program, so with some inputs it doesn't work quite right:

   ```text
   How many points are on your card? 95
   Your bonus is 10 %
   Your bonus is 15 %
   You now have 120.175 points
   ```

   Fix the program so that there is always either a 10% or a 15% bonus, but never both.

9. Ask for tomorrow's weather forecast and then suggest weather-appropriate clothing.

   The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

   Some examples:

   ```text
   What is the weather forecast for tomorrow?
   Temperature: 21
   Will it rain (yes/no): no
   Wear jeans and a T-shirt
   ```

   ```text
   What is the weather forecast for tomorrow?
   Temperature: 11
   Will it rain (yes/no): no
   Wear jeans and a T-shirt
   I recommend a sweater as well
   ```

   ```text
   What is the weather forecast for tomorrow?
   Temperature: 7
   Will it rain (yes/no): no
   Wear jeans and a T-shirt
   I recommend a sweater as well
   Take a jacket with you
   ```

   ```text
   What is the weather forecast for tomorrow?
   Temperature: 3
   Will it rain (yes/no): yes
   Wear jeans and a T-shirt
   I recommend a sweater as well
   Take a jacket with you
   Make it a warm coat, actually
   I think gloves are in order
   Don't forget your umbrella!
   ```
