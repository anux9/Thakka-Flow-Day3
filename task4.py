products = float(input("Products value: "))
city = input("City: ").strip().lower()
weight = float(input("Weight (kg): "))
coupon = input("Coupon (leave empty if none): ").strip().upper()

# Calculate shipping
if city == "riyadh":
    shipping = 15
elif city == "jeddah" or city == "dammam":
    shipping = 20
else:
    shipping = 30

if weight > 5:
    shipping += (weight - 5) * 2

# Apply coupon
discounted_products = products

if coupon == "TF10":
    if products >= 100:
        discounted_products = products * 0.90
    else:
        print("TF10 requires products value of at least 100 SAR")

elif coupon == "FREESHIP":
    shipping = 0

elif coupon != "":
    print("Invalid coupon")

# Free shipping for orders of 300 SAR or more
if discounted_products >= 300:
    shipping = 0

# Calculate VAT and total
subtotal = discounted_products + shipping
vat = subtotal * 0.15
total = subtotal + vat

# Print order summary
print("\n--- Order Summary ---")
print(f"Products value: {products:.2f} SAR")
print(f"City: {city.title()}")
print(f"Products after discount: {discounted_products:.2f} SAR")
print(f"Shipping: {shipping:.2f} SAR")
print(f"VAT: {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")