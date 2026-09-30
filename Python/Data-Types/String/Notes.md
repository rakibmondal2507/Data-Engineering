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
  print(len(password)"
  ```

**count**(substring)
- **Use Case** - Word Frequency check
  Counts how many times a specific word appear
  - returns how often a word appear in a string
  - python is **case-sensitive**,
    means uppercase and lowercase letters are treated as different.
  **Use Case** - **Detect Quality issues** -  count how many unwanted character in my data.
