weight = int(input())

# Ground Shipping 
if weight <= 2:
  price = 20 + 1.5 * weight
elif weight <=6:
  price = 20 + 3 * weight
elif weight <= 10:
  price = 20 + 4 * weight 
else:
  price = 20 + 4.75 * weight

print(f"Ground Shipping: ${price} \n")

premium_cost = 125

print(f"Premium Ground Shipping: ${premium_cost} \n")


# Drone Shipping
if weight <= 2:
  price = 4.5 * weight
elif weight <=6:
  price = 9 * weight
elif weight <= 10:
  price = 12 * weight 
else:
  price = 14.25 * weight

print(f"Drone Shipping: ${price} \n")

