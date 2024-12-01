food_price = float(input("Enter the price of the food item: $"))

tip = food_price * 0.18
sales_tax = food_price * 0.07

total_amount = food_price + tip + sales_tax

print("\nMeal Summary:")
print(f"Price of Food Item: ${food_price:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")