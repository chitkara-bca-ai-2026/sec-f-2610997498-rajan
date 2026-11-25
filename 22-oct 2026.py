# def check_even_odd(n):
#     if n % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"

# def c_to_f(celsius):
#     f = (celsius * 9/5) + 32
#     return f

# num = int(input())
# temp_c = float(input())

# print('Number is:', check_even_odd(num))
# print(f'Fahrenheit: {c_to_f(temp_c):2f}')



tution_fee = float(input("Enter Tution Fee: "))
transport_fee = float(input("Enter Transport Fee: "))
exam_fee = float(input("Enter Lab Exam Fee: "))

total_fee = tution_fee + transport_fee + exam_fee
discount = total_fee/100*5
net_fee = total_fee - discount

print("--- FEE RECEIPT ---")
print(f"Subtotal   :{tution_fee}")
print(f"Discount (5%)  :{discount}")
print(f"")