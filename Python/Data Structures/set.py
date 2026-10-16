#+++++++++++++ 1. Create a set ++++++++++++#

ids = {101, 102, 103, 103}
# print(ids)
cities = {"pune", "delhi", "kolkata", "Pune"} #case sensitive
# print(cities)

empty = set()    # NOT {}, because that makes an empty dictionary



#+++++++++++++ 2. Duplicates are removed automatically +++++++++++++#

nums = {1, 2, 2, 3, 3, 3}
print(nums)

# Remove duplicates from a list
cities = ["pune", "delhi", "pune", "kolkata", "delhi"]
unique = list(set(cities))
print(unique)

## Sets have no order and no indexing, so my_set[0] gives an error.


#++++++++++++++ 3. Add and remove ++++++++++++++#

s = {"a", "b"}
s.add("c") # add one 
print(s)
s.update(["d", "e"]) # add many
print(s)

s.remove("a")  #give error if value not present
# s.remove("z")
print(s)

s.discard("z")  # no error if value not present
print(s)

x = s.pop()  # removes a random item
print(s)
print(x)

#++++++++++++ 4. Fast membership check ++++++++++++#

valid_ids = {101, 102, 103}
print(102 in valid_ids  )
print(999 in valid_ids)

## For big data, in on a set is much faster than in on a list

#+++++++++++++++++ 5. Set operations (very useful)++++++++++++++++++#

yesterday = {"amit", "sara", "john"}
today = {"sara", "john", "riya"}

print(yesterday | today) #Union
print(yesterday & today) #common
print(yesterday - today) # only yesterday not common given
print(today-yesterday) # only today not common is given
print(today^yesterday) #only not common is given from both


#+++++++++++++++++++++ 6. Set comprehension ++++++++++++++++++++#

raw = [" Pune", "pune ", "DELHI", "delhi"]
clean = {c.strip().lower() for c in raw}
print(clean)

#================================================#
         # 7. Data engineering examples
#================================================#

# 1. Find new users compared to yesterday:
yesterday = {1, 2, 3, 4}
today = {3, 4, 5, 6}

added = today - yesterday
print(added)

removed = yesterday - today
print(removed)

# 2. Check for missing columns:
required = {"id", "name", "age"}
actual = {"id", "name", "city"}

missing = required - actual
print(missing)
extra = actual - required
print(extra)

# 3. Find duplicate values in a list:
ids = [1, 2, 3, 2, 4, 1]
seen = set()
dupes = set()

for i in ids:
    if i in seen:
        dupes.add(i)
    seen.add(i)
    
print(dupes)


#=================================================#
                      # Practice
#=================================================#

# 1. Remove duplicates from [5, 3, 5, 1, 3, 9].

raw_list = [5, 3, 5, 1, 3, 9]
remove_dup = set(raw_list)
new_list = list(remove_dup)
print(new_list)
# or 
unique_list = list(set(raw_list))
print(unique_list)
# or 
# If you need to keep the original order
unique_ordered = list(dict.fromkeys(raw_list))
print(unique_ordered)   # [5, 3, 1, 9]


# 2. Given a = {1, 2, 3, 4} and b = {3, 4, 5}, find the items in both, and the items only in a.
a = {1, 2, 3, 4}
b = {3, 4, 5}
both = a&b
print(both)
only_a = a-b
print(only_a)

# 3. Given required columns {"id", "email", "age"} and file columns ["id", "name", "age"], find which required columns are missing.

required = {"id", "email", "age"}
file = ["id", "name", "age"]

# actual = set(file)
# missing = required - actual
missing = required - set(file)

print(missing)
