# i = 1
# while i <= 1000:
#     print("5")
#     i += 1

# i = 5
# while i < 6:
#     print(i)
#     i -= 1

# printing no. from 1 to 100

# i =  1
# while i <= 100:
#     print(i)
#     i += 1


# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=81
# i=0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found",i)
#         break
#     else:
#          print("not found")
#     i+=1

# ODD NUMBERS

# i = 0
# while i <=10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# EVEN NUMBERS

# i = 0
# while i <=10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# TREAVERSE (travel on every element) 

# num = ["red", "green", "blue", "yellow", "black"]

# for val in num:
#     print(val)



# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# x = 36

# i = 0
# while i < len(nums):
#     if nums[i] ==x:
#         print("Found", i)
#     i += 1



# name = "Rajan"

# for c in name:
#     if c =="a":
#         print("Found a")
#         break
     
#     print(c)


#     print("END")



# LEINER SEARCH 



# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36)
# x = 36

# idx = 0
# for el in num:
#     if(el == x):
#         print("Found", idx)
#     idx += 1

# RANGE

# index = range(0,100,2)  # range(start,stop,step)
# for i in index:
#     print(i)


# QUESTION(1)

# for i in range(0, 1000, 50):
#     print(i)


# multi plication tavle in range:

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n*i)

# PASS STATEMENT

# for i in range (4):
#     pass
# print("Hello World")

# n =  5

# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)


n = 10
sum= 1
i = 1
for i in range(1, n+1):
    sum +=i
print(sum)