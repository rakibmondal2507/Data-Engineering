# Day 1 — Python Fundamentals (Data Engineering Track)

> Personal learning notes — Web Dev → Data Engineering transition Background: JS/React/Express dev, learning Python for data engineering.

---

## Why This Matters for Data Engineering

Before the syntax, here's the "so what": in DE, Python is glue code around data movement — pulling from APIs/databases, transforming it, loading it into warehouses. Every fundamental below maps directly onto that pipeline work:

| Fundamental | Where it shows up in DE |
| --- | --- |
| Variables & types | Config values, connection strings, schema definitions |
| Strings | Parsing logs, cleaning raw text fields, building SQL queries, file paths |
| Lists | Rows of data, batches of records pulled from an API |
| Tuples | Immutable records (e.g. a single row from a DB cursor — `cursor.fetchone()` returns a tuple) |
| Sets | De-duplication, comparing schema columns between two sources |
| Dictionaries | The shape of almost everything — JSON API responses, a single row as `{column: value}`, config/env settings |

This is different from web dev, where you're mostly manipulating UI state. In DE you're almost always manipulating **collections of records** — so lists-of-dicts and dicts-of-lists become your bread and butter (this *is* what a DataFrame is, under the hood, before you ever touch pandas).

---

## 1. Install Python

```bash
python3 --version
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**DE-specific note:** you'll juggle more dependency conflicts in data work than in web dev (pandas, pyarrow, database drivers, cloud SDKs all pin different versions). Get disciplined about virtual environments now:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 2. VS Code Setup

1. **Python** extension (Microsoft) + **Pylance**.
2. `Ctrl+Shift+P` → "Python: Select Interpreter" → your venv.
3. Also worth adding early, since you'll use it constantly in DE: **Jupyter** extension — lets you run `.ipynb` notebooks inside VS Code, which is how most data exploration/prototyping happens before code gets moved into production pipeline scripts.

---

## 3. Variables

```python
name = "Rakib"
age = 25
```

- `snake_case`, dynamically typed, no declaration keyword.
- **DE habit to build now:** get comfortable with type hints early — pipeline code lives longer and gets touched by more people than a typical frontend component, so clarity matters more:

```python
def load_records(source: str, batch_size: int = 100) -> list[dict]:
    ...
```

---

## 4. Data Types

| Type | Example | Notes |
| --- | --- | --- |
| `int` | `42` |  |
| `float` | `3.14` | Watch for precision issues with financial/large data — you'll later meet `Decimal` for this |
| `str` | `"hello"` |  |
| `bool` | `True` |  |
| `NoneType` | `None` | **Very common in DE** — represents NULL/missing values coming from databases or APIs |

Python won't coerce types silently — this strictness is actually a feature in DE, where a silent `"5" + 3` bug in a pipeline could corrupt a whole dataset before anyone notices.

---

## 5. Strings

```python
s = "Hello, Rakib"
s[0:3]        # slicing
s[::-1]       # reverse
f"Hello, {name}!"
```

**DE relevance:** string handling is a huge part of the job — parsing CSV lines, cleaning inconsistent text fields ("NY" vs "New York" vs "new york"), building dynamic SQL, working with file paths and timestamps. Methods you'll lean on constantly:

```python
"  messy data \n".strip()
"2024-01-15".split("-")
",".join(["a", "b", "c"])
"raw_log_line".lower().replace("_", " ")
```

---

## 6. Lists

```python
nums = [1, 2, 3, 4]
nums.append(5)
squares = [x**2 for x in range(5)]
```

**DE relevance:** a batch of rows pulled from a database or API is almost always a list (of dicts or tuples). List comprehensions are your main tool for lightweight transformations before you graduate to pandas/PySpark:

```python
raw_rows = [{"id": 1, "amount": 100}, {"id": 2, "amount": -5}]
valid_rows = [r for r in raw_rows if r["amount"] > 0]   # basic data validation
```

---

## 7. Tuples

```python
point = (3, 4)
x, y = point
```

**DE relevance:** database cursors return rows as tuples by default:

```python
cursor.execute("SELECT id, name FROM users")
row = cursor.fetchone()   # (1, 'Rakib')
```

Immutability here isn't just a language quirk — it reflects that a fetched row *shouldn't* be mutated in place; you transform it into something new instead.

---

## 8. Sets

```python
a = {1, 2, 3}
b = {2, 3, 4}
a & b     # intersection
a - b     # difference
```

**DE relevance:** two very common real tasks —

- **De-duplication:** `unique_ids = set(all_ids)`
- **Schema comparison:** compare column names between a source table and a target table: `set(source_cols) - set(target_cols)` instantly tells you what's missing.

---

## 9. Dictionaries

```python
person = {"name": "Rakib", "age": 25}
person.get("email", "not found")
```

**DE relevance:** this is the shape of almost everything you'll touch —

- A single API response record
- A single row read as `{column_name: value}`
- Config/env settings (`{"host": ..., "port": ..., "db": ...}`)

A "list of dicts" is the plain-Python shape of a table, and it's exactly what `pandas.DataFrame(list_of_dicts)` consumes directly — so getting fluent with this pattern now pays off immediately once you start pandas.

---

## Quick Reference: Mutable vs Immutable

| Immutable | Mutable |
| --- | --- |
| `int`, `float`, `str`, `bool`, `tuple` | `list`, `dict`, `set` |

---

## 20 Practice Problems

**Variables & Types**

1. Swap two variables without a third.
2. Take a string input; print its type, length, and whether it's numeric.
3. Convert Celsius (float) to Fahrenheit, 2 decimal places.

**Strings** 4. Reverse a string with a loop (no slicing). 5. Check if a string is a palindrome (ignore case/spaces). 6. Count vowels in a string. 7. Split a full name string into first/last name. 8. Capitalize every word in a sentence manually (no `.title()`).

**Lists** 9. Find largest/smallest in a list without `max()`/`min()`. 10. Remove duplicates from a list, preserving order. 11. List comprehension: numbers 1–50 divisible by both 3 and 5. 12. Flatten a nested list: `[[1,2],[3,4],[5]]` → `[1,2,3,4,5]`. 13. Find the second-largest number in a list.

**Tuples** 14. Given a list of `(name, score)` tuples, find the highest score. 15. Return min/max of three numbers as a tuple.

**Sets** 16. Find common elements between two lists using sets. 17. Check if one set is a subset of another — verify with `issubset()` and manually with a loop.

**Dictionaries** 18. Count character frequency in a string using a dict. 19. Given `{name: score}`, find the student with the highest score. 20. Merge two dicts; on key collision, keep the second dict's value.

**Bonus — DE-flavored (try after the above)** 21. Given a list of dicts representing rows (some with a `None` value for `"amount"`), filter out the invalid rows and compute the sum of `"amount"` for the rest. 22. Given two lists of column names (`source_cols`, `target_cols`), print which columns exist in source but not target, and vice versa.

---

## Notes / Log

*(Use this section to jot your own takeaways, gotchas, or links as you go — keeps this file useful as a running log instead of just a reference.)*

- Date started:
- Key gotcha today:
- Concept to revisit:

---

**Workflow:** Solve each problem in a `.py` file, run it, then commit this notes file alongside your solutions to a `python-de-learning` repo on GitHub — one commit per day keeps a visible progress trail.
