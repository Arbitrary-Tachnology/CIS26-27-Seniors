# =====================================
# Script Name: doublingMoney.py
# Lesson: Algorithm Design (Section 10.9)
#
# Problem (from the textbook):
#   you put $10,000 into an account that earns 5% interest
#   per year. how many years until the balance is doubled
#
#
# Pseudocode (my algorithm):
#   Set year to 0, balance to 10000
#   While the balance is less than 20000
#       Add 1 to the year.
#       Set the interest to balance x 0.05
#       add the interest to the balance
#   Report year as the answer.
#======================================

#set year to 0, balance to 10000
year = 0
balance = 10000

# While the balance is less than 20000
while balance < 20000:
    year += 1
    interest = balance * 0.05
    balance += interest

print("Years to double:", year)
print("Final balance:", f"{balance:.2f}")