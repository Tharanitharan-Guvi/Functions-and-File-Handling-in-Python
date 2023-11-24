# File Handling in Python

A file is a place where is store data

In python programming, a file operation takes place in this following order:

1. Open a file.
2. Perform some operation (Read / Write)
3. Close the file.


## Syntax for opening a file:

```python
fileObj = open("filename.extension", "mode")
```

### Modes

1. Read (r) -> Read Only
2. Write (w)
3. Append (a)


### How to read a file

Sample.txt

```
This is the First line.
This is the Second line.
This is the Third line.
```


read() --> It is used to read the entire content of the file.

```python

file = open("sample.txt", "r")

print(file.read())

file.close()

```


readline() --> It reads from the cursor till the new line character (\n).

```python

file = open("sample.txt", "r")

print(file.readline())
print(file.readline())
print(file.readline())

file.close()

```

readlines() --> it reads the entire content of the file and gives a list as an output.

```python
file = open("sample.txt", "r")

print(file.readlines())

file.close()
```


### How to write a file

1. Write Mode:

    - If we try to open a file that doesn't exist, a new file will be created.

    - if a file already exists, its content is erased, and new content will be added to the file.