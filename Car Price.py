# base price
basePrice = input("What is your base car price? ")

# additional charges
tax = float(input("tax: "))
license = float(input("license: "))
dealerPrep = float(input("dealer prep: "))
destinationCharge = float(input("destination charge: "))

total = round(tax + license + dealerPrep + destinationCharge + basePrice)

print(total)

## exit
input("Press enter to exit\n")