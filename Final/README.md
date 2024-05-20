# Computer Programming Final

## Introduction

There are 4 questions in this test. I do not expect anyone to complete them all. If you are stuck on one question, do as much of it as you can, then move onto something different where you can make some progress. I will award partial credit for knowledge that you demonstrate, even if the solution doesn't completely work.

## Question 1

Complete the following exercise in the [q1.py](./q1.py) file.

During the COVID-19 pandemic, Maize schools adopted a hybrid schedule where only half of the students reported each day. The split was based on the position in the alphabet of a student last name.

Many colleges award scholarships based on the GPA of a student.

Ask the user for their first name, their last name, and their academic GPA. Use that information to tell them which days to report to school using the hybrid schedule shown below, and the scholarship they are eligible for using the scholarship table below.

### Hybrid schedule

| Last name starts with letter | Days to report to school building |
| ---------------------------- | --------------------------------- |
| A-K                          | Monday & Thursday                 |
| L-Z                          | Tuesday & Friday                  |

### Scholarship

| GPA             | Scholarship Amount |
| --------------- | ------------------ |
| 3.86+           | $16000             |
| 3.7 - 3.85      | $12000             |
| 3.5 - 3.69      | $8000              |
| 3.25 - 3.49     | $4000              |
| lower than 3.25 | $0                 |

### Examples of Code Being Run

```plaintext
Please enter your first name: Donna
Please enter your last name: Noble
Please enter your GPA: 3.66

Hello, Donna. You should report to school on Tuesday and Friday. You are eligibile for a scholarship of $8000.
```

```plaintext
Please enter your first name: Peter
Please enter your last name: Bern
Please enter your GPA: 2.5

Hello, Peter. You should report to school on Monday and Thursday. You are eligibile for a scholarship of $0.
```

## Question 2

Complete the following exercise in the [q2.py](./q2.py) file.

A vending machine sells snacks for 50 cents. It accepts quarters (25 cents), dimes (10 cents), and nickels (5 cents). Write code that keeps asking the user to insert coins until enough money has been entered to pay for a snack. It should then display how much change is owed.

### Examples of Code Being Run

```plaintext
Amount due: 50
Insert coin: 25
Amount due: 25
Insert coin: 5
Amount due: 20
Insert coin: 1
Error - this coin type not accepted
Amount due: 20
Insert coin: 25
Change Owed: 5
```

```plaintext
Amount due: 50
Insert coin: 25
Amount due: 25
Insert coin: 10
Amount due: 15
Insert coin: 10
Amount due: 5
Insert coin: 5
Change Owed: 0
```

## Question 3

Complete the following exercise in the [q3.py](./q3.py) file.

Write code that asks the user to input a single mathematical expression. What they type in should of a single digit number (0-9) followed by a math operator (+, -, \*, or /) followed by another single digit number. The user should type these three things on a single line (your code should only have one `input` statement). Your code should then evaluate the mathematical expression and print the result in the format specified below. Don't worry if your code crashes if the user types in an invalid expression (e.g. using two digit numbers, or alphabetic letters, or symbols other than +-/\*)

### Examples of Code Being Run

```plaintext
Enter expression: 6-2
6-2=4
```

```plaintext
Enter expression: 7*5
7*5=35
```

```plaintext
Enter expression: 5/3
5/3=1.6666666666666667
```

## Question 4

Complete the following exercise in the [q4.py](./q4.py) file.

Write a function called `scrabble_score` which takes one argument: a lowercase word. The function should return the number of points that word would earn on a scrabble board. Scrabble has the following scoring rules:

| Number of points | Letters                      |
| ---------------- | ---------------------------- |
| 1                | a, e, i, o, u, l, n, s, t, r |
| 2                | d, g                         |
| 3                | b, c, m, p                   |
| 4                | f, h, v, w, y                |
| 5                | k                            |
| 8                | j, x                         |
| 10               | q, z                         |

### Some examples

```python
print(scrabble_score("hello")) # 8
print(scrabble_score("world")) # 9
print(scrabble_score("zebra")) # 16
print(scrabble_score("xylophone")) # 24
```
