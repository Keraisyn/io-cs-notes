# Lesson 5: Lists

## Introduction
Usually, we store a value in a *variable*. We can read this value or change it throughout the program. So far, the variables we've looked at are all single pieces of data (eg. a number, a string, a float, etc.).

What do we do if we need to store a collection of values? For example:
- A list of temperatures over the past year.
- A list of names in the attendance system.
- A sequence of frames in an animation.
- And others...

## Lists
In Python, we can use *lists* to store a collection of values. (Lists can also be called *Arrays* or *Sequences*)

To create a list:
```python
my_list = [1, 2, 3, 4] # A list with the numbers from 1 to 4
```
This list stores a *collection* of numbers! There are lots of applications: like storing the high scores in a leaderboard, among others.
```python
word_list = ["cow", "broom", "computer", "sunny"] # Lists can store anything
list_of_lists = [[1, 1], [1, 1]] # Even other lists! 
empty_list = [] # We can make empty lists too
```

### Indices
(Indices is the plural of index)

Every item in a list has an *index*. Indices describe the position of an item in a list.

![Will show up when moved out of wip/](./assets/5_lists_array_indices.png)

**NOTE:** Programmers always start counting at zero!
- The **zero***th* item is 20
- The *first* item is 33
- The *second* item is 12
- And so on...

## List Operations

0. Access

    We can get the value at some index in a list using *square brackets* `[]`.
    ```python
    my_array = [2021, 100, 1337, 9001]
    print(my_array[2])

    >>> python3 program.py
    1337
    ```

1. Slicing

2. Append, remove

3. Sorting



## Lists and Loops

## 2D Lists

## List Properties
0. The items in a list always keep the order that they were added in.
    ```python
    x = [4, 12]
    x.append(7)
    x.append(8)

    # 4 will always be the zeroth item
    # 12 will always be the first item
    # 7 will always be the second item
    # 8 will always be the third item
    ```
1. Lists can change size
2. The value at an index in an array can be changed (eg. `x[2] = 3`)
3. Lists can contain any types of values (integers, strings, floats)
4. Lists can be put in lists.

## Challenges