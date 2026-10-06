# replace()

price = "1342,432"
print(price.replace("," , "."))

phone = "213-3248-423"
print(phone.replace("-" , "/"))


phone = "213-3248-423"
print(phone.replace("-" , ""))

price = "$4,283.99"
print(price.replace("$" , "").replace("," , ""))

#Challange 1 
# Convert the messy phone number into a clean number format with only digits

# "+49 (176) 123-4567" -> 00491761234567

ph = "+49 (176) 123-4567"
print(ph.replace("+" , "00").replace(" ", "").replace("(", "").replace(")","").replace("-",""))

# Join Strings
fname = "Rakib"
lname = "Mondal"
lname = fname +" "+lname
print(lname)

folder = "C:Users/Rakib/"
file = "report.csv"
full_path = folder + file
print(full_path)

#f-string
name = "Rakib"
age = 23
is_student = True
print(f"My name is {name}, I am {age} years old and my student status is {is_student}")
print(f"2 + 3 = {2+3}") #expression also work
print(f"{{This is me}}")


#Split
stamp = "2026-05-13 21:40" 
print(stamp.split(" "))
date = "2026-30-09"
print(date.split("-"))

csv_file = "1343,Rakib,India,24-12-2010"
print(csv_file.split(","))


#String Repetition
print("ha"*3)

print("="*30)
print("Rakib")
print("="*30)


#=========================================
            #DATA EXTRACTION
#=========================================

#++++ Indexing & Slicing +++++++

text = "python"

#Extract the first character
print(text[0])
print(text[-6])

#Extract the last character
print(text[5])
print(text[-1])

date = "2026-07-25"
print(date[0:4])
print(date[:4])

#extract month
print(date[5:7])

#extract day
print(date[8:])
print(date[-2:])
