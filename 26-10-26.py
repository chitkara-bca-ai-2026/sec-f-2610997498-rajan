# rupee = float(input("Enter amount in INR:"))
# usd_rate = float(input("Enter USD rate (INR per USD):"))
# eur_rate = float(input("Enter EUR rate (INR per EUR):"))

# usd = (rupee/usd_rate)

# print(usd)


# def fabb(n):
#     if n==0 or n==1:
#         return n
#     return fabb(n - 1)+fabb(n-2)



# for i in range(6):
#     print(fabb(i))

# n=0

# while n <= 5:
#     print(n)
#     n += 1

student_name = 'Aman Sharma'

f = open('student.txt','w')
f.write('Aman Sharma\n')
f.close()
print('Data saved to student.txt!')