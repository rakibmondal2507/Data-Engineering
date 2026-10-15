######### 1. Create a dictionary ##########

student = {"id": 1, "name": "Amit", "age": 25}
address = dict(nearest_city="Kolkata", dist="(N) 24 pgs", state="West Bengal")
print(student)
print(address)

empty = {}
print(empty)

also_empty = dict()
print(also_empty)



#++++++++++++ 2. Access values +++++++++++++#

print(student["name"])
print(student.get("age"))
print(student.get("city")) #no error -> output : none
print(student.get("city","unknown")) #if value is not present there unknwon will default values
print(student.get("age","unknown")) #print age because age is presnt there

## Use .get() when the key might be missing. student["city"] would crash with a KeyError.


#++++++++++++++ 3. Add, change, remove ++++++++++++++#

student["city"] ="Kolkata" ## add new key
print(student)

student["age"] = 26   # change existing value

student.update({"age":24, "grade":"A"}) # add/change many
print(student)

del student["city"]   # remove a key
del student["grade"]
print(student)

age = student.pop("age")    # remove and return value
print(age)
print(student)


#+++++++++++++++ 4. Check if a key exists +++++++++++++++#

print("name" in student) #output : boolean
print("age" in student) #output : boolean


#+++++++++++++++++ 5. Loop through a dictionary +++++++++++++++++#

student = {"id": 2, "name": "Rakib", "city": "Kolkata"}
print(student.keys()) #print all keys
print(student.values()) #print all values
print(student.items()) #print all keys and values

for key in student:
    print(key) # print all keys
    
for key, value in student.items():
    print(key ,"=" ,value)
    
    
    
#+++++++++++++++++ 6. Dictionary comprehension ++++++++++++++++#
## Like list comprehension, but builds a dictionary: {key: value for item in list}

names = ["amit", "sara", "john"]
length = {n: len(n) for n in names}
print(length)

raw = {" ID ": 1, "Name ": "Amit", " AGE": 25}
clean = {key.strip().lower() : value for key,value in raw.items()}
print(clean)


#+++++++++++++++++ 7. Nested dictionaries (like JSON) +++++++++++++++++#

user = {
    "id" : 1,
    "name" : "Rakib",
    "address": {
        "city": "Kolkata",
        "pin" : 700001
    },
    "skills": ["python", "sql"]
}
# print(user)
print(user["address"]["city"])
print(user["skills"][0])

## This is exactly how API responses look.


#+++++++++++++++ 8. Lookup table (very common) +++++++++++++++#

## Use a dictionary to convert codes into readable values.

status_map = {"A": "Active", "I": "Inactive", "P": "Pending"}
rows = ["A", "P", "A", "I"]

readable = [status_map[key] for key in rows]
print(readable)

#+++++++++++ 9. Counting and grouping +++++++++++#

cities = ["pune", "delhi", "pune", "kolkata", "pune"]

count = {}

for  city in cities:
    count[city] = count.get(city, 0) + 1
    
print(count)

count_compre = {city:cities.count(city) for city in set(cities)} #set removes duplicate
print(count_compre)

#======== Group names by city ============#

people = [
    {"name": "Amit", "city": "pune"},
    {"name": "Sara", "city": "delhi"},
    {"name": "John", "city": "pune"},
]

groups = {}

for p in people:
    groups.setdefault(p["city"],[]).append(p["name"])
    
print(groups)


#++++++++++++++ 10. Copying (same trap as lists) ++++++++++++#

a = {"x": 1}
b = a            # NOT a copy
c = a.copy()     # real copy


#+++++++++++++ 11. Small data engineering example ++++++++++#

## Convert a CSV row into a dictionary, then validate it.

header = ["id", "name", "age"]
line = "1, Amit , 25"

values = [v.strip() for v in line.split(",")]
print(values)
row = dict(zip(header, values))
print(row)

row["id"] = int(row["id"])
row["age"] = int(row["age"])

print(row)

#=============================#
        # Practice
#=============================#

# 1. Make a dictionary for a product with name, price, stock. Then increase the price by 10%.
        
products = {
    "name": "Laptop",
    "price": 39000,
    "stock" : True   
}

products["price"] = products["price"] * 1.10

print(products)


## 2. Given ["a", "b", "a", "c", "a", "b"], count how many times each letter appears.

letter = ["a", "b", "a", "c", "a", "b"]
count = {}

for l in letter:
    count[l] = count.get(l, 0) + 1

print(count)

count_com = {l: letter.count(l) for l in set(letter)}

print(count_com)

## 3. Given {"A": "Active", "I": "Inactive"} and the list ["A", "I", "A", "X"], convert it to readable words and use "Unknown" for codes not in the dictionary.

status_map = {"A": "Active", "I": "Inactive"} 
codes = ["A", "I", "A", "X"]

readable = [status_map.get(c, "unknown") for c in codes]

print(readable)
