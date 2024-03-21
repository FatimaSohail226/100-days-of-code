print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip = bill * tip_percent / 100
total_bill = bill + tip
print("Each person should pay $", total_bill / people)
