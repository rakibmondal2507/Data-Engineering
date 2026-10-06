## Types
 
 **type(**value**)** built in function, output: type
- returns the data type of value, so you know what kind of object it is.
```python
  age = 23
  print(type(age))
```
**str()**
  str() function in Python is a built-in function used to convert a specified value or object into its string representation. 

## Math

**len** 
- returns the number of item in a value returns the number of characters in a string
- len() counts everything even **spaces**
- **Use Cases** - Validate input Length
  Prevent values that are too short or too long.
  ```python
  password = "34827fdk3"
  print(len(password))
  ```

**count**(substring)
- **Use Case** - Word Frequency check
  Counts how many times a specific word appear
  - returns how often a word appear in a string
  - python is **case-sensitive**,
    means uppercase and lowercase letters are treated as different.
  **Use Case** - **Detect Quality issues** -  count how many unwanted character in my data.
```python
 #count
 text = """
 Python is easy to learn.
 Python is powerful.
 Many people love python.
 """
 
 print(text.count("Python"))
 print(text.count("python"))
```
## Data Transformation

**replace()**
- swaps part of text with something new
- **Use Case** - **Clean Numeric format**
```python
# replace()

price = "1342,432"
print(price.replace("," , "."))
```
- **Use Case** - **Change phone number format** - replace special character with something else.
```python
phone = "213-3248-423"
print(phone.replace("-" , "/"))
```
- **replace()** is not just for changing values , you can also **remove unwanted parts** by replacing them with an **empty string("")**
```python
phone = "213-3248-423"
print(phone.replace("-" , ""))
```
- **Use Case** - **Clean Numeric format**
```python
price = "$4,283.99"
print(price.replace("$" , "").replace("," , ""))
```
- **Chained methods** are executed in order from **left to right.** Each replace() runs on the results of the one before it.

**Join String** -> **+** plus operator
'string'+'string' -> **joins(concatinates) two string into one.**
```python
# Join Strings
fname = "Rakib"
lname = "Mondal"
lname = fname +" "+lname
print(lname)
```
- **Use Case** - **Build file path** - build dynamic paths using folder and file variable
  ```python
  folder = "C:Users/Rakib/"
  file = "report.csv"
  full_path = folder + file
  print(full_path)
  ```

**f-String**
- modern , super easy way to format and build strings
- "f" stands for "formatted"
- lets you easily put variables and expressions directly inside string value
```python
  #f-string
  name = "Rakib"
  age = 23
  is_student = True
  print(f"My name is {name}, I am {age} years old and my student status is {is_student}")
  print(f"2 + 3 = {2+3}") #expression also work
  print(f"{{This is me}}")
```


**Split**
- Breaks a string into smaller part.
```python
stamp = "2026-05-13 21:40" 
print(stamp.split(" "))
```
- Break **comma-separated** values into individual items
```python
csv_file = "1343,Rakib,India,24-12-2010"
print(csv_file.split(","))
```

**Indexes & Slicing**
- If you leave start index empty Python start from index 0
- use negative indexs if you want to extract part from the right side (end) of the string)

=========================
## String Cleaning
=========================
### clean whitespaces
