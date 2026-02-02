print("Welcome to the Band Name Generator")
print("Author: Rick19F\n\tDone in 4 attempts\n")

city = str(input("What's the name of the city you grew up in?\n"))
while city is None or city.strip() == "":
    city = str(input("Try again. What's the name of the city you grew up in?\n"))
pet_name = str(input("What's your pet's name?\n"))
while pet_name is None or pet_name.strip() == "":
    pet_name = str(input("What's your pet's name?\n"))

print(f"Your band name could be...\n\t{city} {pet_name}")
