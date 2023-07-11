# Day 2 - Understanding Data Types and How to Manipulate Strings

billamount = float(input("What is the total bill amount?: "))
print("how much would you like to tip?")
percent = int(input("Percent: "))
print("how many people would like to split the bill?")
people = int(input("number of people: "))

total = round((billamount * (1 + (percent/100))) / people,2)

print(f"each person should pay: ${total}")