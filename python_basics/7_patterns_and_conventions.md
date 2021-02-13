# Lesson 7: Patterns and Conventions

A common saying among programmers is that *readability* is what separates the good coders from the great coders. The hardest part of coding is reading and understanding someone else's code since we can't tell what the author was thinking while coding. Usually, the code you'd write for big projects would need to be read and re-read hundreds of times. 

## Importing Modules

Python (and most other coding languages) let us combine code files. This is done using a method called *importing*.

As an example, let's say we have two files: `a.py` and `b.py`.

```python
# This is a.py

x = 10
def say_hi():
    print('hi')

y = 29282
my_name = 'Thomas the Tank Engine'
```

You can *import* `a.py` into `b.py` using and `import` statement.
```python
# this is b.py

import a    # This pastes all of the code in a.py into this file.
            # Now we can use all of the variables and functions we defined in a.py!

# To access something we've defined in the imported file,
# we just add the filename and a dot before the thing we want to get.
# In this case, we add "a." before the variables and functions in a.py

# The "a." is called a prefix. They exist to avoid naming conflicts.

print(a.x)
print(a.y)
print(a.my_name)
a.say_hi()

>>> python3 b.py
10
29282
Thomas the Tank Engine
hi
```

Whenever you `import` a file into another file, the file that gets copied is called a *module*.

If you want to `import` specific things from a module without a prefix, use `from X import Y` where X is the module name and Y are the things.

For example, using `a.py`,
```python
# This is c.py

from a import say_hi, my_name  # Only imports say_hi() and my_name

print(my_name)
say_hi()
# Notice that we don't use the "a." prefix!

>>> python3 c.py
Thomas the Tank Engine
hi
```

If you just want to import everything from a file, you can use `*`, the wildcard symbol.

Usually, `*` (the asterisk) is called the wildcard and just means "anything and everything". In the case of `import`ing, the wild card means "every variable/function/class" (We'll talk about classes soon).

```python
# This is d.py
from a import *

print(x)
print(y)
print(my_name)
say_hi()
# Notice that we don't use the "a." prefix!

>>> python3 d.py
10
29282
Thomas the Tank Engine
hi
```

Remember when I said that `import` copies+pastes code from the module into the current file? This means that you can also import working code.

```python
# This is file1.py

x = 'Spam and Eggs!'

print('I contain spam and eggs!!')
for i in range(5):
    print('spam')
    print('eggs')
```

Now let's import file1.py into file2.py

```python
# This is file2.py

import file1
print(file1.x)
```
```
>>> python3 file2.py
I contain spam and eggs!!
spam
eggs
spam
eggs
spam
eggs
spam
eggs
spam
eggs
Spam and Eggs!
```

Usually, modules only contain variables/functions/classes.

However, if you want to have code that doesn't run when a module is imported, you can use a special trick.

```python
# This is file3.py

def say_hi(name):
    print('hi ' + name + '!')

if __name__ == '__main__':
    # Test say_hi()
    if say_hi('Sportacus') == 'hi Sportacus!':
        print('say_hi() works :)')
    else:
        print('say_hi() does not work :(')

# When we run file3.py, the code in the "if __name__ == '__main__':" runs. 
>>> python3 file3.py
say_hi() works :)
```

If we import file3.py into, say, file4.py, the code that tests say_hi() won't execute.

```python
# This is file4.py

import file3
file3.say_hi('Trevor')

# Notice that the file doesn't print "say_hi() works :)"
>>> python3 file4
hi Trevor!
```

### Python Libraries

Python has a bunch of built-in code files full of functions that we can use! They're called libraries and we can `import` them just like any regular old module.

```python
import math
print(math.sqrt(4)) # We can use the built-in square root function.

>>> python3 program.py
2.0
```

## String Quotes

You might have noticed that the quotation marks can be either apostrophes `'` or actual quotation marks `"`. There's no required standard in Python, so you should choose one style and stick with it.

```python
x = "This is a valid string"
y = 'This is also a valid string'
```

## Variable Naming Conventions

There are three popular conventions for naming variables: snake_case, PascalCase, and camelCase.

- `snake_case` puts *underscores* `_` between the words in a name.
- `PascalCase` capitalizes the first letter of each word in a name.
- `camelCase` is like `PascalCase` but the first letter isn't capitalized.

Python uses a combination of snake_case and PascalCase.

```python
# Variables and functions should be in snake_case.
my_var1 = 1
my_var2 = 'hehe'
my_variables = [my_var1, my_var2]

# Class namese should be in PascalCase (We'll talk about classes in the next note).
class MyCustomClass:
    # class stuff...
    # Don't worry about what goes here for now.
```
