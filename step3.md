# Step 3

## Introduction

So far we have displayed a menu to the user and asked them to enter a selection.

Next we will add the code that checks which number they have entered.

For now, if the user enters "1", we will just print "You entered 1" on the screen and take no further action. Same for "2", "3", and "4".

Later on, we will make our application do something more useful when the user makes a choice.

## Objective(s)

- Create conditionals (if/elif) to check whether the user typed 1, 2, 3, or 4

## Background Information

### if / elif / else

In Python, the `if`, `elif` (short for "else if"), and `else` statements are used for conditional execution. They allow you to control the flow of your program based on certain conditions.

For example:

```
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

In this example, the program evaluates the conditions in order. If x is greater than 10, the first block is executed. If x is equal to 10, the second block is executed. If neither condition is true, the else block is executed.

## Steps

1. Edit your *zoo-manager.py* file.
2. At the end of your code, add an `if` statement to check if the user entered "1". If so, then print `You entered 1` on the screen.
3. Add an `elif` statement to check if the user entered "2". If so, then print `You entered 2` on the screen.
4. Add an `elif` statement to check if the user entered "3". If so, then print `You entered 3` on the screen.
5. Add an `elif` statement to check if the user entered "4". If so, then print `You entered 4` on the screen.
6. Save and run your program. If you enter 1, 2, 3, or 4, does it respond correctly?

## More Information

- [W3Schools: Python Conditions](https://www.w3schools.com/python/python_conditions.asp)

