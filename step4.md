# Step 4

## Introduction

So far we have displayed a menu to the user, asks them to enter their selection and then tells the user what they entered. The application then ends.

Ideally, we would like it so that the user is returned back to the menu afterwards.

To do this, we can put all of our code into an infinite loop. That way, when the end of your code is reached, it goes back to the start.

## Objective(s)

- Create an infinite loop using a while statement

## Background Information

### while

In Python, the `while` loop is used to repeatedly perform a task (or tasks) as long as a certain condition is true.

Commonly, the condition is set to **1**, for example: `while 1`. These loops continue indefinitely until manually interrupted or until a `break` statement is encountered within the loop.

For example:

```
while 1:
    user_input = input("Enter your name: ")
    
    if user_input == 'Kim':
        break

    print("Now we go back to the start.")
```

In this example, the `while` loop will keep run until it is stopped. The user can stop the loop by entering 'Kim', which triggers the `break` statement (which exits the loop).

**Visual demonstration:**

![](images/while-1.gif)

## Steps

1. Edit your zoo-manager.py file.
2. Create an infinite loop using a `while 1:` statement at the top of your code.
3. Indent all other lines of your code (1 level) to add them to the loop.
4. Save and run your program. Does it work correctly? Does it return to the menu after making a selection?

## More Information

- [W3Schools: Python print() Function](https://www.w3schools.com/python/ref_func_print.asp)

