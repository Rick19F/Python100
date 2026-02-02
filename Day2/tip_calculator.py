print("Welcome to the Tip Calculator")
print("Author: Rick19F\n\tDone in 6 attempts")

ban = True
total = 0
while ban:
    try:
        total = float(input("What was the total bill?\n\t$ "))
        if (total is None or total <= 0):
            raise ValueError("Total should be greater than 0")
        ban = False
    except Exception as e:
        print("Sorry, try again")

available_tip = ["10", "12", "15"]
tip = str(input("How much tip would you like to give? (10, 12, 15) "))
while tip is None or tip.strip() == "" or tip not in available_tip:
    tip = str(
        input("Sorry, try again.\nHow much tip would you like to give? (10, 12, 15) "))

ban = True
people = 0
while ban:
    try:
        people = int(input("How many people to split the bill? "))
        if (people is None or people < 1):
            raise ValueError("You need at least one person to pay the bill")
        ban = False
    except Exception as e:
        print("Sorry, try again")

payment = (int(tip) / 100 * total + total) / people

print(f"Each person should pay...\n\tUSD {round(payment, 2):.2f}")
