weight = float(input("Enter your weight in your unit: "))
print("Put the corresponding letter for the unit you want to convert to: Put a 'L' for Lbs, or put a 'K' for KG")
conversion = input("To what unit would you like to convert: ").lower()

if conversion =="l" or conversion =="lb":
    result = weight * 2.20462
    print(f"{weight} Kg converted to Lb is {round(result, 2)} Lb")
elif conversion =="k" or conversion =="kg":
    result = weight * 0.453592
    print(f"{weight} Lb converted to Kg is {round(result, 2)} Kg")
