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

const = 0.125

total = (license + dealerPrep + destCharge) + \
    round(tax * basePrice) + (const * basePrice) + basePrice

print(
    f"""
tax: {tax*basePrice}
license plate cost: {license}
dealer prep: {dealerPrep}
destination charge: {destCharge}
total: {round(total)}
    """
)
