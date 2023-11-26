# Functions in Python Programming

A function is a block of code that performs a specific task.

Dividing a complex problem into smaller chunks to make our program easy to understand and reuse.


## Types of functions:

1. Builtin Functions:

These are the functions which are already built-in functions in the python program that are available to use.


2. User-defined Functions:

We can create our own functions based on our requirements.


## User Defined Functions:


Syntax:

def function_name(arguments):
    # code

    return

function_name(arguments) # function call


1. Whenever we call the function, it goes to the function definition.
2. All the lines of code present inside the functions are executed.
3. Comes back to the function call itself.


## Types of User-Defined Functions based on arguments and return value.

1. Without arguments and without return value
2. With arguments and no return value
3. without arguments and with return value
4. with arguments and with return value

### Programs for the Types of User-Defined Functions based on arguments and return value.

1. Without arguments and without return value

```python

# Without arguments and without return value

def greet():
    print("Welcome to python programming!")

greet() # Output: Welcome to python programming!

```

2. With arguments and no return value

```python

# With arguments and without return value

def sub(a, b):
    c = a-b
    print("The sub of the numbers is", c)

x = 10
y = 20
sub(x, y) # Output: The sub of the numbers is -10
sub(10, 15) # Output: The sub of the numbers is -5
sub(y, x) # Output: The sub of the numbers is 10

```

3. Without arguments and with return

```python

# Without arguments and with return value

def sum():

    a = 20
    b = 30
    return a+b

c = sum()
print(c)# Output: 50
```

4. With Arguments and with return value

```python

# Without arguments and with return value

def sum(a, b):
    c = a+b
    return c

z = sum(10, 20)
print(z)# Output: 30

x = -10
y = 20
z = sum(x, y)
print(z)# Output: 10

z = sum(y,x)
print(z) # Output: 10
```

## Function argument with default values

```python

def sum(a=0, b=0):
    print(a+b)
 
sum() # Output: 0
sum(10) # Output: 10
sum(10, 20) # Output: 30
```

## Keyword Argument

```python
def sub(a=0, b=0):
    print(a-b)
 
x = 10
y = 20

sub(x, y) # -10
sub(y, x) # 10
sub(b=y, a=x) # - 10
```


## Scope of the variable:

1. Local Scope:

When we declare a variable inside the function, these variables are will have a local scope (within the function). We cannot access them outside the function.


2. Global Scope:

a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.


![Image of Local and Global Variables]("Screenshot%202023-11-24%20112019.png")

---

Ever Imagined how various functions would work if they don't know how many arguments it is going to get in advance like print function in python. 

print(1)
print(2,3,4)
print(3,4,5,6)
print()

In these cases we use something known as **arbitary arguments**


## Arbitary Arguments

We do not know the number of argument that will be
passed into a function in advance then we will use
the arbitary arguments.

```python

def find_sum(*numbers):
    print(numbers)
    print(type(numbers))
    print(sum(numbers))

find_sum(10,20,30,40)
find_sum(10)
find_sum(1,2)

```

## Keyword Arbitary Argument

```python

def personInformation(**info):
    print(info)
    print(type(info))


personInformation(name="Tharani", role="Mentor")

```
