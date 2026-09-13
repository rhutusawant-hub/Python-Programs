# Create a travel expense calculator that accepts distance, vehicle mileage, and fuel price and 
# calculates estimated fuel cost.

distance = float(input("Enter distance in km: "))
mileage = float(input("Enter vehicle mileage (km/l): "))
fuel_price = float(input("Enter fuel price per litre: "))

fuel_required = distance / mileage
fuel_cost = fuel_required * fuel_price

print(f"Fuel Required: {fuel_required:.2f} litres")
print(f"Estimated Fuel Cost: ₹{fuel_cost:.2f}")