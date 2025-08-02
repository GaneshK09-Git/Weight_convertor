# Python weight converter

# Ask the user to enter their weight
weight = float(input("Enter your weight: "))

# Ask the user to specify the unit: K (kilograms) or P (pounds)
unit = input("Kilograms or pounds? (K or P): ")

# Convert the unit to uppercase to accept both uppercase and lowercase inputs
unit = unit.upper()

# Check the unit and convert accordingly
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not a valid unit. Please enter 'K' for Kilograms or 'P' for Pounds.")
