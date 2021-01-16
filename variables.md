# Lesson 2: Variables

## Introduction
In the previous lesson, we created programs that ran the same every time. For the last program, it would always print my information (age, favourite food, etc.). The information was *hard-coded*. To change the *output* of the program, that is, what the computer prints out, we must change the print statements themselves. What if the program could ask the user for their *input*, that is, the information that the user gives to the program?

## Input, Output
*Input* is what a user *gives* to a program. *Output* is what the program *returns* to the user. A typical cycle for a program is input, processing, output. For example:

    Enter your name: Matthews
    Hello, Matthews

The input is my name, the processing is storing the input, and the output is "Hello, Matthews".

### Exercise
Determine possible input, processing, and output for Mario jumping.

<details>
<summary>Solution</summary>

Input - The player pressing the "A"/Jump button.  
Processing - Calculate where Mario's position and speed.  
Output - Show Mario's character moving up, then down.

</details>

## Variables
One of the most useful tools in programming is the variable. They allow us to store data, be it numbers, words, and more.

A variable is something that varies, that means to change. There are multiple ways to think about variables, but there are two that I like to use. 

### Variables as Nametags
Variables can be thought of as nametags. Let's take a nametag and write "doctor" on it. Then, we stick it to Dr. Smith. When we call out "doctor", Dr. Smith will respond.

```python
doctor = "Dr. Smith"
print(doctor)

Output:
Dr. Smith
```

Now, we take a nametag and write "my_number" on it. Then, we stick it to the number 6. When we call out "my_number", we'll get the number 6.

```python
my_number = 6
print(my_number)

Output:
6
```

By making `my_number` equal to something else, we change the value. This is like taking the nametag off `6` and sticking it onto `7`.

```python
my_number = 7
print(my_number)

Output:
7
```

You can assign a variable 

### Variables as Signs
Variables can also be thought of as signs pointing to objects. A sign that says "doctor" points to Dr. Smith. A sign that says "my_number" points to 6. When I set my_number to 7, the sign stops pointing to 6, and points to 7.

### Variable Syntax
The equal sign works a little differently than in math. In math, the equal sign tells us that both sides are equal, a comparison. However, in programming, the equal sign means we are making the left side equal to the right side.

```python
fav_colour = "Blue"
print(fav_colour)

Output:
Blue
```

The variable (nametag) is on the left side and the value we make it is on the right. In plain English, `fav_colour = "Blue"` might be said as "the variable `fav_colour` is now made equal to `"Blue"`."

Notice how we reference variables in Python. Why didn't the program output `fav_colour`? That's because there are no quotation marks around it.  
When we use quotation marks, that tells Python to take it literally. Print out what's in between the quotation marks.  
When we don't use quotation marks, that tells Python it's a variable. Python finds the real value and replaces the variable with it. The next example shows what's going on under the hood.

```python
fav_colour = "Blue"
print(fav_colour)

BECOMES...

fav_colour = "Blue"
print("Blue")
```

### Age Variable
Set a variable named `my_age` to your age. Print out what your age is. Then, try changing the value of `my_age`.

    My age is 9

    My age is 48

<details>
<summary>Hint 1</summary>

To make a variable, put the variable name on the left and the value on the right with an equal sign inbetween.

In the print statement, put `my_age` instead of the number. Don't forget to separate the string and variable with a comma!

</details>

<details>
<summary>Answer</summary>

```python
my_age = 21
print("My age is", my_age)
```

</details>

## Variable Examples
Let's check out some examples of manipulating variables.

You can put variables on the right side as well.
```python
a = 23
b = 2
c = a + b   # The value of c is 25

Calculated as...

c = 23 + 2
```

Multiple variables can have the same value. Just like how one person can have multiple nametags, or multiple signs can point at one person.

```python
doctor = "Dr. Smith"
father = "Dr. Smith"

# doctor and father both have the value "Dr. Smith"
```

## Getting User Input
By getting input directly from the using, we are able to change the input every time we run the program. There's a handy function built in to Python. It's called `input()`. This function will prompt the user for an input and save it as a string.  
The argument inside the brackets is a string that will prompt the user. Remember to add a space to the end or else the user's input will stick right next to the prompt!

```python
user_name = input("Type in your name: ")
```

Try it! Whatever the user types in, it will replace the entire `input()` function. In the next example, I'll type in "Matthews" as the input.

```python
user_name = input("Type in your name: ")

BECOMES...

user_name = "Matthews"
```

## Converting Between Types
One final thing. Since `input()` always gives a string, we have to convert it to an integer if needed.  
We can use the function `int()` to convert strings to integers and `str()` to convert integers to strings.

```python
a = int("9")
b = str(3)
```

`a` is now the integer 9.  
`b` is now the string "3".
