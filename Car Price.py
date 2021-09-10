# base price
basePrice = float(input("What is your base car price? "))

# additional charges
tax = float(input("tax: "))
license = float(input("license: "))
dealerPrep = float(input("dealer prep: "))
destinationCharge = float(input("destination charge: "))

const = 1.1245

total = round((tax + license + dealerPrep + destinationCharge + basePrice)* const)

print(total)

## exit
input("Press enter to exit\n")