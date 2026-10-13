######### 1. CREATE LIST ##########

columns = ["id", "name", "age", "city"]
# print(columns)
ids = [101, 102, 103]
# print(ids)
mixed = [1, "Rakib", 25.5, True]   # can mix types
empty = []
# print(empty)


######### 2. Access items (indexing) ##########
## Counting starts at 0. Negative numbers count from the end.

columns = ["id", "name", "age", "city"]
print(columns[0])
print(columns[2])
print(columns[-1])
print(columns[-3])



########## 3. Slicing (take a part) ###########
## Format: list[start:stop]. The stop index is not included.
name = ["Rakib", "Payel", "Pandit", "Rupam", "Pravat"]
print(name[1:3])
print(name[:2])
print(name[3:])
print(name[1:4:2]) # every 2nd item
print(name[::2]) # every 2nd item
print(name[::-1]) #Revese the list 



########## 4. Add, remove, change ##########
files = ["name.csv", "city.csv"]
# Add
files.append("country.csv")

files.insert(1,"role.csv",)
print(files) # Insert use in position for add value

files.extend(["hello.csv", "world.csv"])
print(files) # extend([]) use for add many values on files


# remove
files.remove("country.csv") # remove by values
# print(files)
last = files.pop() #pop() removes last and returned also that remove values
print(files)
print(last)

files.pop(2) # remove by index
# print(files)


#Change
files[0] = "department.csv"
# print(files)


############# 5. Useful built-in tools ######

nums = [5, 2, 9, 1]
print(len(nums)) # length --> 4
print(sum(nums)) # addtion of all values
print(min(nums)) # give minimum/smallest number on output
print(max(nums)) # give maximum/largest number on output
print(sorted(nums)) # return new sorted list
nums.sort() # sorts existing list
nums.reverse() # revese same/existing list
# print(nums) 

# check is value exist on list (membership check)
print(9 in nums)
print(3 in nums)

print(nums.count(2)) # check how time values appears on list

print(nums)
print(nums.index(9)) # give indexs of value
# print(nums.index(3)) if value does exist give error



########### 6. Loop through a list ############
files = ["jan.csv", "feb.csv", "mar.csv"]

for f in files:
    print("Processing", f)
    
# With index
for i, f in enumerate(files):
    print(i, f)
    
    
    
########### 7. List comprehension (very important) #############

## A short way to build a new list from an old one. Format: [expression for item_name in list_name if condition]

nums = [1, 2, 3, 4, 5]
squares = [n*n for n in nums]
print(squares)
evens = [n for n in nums if n%2==0]
print(evens)

# Data engineering style: clean column names
raw = [" ID ", "Name ", " AGE"]
clean = [c.strip().lower() for c in raw]
print(clean)




#================= 8. List of lists and list of dicts ================#
## This is how real data looks.

# Rows as lists
rows = [
    [1, "Amit", 25],
    [2, "Sara", 30],
]
print(rows[1][1])


# Rows as dictionaries (very common with JSON / APIs)
records = [
    {"id": 1, "name": "Amit", "age": 25},
    {"id": 2, "name": "Sara", "age": 30},
]

# Get all names
names = [r["name"] for r in records] 
print(names)

# Filter records
adults_30 = [r for r in records if r["age"] >= 30]
print(adults_30)


################# 9. Copying a list (common mistake) #################

a = [1, 2, 3]
b = a  # NOT a copy, both point to the same list

b.append(5)
print(a) #This is eg.

c = a.copy() # This is real copy (or a[:])
c.append(10)
print(a)
print(c)


#=================== 10. Small data engineering example ==================#
# Simulating cleaning rows from a CSV
raw_rows = [
    "1, Amit , 25",
    "2, Sara , 30",
    "3, John , ",
]

cleaned = []
for line in raw_rows:
    parts = [p.strip() for p in line.split(",")]
    if parts[2] != "":
        cleaned.append({
            "id": int(parts[0]),
            "name" :parts[1],
            "age": int(parts[2])
        })
        
print(cleaned)



#++++++++++++++++ Practice +++++++++++++++++++#
#  1. Make a list of 5 numbers and print only the ones greater than 10.

nums = [5, 13, 9 , 12, 10]

# num = [n for n in nums if n>10]
for i in nums:
    if(i>10):
        print(i)
        break;

# 2. Given [" Pune", "delhi ", "KOLKATA "], clean it to ["pune", "delhi", "kolkata"].

city_list =  [" Pune", "delhi ", "KOLKATA "]

clean_city_list = [city.strip().lower() for city in city_list]
print(clean_city_list)

# 3. From a list of dicts with name and salary, get the names of people earning above 50000.
