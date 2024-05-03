This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [4.1 - Printing Functions](#41---printing-functions), [Exercises](#41-exercises)

## 4.1 - Printing Functions

### Nested function calls

It's possible to call functions within functions. For example,

```python
def greet(name):
    print("Hello there,", name)

def greet_many_times(name, times):
    while times > 0:
        greet(name)
        times -= 1

greet_many_times("Emily", 3)
```

## 4.1 Exercises

Complete these exercises in the [1PrintingFunctionsAssignment.py](1PrintingFunctionsAssignment.py) file.

1. Write a function named `line`, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.

   For example, these function calls:

   ```python
   line(7, "%")
   line(10, "LOL")
   line(3, "")
   ```

   should print this:

   ```text
   %%%%%%%
   LLLLLLLLLL
   ***
   ```

2. Write a function named `box_of_hashes`, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

   The function should call the function `line` from the exercise above for the actual printing out. Don't change anything in your `line` function.

   This python code:

   ```python
   box_of_hashes(5)
   box_of_hashes(2)
   ```

   Should print this:

   ```text
   ##########
   ##########
   ##########
   ##########
   ##########

   ##########
   ##########
   ```

3. Write a function named `square_of_hashes`, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square.

   The function should call the function `line` from the exercise above for the actual printing out. Don't change anything in the `line` function.

   This python code:

   ```python
   square_of_hashes(5)
   print()
   square_of_hashes(3)
   ```

   Should print this:

   ```text
   #####
   #####
   #####
   #####
   #####

   ###
   ###
   ###
   ```

4. Write a function named `square`, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

   The function should call the function `line` from the exercise above for the actual printing out. Don't change anything in the `line` function.

   This python code:

   ```python

   square(5, "*")
   print()
   square(3, "o")
   ```

   Should print this:

   ```text
   *****
   *****
   *****
   *****
   *****

   ooo
   ooo
   ooo
   ```

5. Write a function named `triangle`, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

   The function should call the function `line` from the exercise above for the actual printing out. Don't change anything in the `line` function.

   This python code:

   ```python

   triangle(6)
   print()
   triangle(3)
   ```

   Should print this:

   ```text
   #
   ##
   ###
   ####
   #####
   ######

   #
   ##
   ###
   ```

6. Write a function named `shape`, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

   The function should call the function `line` from the exercise above for the actual printing out. Don't change anything in the `line` function.

   This python code:

   ```python

   shape(5, "X", 3, "*")
   print()
   shape(2, "o", 4, "+")
   print()
   shape(3, ".", 0, ",")
   ```

   Should print this:

   ```text
   X
   XX
   XXX
   XXXX
   XXXXX
   *****
   *****
   *****

   o
   oo
   ++
   ++
   ++
   ++

   .
   ..
   ...
   ```

7. Write a function named `spruce`, which takes one argument. The function prints out the text `a spruce!`, and then a spruce tree, the size of which is specified by the argument.

   Calling `spruce(3)` should print out:

   ```text
   a spruce!
     *
    ***
   *****
     *
   ```

   Calling `spruce(5)` should print out:

   ```plaintext
   a spruce!
       *
      ***
     *****
    *******
   *********
       *
   ```

   NB: to the left of the spruce there should be exactly the right amount of whitespace. The left edge of the tree should be touching the left edge of the text area in the terminal.
