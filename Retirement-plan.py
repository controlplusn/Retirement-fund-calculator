#Calculate how much fund do you need to retire comfortably
print("=" * 20)
heading = "Assumptions"
heading.upper()
print(heading)
print("=" * 20)


monthly_retirement = int(input("Monthly Retirement: "))
average_infaltion = float(input("Average infaltion: "))
current_age = int(input("Current age: "))
retirement_age = int(input("Retirement age: "))

annual_retirement = monthly_retirement * 12
yearsToRetire = retirement_age - current_age

print("\n===================SUMMARY======================")
print(f"Monthly Retirement: {monthly_retirement}")
print(f"Annual Retirement: {annual_retirement}")
print(f"Expected Average Infaltion Rate: {average_infaltion}")
print(f"Current Age: {current_age}")
print(f"Retirement Age: {retirement_age}")
print(f"Years to Retire: {yearsToRetire}\n")

print("=" * 20)
heading2 = "Retirement Needs"
heading2.upper()
print(heading2)
print("=" * 20)

print(f"Future Value of Annual Retirement at age {retirement_age}: ") #Need calculations
print(f"Investment Yield During Retirement (%): ") #Need calculations

print("\n")
print("=" * 20)
print("TOTAL RETIREMENT FUND NEEDED: ") #Need calculations
