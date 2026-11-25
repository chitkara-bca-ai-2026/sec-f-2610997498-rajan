# 1. Variable Scope (Global Variable)
# Yeh variable poore program mein kahin bhi use kiya ja sakta hai
company_name = "Tech Solutions Ltd."


def calculate_salary(hours_worked, hourly_rate):  # 2. Parameters (Inputs)
  # 3. Variable Scope (Local Variable)
  # Yeh variable sirf is function ke andar hi accessible hai, bahar nahi
  bonus = 1000

  # Reusable code block: Calculation ka logic
  total_pay = (hours_worked * hourly_rate) + bonus

  # Global variable ko function ke andar use kar rahe hain
  print(f"Company: {company_name}")

  # 4. Return Value (Output wapas bhejna)
  return total_pay


# --- Functions ko use karna (Reusable Code Blocks) ---

# Employee 1 ke liye function call kiya
employee1_salary = calculate_salary(40, 500)
print(f"Employee 1 Total Salary: {employee1_salary}\n")

# Employee 2 ke liye same function ko dobara use kiya (Reusability)
employee2_salary = calculate_salary(35, 600)
print(f"Employee 2 Total Salary: {employee2_salary}\n")


# --- Variable Scope Error Example (Samajhne ke liye) ---
# Agar aap yahan print(bonus) likhenge, toh Python error dega
# Kyunki 'bonus' ek Local Variable hai jo function ke bahar exist nahi karta.