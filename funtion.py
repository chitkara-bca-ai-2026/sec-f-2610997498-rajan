# def calc_multi(a, b):
#     multiply = a * b
#     print(multiply)
#     return multiply

# calc_multi(5, 3)

# calc_multi(10, 2)


# def calc_sub(a , b):
#     return a - b

# sub = calc_sub(10, 5)
# print(sub)

# from traceback import print_list


# herios = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow"]
# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end="1")

# print_list(herios)


# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(9999)

# def converter(usd_val):
#     inr_val = usd_val * 82.74
#     print(usd_val, "USD =", inr_val, "INR")

# converter(99)




# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n - 1)

# show(5)


def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n - 1) + n
sum = calc_sum(50)

print(sum)