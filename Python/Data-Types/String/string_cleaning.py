#===================================
        # Clean Whitespaces
#===================================

# ===== Remove spaces ======


text = "   Engineering".lstrip()
print(text)

text = "Engineering   ".rstrip()
print(text)

print("   Engineering   ".strip())

text = "###Rakib###".strip("#")
print(text)

#use cases 1

text ="  Engineering"
print(len(text))
print(len(text.strip()))
print(len(text) - len(text.strip()))
print(len(text) == len(text.strip()))


#===================================
        # Case conversion
#===================================

text = "Python PROGRAMMING"
print(text.lower())
print(text.upper())

#use case

search = "Email ".lower().strip()
data = "  eMaIL ".lower().strip()

print(search==data)

################ challange ##############

# Turn the messy string into a single clean summary with name,role and age

user_data = "968-Maria, (D@t@ Engineer);;  27  "

# print(user_data.strip().replace("968-","name: ").replace(","," | ").replace("(","role: ").replace("D@t@","data").replace(")","  |  ").replace(";;"," age:").lower().strip())


data = user_data.strip()
name = data.split("-")[1].split(",")[0].strip()
role = data.split("(")[1].split(")")[0].replace("D@t@","data").strip()
age = data.split(";")[2].strip()

# print(age)
print(f"name: {name.lower()} | role: {role.lower()} | age: {age}")
