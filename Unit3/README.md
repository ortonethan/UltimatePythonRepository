This material is adapted from the [University of Helsinki Python Programming MOOC](https://programming-24.mooc.fi/). The original material is licensed under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license. The original material has been modified from its original form.

## Table Of Contents

- [3.1 - Basic String Operations](#31---basic-string-operations), [Exercises](#31-exercises)

## 3.1 - Basic String Operations

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

## 3.1 Exercises

These exercises are to be done in the [1BasicStringAssignment.py](1BasicStringAssignment.py) file

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
