# Challenge

# Write a Car Salesman program where the user enters the base price of a car.
# The program should add on a bunch of EXTRA fees such as tax, license,
# dealer prep and a destination charge.
# The other fees should be set values (constants).
# Display the actual price of the car once all the extras are applied.


from random import randrange

while True:
    try:
        basePrice = float(input("what is the base price of your car? "))
        break
    except:
        pass

tax = 0.08
license = 51.75
dealerPrep = randrange(0, 75)
destCharge = randrange(1000, 1500)

const1 = 52
const2 = 18

total = (license + dealerPrep + destCharge) + \
    round(tax * basePrice) + (const1 + const2) + basePrice

print(
    f"""
tax: {tax*basePrice}
license plate cost: {license}
dealer prep: {dealerPrep}
destination charge: {destCharge}

total: {round(total)}
    """
)
