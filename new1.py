# age = int(input("enter your age :"))
# if age >=18:
#        has_id = input("do you have id card (yes/no) :")
#        if has_id == "yes":
#         print("you can vote")
#        else:
#         print("you have not id card, you cannot vote")

# else:
#     print("you cannot vote,because you are under 18")


# print("end")


print("welcome to shopping mall")
print("_____BILL______")

product = input("Enter your product name :")
rate =float(input("Enter product rate :"))
quantity = int(input("Enter product quantity :"))


total_amount = rate * quantity
print("your total bill is :", total_amount)

if total_amount >= 5000:
    print("you are eligible for discount")
    discount = str("20%")
    print (discount)
    discount_amount= total_amount*0.20
    print ("your discount amount is :", discount_amount)
elif total_amount >= 2000:
    print("you are eligible for a small discount")
    discount = str("10%")
    print(discount)
    discount_amount = total_amount * 0.10
    print("your small discount is :", discount_amount)
elif total_amount >=1000:
    print("you are eligible for a very small discount")
    discount = str("5%")
    print(discount)
    discount_amount = total_amount * 0.05
    print("your very small discount is :", discount_amount)
else:
    print("you are not eligible for any discount")
    print("try to purchase more to get discount")

final_amount = total_amount - discount_amount
print("your final amount is :", final_amount)

print("thank you for shopping with us")
