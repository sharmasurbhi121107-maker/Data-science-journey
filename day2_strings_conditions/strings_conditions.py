# Day 2- Strings & conditionals Practice
#indexing
str1 = "thakur"
str2 = "college"
print(str1[0])
print(str2[4])

#slicing
str1 = "thakur"
str2 = "college"
print(str1[0:4])
print(str2[4:])

#string functions
 str = "i am studying python from apnacollege"
print(str.endswith("python"))
print(str.capitalize())
print(str.replace("o","a"))
print(str.replace("python","javascript"))
print(str.find("studying")) 
print(str.count("from"))

#conditional statements

 age = 16
 if(age>18):
    print("can give vote")
 elif(age==18):
    print("have to apply for voting card")
 elif(age<18):
    print("cannot give vote right now")

#nesting example
 age = 80
 if(age>=18):
     if(age>=80):
         print("cannot drive")
     else:
         print("can drive")



