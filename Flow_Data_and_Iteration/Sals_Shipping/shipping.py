premium_ground_shipping = 125.0

def ground_shipping_cost(weight):
  flat_charge = 20  
  if weight <= 2:
    price_per_pound = 1.50
  elif weight > 2 and weight <= 6:
    price_per_pound = 3.00
  elif weight > 6 and weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return (weight * price_per_pound) + flat_charge
    
print(ground_shipping_cost(8.4))

def drone_shipping_cost(weight):
  flat_charge = -20
  return 3 * (ground_shipping_cost(weight) + flat_charge)

print(drone_shipping_cost(1.5))

def print_cheapest_shipping(weight):
  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)
  premium = premium_ground_shipping
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
    
  print(
      "The cheapest option available is $%.2f with %s shipping." 
      % (cost, method)
    )
  
print_cheapest_shipping(4.8) 
print_cheapest_shipping(41.5) 