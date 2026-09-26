# Day 1 — Strings Deep Dive (Data Engineering Track)

> Personal learning notes — Web Dev → Data Engineering transition

---

## Creation & Basics

```python
s1 = "double quotes"
s2 = 'single quotes'          # functionally identical
s3 = """triple quotes for
multi-line text"""
s4 = 'It\'s escaped'          # or use "It's" to avoid escaping
```

## Indexing & Slicing

```python
s = "Data Engineer"

s[0]        # 'D'
s[-1]       # 'r'  (last char)
s[5:14]     # 'Engineer'
s[:4]       # 'Data'
s[5:]       # 'Engineer'
s[::2]      # 'Dt niei'  (every 2nd char)
s[::-1]     # 'reenignE ataD'  (reversed)
```

## Immutability

```python
s = "hello"
s[0] = "H"        # ❌ TypeError — strings can't be modified in place
s = "H" + s[1:]   # ✅ this creates a NEW string, "Hello"
```

## f-strings (formatting)

```python
name = "Rakib"
score = 91.5
print(f"{name} scored {score:.1f}%")     # Rakib scored 91.5%
print(f"{name!r}")                        # 'Rakib' (repr form)
print(f"{score:>10.2f}")                  # right-aligned, width 10, 2 decimals
```

## Core Methods You'll Use Constantly

| Method | Does | Example |
| --- | --- | --- |
| `.strip()` | remove leading/trailing whitespace | `" hi ".strip()` → `"hi"` |
| `.lower()` / `.upper()` | case conversion | `"Hi".lower()` → `"hi"` |
| `.split(sep)` | string → list | `"a,b,c".split(",")` → `['a','b','c']` |
| `.join(iterable)` | list → string | `",".join(['a','b'])` → `"a,b"` |
| `.replace(a,b)` | substitute | `"hi".replace("h","H")` → `"Hi"` |
| `.startswith()` / `.endswith()` | prefix/suffix check | `"file.csv".endswith(".csv")` → `True` |
| `.find(sub)` | index or -1 | `"hello".find("l")` → `2` |
| `.count(sub)` | occurrences | `"banana".count("a")` → `3` |
| `.isdigit()` / `.isalpha()` | content check | `"123".isdigit()` → `True` |
| `.zfill(n)` | pad with zeros | `"7".zfill(3)` → `"007"` |

**DE-specific pattern — parsing a raw log/CSV line:**

```python
line = "2024-01-15, RAKIB , 450.75 "
date, name, amount = [field.strip() for field in line.split(",")]
amount = float(amount)
name = name.title()
# date='2024-01-15', name='Rakib', amount=450.75
```

---

## Code Practice — Strings

```python
# 1. Reverse a string WITHOUT slicing (use a loop)
def reverse_str(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_str("Rakib"))   # bikaR
```

```python
# 2. Check palindrome (ignore case & spaces)
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("Was it a car or a cat I saw"))  # True
```

```python
# 3. Count vowels
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print(count_vowels("Data Engineering"))  # 6
```

```python
# 4. Clean a messy CSV-style row (DE task)
raw = "  2024-02-01 , john doe , 1200.5000 "
parts = [p.strip() for p in raw.split(",")]
date, name, amount = parts
name = name.title()
amount = round(float(amount), 2)
print(date, name, amount)   # 2024-02-01 John Doe 1200.5
```

```python
# 5. Word frequency counter (very common DE/text-processing task)
def word_freq(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

print(word_freq("data data engineering is fun data is fun"))
# {'data': 3, 'engineering': 1, 'is': 2, 'fun': 2}
```

```python
# 6. Validate a simple email-like string
def is_valid_email(s):
    return "@" in s and "." in s.split("@")[-1] and s.count("@") == 1

print(is_valid_email("rakib@example.com"))  # True
print(is_valid_email("bad@@email"))          # False
```

### Try on your own (no solution given yet)

- Extract only the digits from a mixed string like `"Order#4521-XYZ"`.
- Given a sentence, return the longest word.
- Convert `"snake_case_name"` to `"camelCaseName"`.

---

## Notes / Log

- Date:
- Key gotcha today:
- Concept to revisit:
