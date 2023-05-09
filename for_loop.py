#for loop for to iterate through group of values
'''
step1 : first iterate all numbers (marks)
step2 : assin values according to our reqiuement
step3 :
# '''
# smarks = [34,22,11,55,89,36,90,100] #state
# for marks in smarks: #behavior
#     print("marks--", marks)
#     if 0 <= marks <= 100:
#         print("vaild marks")
#         if marks >= 35:
#             print("pass")
#             if marks >= 60:
#                 print("first class")
#                 if marks >= 90:
#                     print("distinction")
#                     if marks >= 100:
#                         print("congratulations")
#             elif marks >= 50:
#                 print("second class")
#             else:
#                 print("third class")
#         else:
#             print("fail")
#     else:
#         print("invaild marks")

#  Req : print each character of string in lower case
# state
# course = "PYTHON-PROGRAMMING-LANGUAGE"
# # BEHAVIOR
# for i in course:
#     print("char: ", i.capitalize())

# list1 = [1, 2.5, True, "madhu" , [1, 2, 3], 5.0 ,False, 7]
# for i in list1:
#     print("value: ", i)

# e_data = {"id": 100, "name": "ravi teja", "sal": 1000}
# for key, val in e_data.items():
#     print("dict_data :", key, val)

# set1 = {1, 2, 3, 4, 5, 6}
# for val in set1:
#     print("set value :", val)

# sum = 0
# for i in range(1, 4):
#     print(i)
#     result = 5 * i
#     sum += result
# print("sum :", sum)

#  find sum of numbers from 1 to 100
'''
# step1 : display by 1-100
# step2 : sum of all number
# step3 : '''
# i = 1
# sum = 0
# while i <= 101:
#     sum += i
#     i += 1
# print("total : ",sum)

# sum = 0
# for i in range(1, 101):
#     sum += i
# print("total :", sum)

#  find student grade (operators , DM, loops with CS)
#  state
# marks  = {19631: 55, 128 : 35, 8975 : 56, 7896 : 80, 31645 : 34}
# #  behaviors
# for id, marks in marks.items():
#     print("***result for *****",id)
#     if marks >= 0 and marks <= 100:
#         print("vaild marks")
#         if marks >= 35:
#             print("--Result :pass--")
#             if marks >= 60 :
#                 print("-first class-")
#                 if marks == 100:
#                     print("** distinction **")
#             elif marks >= 50 :
#                 print("--second class--" )
#         else:
#             print("--result : fail--")
#     else:
#         print("invaild marks")

'''
1. find char count
# steps1 : first give group of characters
# steps2 : use count function to count each character in string sing for loop'''
# #  state
# msg = "hello world"
# # behavior
# count = 0
# for i in msg:
#     count += 1
# print("count:", count)

#  req : find capital letters, small letters

'''
step1 : giving data group string with capital letters and small letters
step2 : use for loop and islower'''
# state
string_data = "Ravi Teja Person Learning Python In Vn2 Solution"

# behavior
# lower = 0
# upper = 0
# for i in string_data:
#     if(i.islower()):
#         lower += 1
#     else:
#         upper += 1
# print("upper string numbers: ", upper)
# print("lower string numbers :", lower)
#
# lower = 0
# upper = 0
# for i in string_data:
#     if i >= "a" and i <= "z":
#         lower += 1
#     else:
#         upper += 1
# print("lower",lower)
# print("upper",upper)

# find repeated char count

# str = "ravi teja now learning python in vn2 solution"
# duplicate_list = []
# for i in str:
#     if str.count(i)>1:
#         if i not in duplicate_list:
#             duplicate_list.append(i)
# print(duplicate_list)

#  find vomels , consonants
# str = input("enter the string :")
# vowels = []
# consonants = []
# str.lower()
# for i in str:
#     if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
#         vowels.append(i)
#     else:
#         consonants.append(i)
# print("vomels:", vowels)
# print("consonants :" , consonants)

#  req : Get alphabets, numbers, special chars
'''
# step1 : gather group of elememts seperate elements accordingly
# step2 : using for loop'''
# str = input("enter the string value:")
# alphabets = digits = special = ""
#
# for i in str:
#     if(i.isalpha()):
#         alphabets = alphabets + i
#     elif(i.isdigit()):
#         digits = digits +i
#     else:
#         special = special +i
# print("alphabets:",alphabets)
# print("digits :", digits)
# print("special :", special)

#  req: reverse a string
# str = " ravi teja was learn vmware, testing, linux, storage"
# #print(str[::-1])
# out=''
# for i in str:
#     out=i+out
# print(out)
# n=input('enter a string:')
# vowels=''
# consonants=''
# for i in n:
#     if i in "AEIOUaeiou":
#         vowels+=i
#     else:
#         consonants+=i
# print("vowles:", vowels)
# print("consonants:", consonants)

# for i in range(1):
#     print("range val: ", i)

# set1 = {1,2,3,4,5}
string = (0,1,2,3,4,5,6,True,False,"False",2,3,4,5)
out  = []
for i in string:
    if i not in out:
        out += [i]
print(out)