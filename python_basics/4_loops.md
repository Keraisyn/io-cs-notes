# Lesson 4: Loops

## Introduction
Consider the following. You want to make a program that prints out each number from 1 to 100. How would you do it?

Instead of writing 100 print statements, we can use *loops* to perform the same steps over and over again.

## Loops
There are two common types of loops that you will encounter.
- *While* loops or *conditional* loops continue repeating as long as a condition is true.
- *For* loops or *counting* loops repeat for a certain amount of times.

### A Racecar on a Track
You can think of loops as a racecar on a track. On every lap of the track, certain lines of code are executed. More on this later.

## While Loops
*While* loops are sometimes called *conditional* loops because they continue repeating code while a condition is true.

In the following example, the program will keep looping until the user inputs `stop`. Try running the program on your own computer.

```python
print("Type 'go' to greet and anything else to exit.")
user_input = input()

while user_input == "go":
    print("How are you today?")
```

While loops use the following template:

```python
while <condition>:
    <code to run>
```

Don't forget to indent your code! Indented code will be run on each pass (or *iteration*) of the loop while unindented code will not.

### Terminate Process
Consider the program:

```python
while True:
    print("I am a never-ending loop!")
```

This may look a little funny, but `True` is a condition which always evaluates to `True`. Therefore, this loop will never exit. 

If you find yourself with an endless loop like this one, use the keyboard shortcut `CTRL + C`. This will force quit any Python program.

## For Loops
A *for* loop, sometimes called a *counting* loop, goes through a sequence. This is also called *iterating* through a sequence. 

Let's use a for loop to count.

```python
for number in [1, 2, 3]:
    print("My number is", number)
```

Run the program. The output will look like this:

    My number is 1
    My number is 2
    My number is 3

What's going on? On each iteration (pass through) of the loop, the variable `number` is set to a number in `[1, 2, 3]`. To break it down, 
1. `number` is set to `1`.
2. The code in the loop runs and prints "My number is 1".
3. `number` is set to `2`.
4. The code in the loop runs and prints "My number is 2".
5. `number` is set to `3`.
6. The code in the loop runs and prints "My number is 3".

Let's try printing out the timestables for 7.

```python
for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(number, "x 7 =", number * 7)
```

Run the program. The output will look like this:

    0 x 7 = 0
    1 x 7 = 7
    2 x 7 = 14
    ...

The square brackets `[]` creates a list which we'll talk about in a future lesson.

### Range()
It's great that we can iterate through numbers that we type out, but what if we want to do something 1000 times? Revisiting our problem of print the number from 1 to 100, I don't want to type out all those numbers!

Luckily, there is a handy function called `range()` which will do most of the work for us. 

With one argument, we specify the end number for `range()`. Try running the program.

```python
for i in range(10):
    print(i)

# i is a common variable in for loops
# it is short for 'iteration'
```

The output will look like this:

    0
    1
    2
    ...
    8
    9

When we specify the end number, like in `range(10)`, it starts from 0 and goes all the way to that end number - 1. In this case, it was 10 - 1 = 9.

Why does it start from 0 and end at 9 rather than from 1 to 10? Well, it was a decision made by early programmers to be more efficient. Nowadays, we don't have the same limitations, but starting from 0 has stuck.

Now, we can easily write the program mentioned in the introduction: printing out the numbers from 1 to 100.

```python
print("Watch me count to 100!")

for i in range(100):
    print(i + 1)

# Why is the code print(i + 1) rather than print(i)?
# Because range starts with 0 so we need to add 1 to each number
```

#### Start and End Numbers
If we specify two arguments, `range()` will treat the first number as the starting point and the second as the ending point.

```python
for i in range(20, 50):
    print(i)
```

Output:

    20
    21
    22
    ...
    48
    49

#### Step
Finally, if we specify 3 arguments to `range()`, the first is the start number, the second is the end number, and the third is the step. The loop will go from the start to the end, jumping by the step every iteration.

```python
print("Here are the even numbers from 2-30")

for i in range(2, 31, 2):
    print(i)

# Notice the ending number must be 31 in order
# to print the numbers up to 30.
```

## Challenges
Todo