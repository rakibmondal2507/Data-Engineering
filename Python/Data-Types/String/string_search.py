# startwith 

phone = "+91-8471348234"
print(phone.startswith("+91"))

email = "rakib@gmail.com"
print(email.endswith("gmail.com"))
print(email.endswith("google.com"))

#use case 
file = "data_backup.csv"
print(file.endswith(".csv"))

# 'substring' in 'string' - checks if a words exists in string

print("@" in email)


#################################
        # find()
##################################
#find() is great when combined with other methods to add dynamics
#find() returns the string position of a word in string

phone = "+34-42892-4725-2"
phone2 = "48-8429-423893"
phone3 = "0042-42783-42877"
print(phone.find("-"))
#using slice
print(phone[phone.find("-")+1: ])
print(phone2[phone2.find("-")+1: ])
print(phone3[phone3.find("-")+1: ])

# find() is great when combined with to other methods to add dynamics
