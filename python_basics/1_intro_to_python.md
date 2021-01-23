# Lesson 1: Introduction to Python

## Introduction
Programming is giving instructions to computers.

Let's try giving instructions through the console.

```python
>>> print("Hello World!")
```

Now, press the enter key. You should see:

    Hello World!

The console is *executing* our commands. The computer is under our control! What other commands can we try? Note: >>> means we are typing a command.

```python
>>> print(28 + 99)
127
>>> print(2 * 9)
18
>>> print("cat" * 20)
catcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcatcat
>>> print(2350923840840 * 230459720)
541793250101310964800
```

## Math in Python
Math is really important in programming. We can use certain *operations* to manipulate numbers.

| Operation         | Operator  |
| ---               | :---:     |
| Addition          | +         |
| Subtraction       | -         |
| Multiplication    | *         |
| Division          | /         |
| Exponents         | **        |
| Modulo/Remainder  | %         |

```python
>>> print(2 ** 3)
8
>>> print(9 / 2)
2.25
```

Remember that math in Python follows the order of operations.

```python
>>> print( 6 / 2 * (1 + 2) )
9.0
```

## Print Statements
You've probably noticed something in the previous code examples. The word `print` with brackets surrounding expressions.

This is called a *built-in function*. The print function takes whatever's inside the brackets and displays it on the screen.

We can put multiple *arguments* into one print statement by separating them by commas.

```python
>>> print("8 / 2 is", 8 / 2)
8 / 2 is 4.0
```

The print function will automatically separate arguments by spaces and add a newline.

## Integers and Strings
In the previous examples, we worked with numbers and text.  
In programming, whole numbers are called *integers*.  
Text is called *strings*.  
Integers and strings are both called *datatypes* or simply, *types*. There are many more types which we'll cover in the future.

Integers are specified with just the number and no decimal points. `0`, `-4`, `2346234723722346` are examples of integers.

Strings are specified with quotation marks around text. `"Hello World!"`, `"e"`, `";l,;ml--"` are examples of strings.

Beware! Even though `7` and `"7"` both look like whole numbers, they are different! `7` is an integer while `"7"` is a string. Can you tell why?

There's another type that you'll see often. *Floats* are decimal numbers. `2.15`, `-02`, `5.0` are examples of floats.

<details>
<summary>Answer</summary>

`"7"` has quotation marks around it.

</details>

## Python Files
We've only been executing single commands in the console. Now, we want to create programs with multiple lines. 

Create a new file in your editor of choice. In VSCode, the command is CTRL + N. Name it and add `.py` to the end. 

    my_first_program.py

Python reads code line-by-line and executing each instruction. That means code on line 1 is run before code on line 2.

```python
print("Hi there!")
print("My name is Matthews.")
print("Check out my calculations!")
print(28903 * 920)
```

## Exercises
### Seconds/Year
Using the Python console, figure out how many minutes are in a year.

<details>
<summary>Hint 1</summary>

There are 60 minutes in an hour, 24 hours in a day, 365 days in a year. Multiply the numbers together.

</details>

<details>
<summary>Answer</summary>

```python
>>> 60 * 24 * 36
```

</details>

### All About You
On separate lines, print out an introduction about you including: age, your favourite food, and the city you live in.

    Hi, I'm Matthews.
    I am 124 years old.
    My favourite food is salmon.
    I live in Sydney, Australia.

<details>
<summary>Hint 1</summary>

Put your messages inbetween print statements.

```python
print("Hi, I'm Matthews.")
print("I am 124 years old.")
etc.
```

</details>