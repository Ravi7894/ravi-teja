"""while loops"""
# print even numbers in a given range
# state
# st = 1
# end = 100

# Behavior

# while st <= end:
#     if st % 2 ==0:
#         print(st,end="-->")
#     st += 1
# print("-----end of while loop-------")
#
# # state , validation, behavior
# # state
# n1 = int(input("enter number 1 : "))
# n2 = int(input("enter number 2 :"))
# # validation 10 100 100 10, 100 100
# if n1 <= n2:
#     print("--valid input data---")
#     while n1 <= n2:
#         if n1 % 2 ==0:
#             print("value : ", n1)
#         n1 += 1
# else:
#     print("----invalid data-----")
# req : print numbers between 1 to 100 which are divisible by 3 or 5

'''
1. high level : numbers between 1 to 100
2. second level :divisible by 3 or 5
                divisible by 3 or divisible by 5
'''
# state
# num1 = int(input("enter start value : "))
# num2 = int(input("enter end value : "))
#
# #behavior
# if num1 <= num2:
#     print("valid data")
#     while num1 <= num2:
#         if num1 % 3 ==0 or num1 % 5 ==0:
#             print("value :", num1)
#         num1 += 1
# else:
#     print("invalid data")

# print numbers between 1 to 100 which divisible by 4 and 7

# state
# num1 = int(input("enter start numbers: "))
# num2 = int(input("enter ending numbers: "))
# # validation 10 100, 20 100, 100 2
# if num1 <= num2:
#     print("valid data")
#     while num1 <= num2:
#         if num1 % 4 ==0 or num2 % 7 == 0:
#             print("value :",num1)
#         num1 += 1
# else:
#     print("invalid data")

# st = int(input("enter start value : "))
# end = int(input("enter end value : "))
# if st < end:
#     while st < end:
#         if st % 2 == 0:
#             print("value :", st)
#         st += 1
# elif st > end:
#     while st >= end:
#         if st % 2 == 1:
#             print("value : ", st)
#         st -= 1
# else:
#     print("cant iterate")
#
# while st <= end:
#     print("value is :", st)
#     st += 1


# result of exam
# # state
# marks = int(input("enter the exam marks :"))
#
# # behavior
# # 1. validation
# # 2. marks should be greater than zero and less than hundred
# if marks >= 0 and marks <= 100:
#     print("vaild marks")
#     if marks >= 35:
#         print("result pass")
#         if marks >= 60:
#             print("first class")
#             if marks >= 90:
#                 print("distinction")
#                 if marks == 100:
#                     print("congratulations")
#         elif marks >= 50:
#             print("second class")
#         else:
#             print("third class")
#     else:
#         print("result fail")
# else:
#     print("invalid marks")

#  req : print numbers from 1 to 10
# state : is changing in each iteration
#  behavior : same : printing the data
# i = 0
# while i <= 9:
#     i += 1
#     print(i)
'''
req : print numbers between 1 to 10 except 5
p1 : print number
p2 : increment number
p3 : check number <= 10
p4 : check num = 5
'''
# i = 1
# while i<=10:
#     if i != 5:
#         print(i)
#     i = i + 1


'''req : print number 1 to 100  divisible by 4 or 5 or 7
p1 : print number 1 to 100
p2 : increment number 
p3 : check number <= 100
p4 : check divisible by 4 or 5 or 7
'''
# i = 1 # state
# while i <= 100: #behavior
#     if i % 4 == 0 or i % 5 == 0 or i % 7 == 0:
#         print(i)
#     i += 1

# req : print numbers from 10 to 1
# state
'''data initalization x = 10
#  behavior
condition verfication : while x >= 1
business logic        : print(x)
operation on input data : x -= 1
'''
# x = 10
# while x>= 1:
#     print(x)
#     x -= 1
#  sdlc - agile methodolagy

#  i req. gathering : print even numbers from 15 to 100
#  state : 15 to 100 numbers  print even numbers
#  behavior : operators : <= == , if , else ,while

# str = int(input("enter first num :"))
# end = int(input("enter last num :"))
#
# while str <= end:
#     if str % 2 == 0:
#         print(str)
#     str += 1

# req : print numbers between 1 to 100 which are odd numbers and divisibleby 3 and 5
'''
validation logic : if else
business logic : while
c1 : print numbers b/w 1 to 100 
c2 : odd numbers
c3 : divisible by 3 and 5
'''
# #state
# n1 = 1
# n2 = 100
#
# # behavior
# if n1 <= n2:
#     while n1 <= n2:
#         if n1 % 2 == 1:
#             if n1 % 3 ==0 and n1 % 5 == 0:
#                 print("value :", n1)
#         n1 += 1
# else:
#     print("invalid input data")


# req : print even numbers between 1 to 20
'''
# p1 = write code for 1 to 20 numbers
# p2 = display only even numbers
# p3 = it should be in list format using while loop'''
# # state
# x = 1
# l1 = []
# while x<= 20:
#     if x % 2 ==0:
#         l1.append(x)
#
#     x += 1
# print(l1)


#  req : print numbers divisible by 5 between 1 to 100

# '''
# p1 : diplay first 1 to 100 num
# p2 : display only number of divisible
# p3 : using while loop'''
#
# n1 = 1
# n2 = 100
# while n1 <= n2:
#     if n1 % 5 == 0:
#         print(n1)
#     n1 += 1

# req : print numbers 1 to 20 but first ten numbers in single line
# '''
# p1 : fist dispaly first 1 to 20 numbers
# p2 : then write for first ten numbers in single line code'''
# num = 1
# while num <= 20:
#     if num < 10:
#         print(num , end= "-")
#     else:
#         print(num)
#     num += 1
#  req : print nmbers which are divisible by either 3 or 8 between 1 to 1000
# '''
# p1 : take the user input, iterate till upper limit
# p2 : check whether the value divisible by 3 or 8
# p3 : if true , print the value'''
#
# x = 1
# while x <= 1000:
#     if x % 3 == 0 or x % 8 == 0:
#         print(x)
#     x += 1

#  numbers between 1 to 1000 divisible by either 5 or 8, should not divisible 3
# '''
# step1 : take the user input , iterate till upper limit
# step2 : check whether the value divisible by 5 or 8
# step3 : it should not divisible by 3
# step4 : if true , print the value inwhile loop'''
#
# n1 = 1
# n2 = 1000
# while n1 <= n2:
#     if n1 % 5 ==0 or n1 % 8 == 0:
#         if n1 % 3 != 0:
#             print(n1)
#     n1 += 1
#
#eq: print first 7  between 1 to 20
#
# '''
# step1 : take starting value and print upto upper value
# step2 : display only first 7 value
# step3 : we have to use break and count'''
#
# n1 = 1
# n2 = 20
# counter = 0
# while n1<= n2:
#     print(n1)
#     counter += 1
#     if counter == 7:
#         break
#     n1+= 1

# n1 = 1
# n2 = 100
# counter = 0
# while n1 <= n2:
#     if n1 % 2 ==0:
#         print(n1)
#         counter += 1
#         if counter == 11:
#             break
#     n1 += 1

#  req : print first 4 numbers divisible by 6 between 1 to 100

# '''
# step1 : take input value and output value dispaly
# step2 : display number with are divisible by 6
# step3 : and print only first 4 values '''
#
# n1 = 1
# n2 = 100
# count = 0
# while n1 <= n2:
#     if n1 % 6 == 0:
#         count += 1
#         print(n1)
#         if count == 4:
#             break
#
#     n1 += 1

#  Print first 7 numbers  between 1 to 100. Which are divisible by 5.
# # If number ends with 0(divisible by 10) don't consider it.
#
# n1 = 1
# n2 = 100
# count = 0
# while n1 <= n2:
#     if n1 % 5 ==0:
#         if n1 % 10 ==0:
#             n1 += 1
#             continue
#         print(n1)
#         count += 1
#         if count == 7:
#             break
#     n1 += 1
