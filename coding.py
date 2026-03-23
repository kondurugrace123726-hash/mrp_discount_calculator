mrp = float(input().strip())
discount_percent = float(input().strip())

discount_amount = mrp * (discount_percent / 100)
final_price = mrp - discount_amount

print(f"{final_price:.2f}")