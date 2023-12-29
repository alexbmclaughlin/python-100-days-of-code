print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))

individual_bill = bill / split
tip = ((percentage / 100) * individual_bill)
total = round(individual_bill + tip, 2)

print(f"Each person should pay: ${total}")