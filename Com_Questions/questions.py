#Time for while vs for loops
# import time
# import datetime
# def while_loop():
#     i=0
#     while i<1000:
#         print(i)
#         i +=1

# def for_loop():
#     for i in range(1000):
#         print(i)

# org_time = time.time()
# while_loop()
# w = time.time() - org_time
# org_time=time.time()
# for_loop()
# f = time.time()-org_time
# print("While loop time: ", w)
# print("For loop time:", f)

# t = time.localtime()
# formated_time = time.strftime("%Y-%m-%d %H:%M:%S", t  )
# print(formated_time)

# timee= datetime.datetime.now()
# print(timee)

# timem = timee.strftime("%Y-%m-%d %H:%M:%S")


#------- Sorting through dicts and dates --------

# import datetime
# val =datetime.datetime.now()
# print(val)
# data :list = [
# "2026-01-12 22:18:17",
# "2026-01-11 22:18:18",
# "2026-01-12 22:18:19"
# ]

# sorted_val = sorted(
#     data,
#     key=lambda x :datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
# )
# print(sorted_val)


# dicts = {
#     1 : "2026-01-12 22:18:17",
#     2 : "2026-01-11 22:18:18",
#     3 : "2026-01-12 22:18:19"
# }

# sorted_vals = dict(sorted(
# dicts.items(),
# key=lambda x : datetime.datetime.strptime(x[1],"%Y-%m-%d %H:%M:%S")

# ))
# print(sorted_vals)
# print(dicts.items())

# import datetime

# lst:list = [

#     "2026-01-10 22:18:55",
#     "2026-01-11 22:18:55",
#     "2026-01-10 22:18:54",
# ]

# sorted_lst = sorted(
#     lst,
#     key=lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S")
# )
# print(sorted_lst)

# dst = {
#     1 : "2026-01-10 22:18:55",
#     2 : "2026-01-11 22:18:55",
#     3 : "2026-01-10 22:18:54"   
# }

# sorted_dict = dict(
#     sorted(
#         dst.items(),
#         key=lambda x : datetime.datetime.strptime(x[1],"%Y-%m-%d %H:%M:%S")
#     )
# )
# print(sorted_dict)


#---------------Remote-odd/even-------------------

# val = 51
# target_val= 56

# while True:

#     if val < target_val-1:
#         val +=2
    
#     if val == target_val -1:
#         break

# print(f"The Current val is {val} and add +1 to reach {target_val}")



#N number , all odd numbers print till that n

# num = int(input("Enter a number: "))


# for i in range(num):
#     if num < 2:
#         print(1)
#         break

#     if i % 2 == 0:
#         continue

#     else:
#         print(i)


#--------Write a Python program that counts the frequency of each character in a string using a dictionary.------------


# letter = input("Input :-> ")
# my_dict = {}


# for ch in letter:

#     if ch in my_dict:
#         my_dict[ch] +=1
    
#     else:
#         my_dict[ch] =1

# print(my_dict)



#Palidrome number 

# numm = 141
# numm = str(numm)
# rev_num=numm[::-1]

# if numm==rev_num:
#     print("Palidrome")
# else:
#     print("Not Palidrome")


#-- Highest marks and print there name and marks----#

# students = {"Ali": 85, "Ahmed": 78, "Sara": 92}
# highest_marks = max(students.values())

# name =''

# for key,val in students.items():
#     if val == highest_marks:
#         name=key
#         break

# print(name,highest_marks) 

# dates = [
#     "2024-01-05",
#     "2023-12-25",
#     "2024-01-01"
# ]

# import datetime

# sorted_vals = sorted(
#     dates,
#     key=lambda x :datetime.datetime.strptime(x,'%Y-%m-%d')
# )
# print(sorted_vals)
# sorted_vals.reverse()

#--prime--

# numm = int(input("INPUT A NUM --> "))
# flag=True
# for i in range(2,int(numm/2)):
#     if numm < 2:
#         print("Ënter a bigger number : ")
#         break
#     if numm%i==0:
#         print("Not a Prime")
#         flag=False
#         break

# if flag:
#     print("prime")


#factorial of a num
# n=7
# def factorial(n):
#     if n==1:
#         return 1
    
#     return n*factorial(n-1)

# val = factorial(n)
# print(val)