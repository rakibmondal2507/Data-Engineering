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
- **Use Case** - **Clean Numeric format**
- swaps part of text with something new
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
