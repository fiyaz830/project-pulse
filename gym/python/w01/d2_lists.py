amounts = [1250, 899, 3400, 450, 2100]

print(f"Order count is {len(amounts)}")
print(f"The total revenue is ₹{sum(amounts):,.2f}")
print(f"The smallest order is ₹{min(amounts):,.2f}")
print(f"The biggest order is ₹{max(amounts):,.2f}")
print(f"The first order is ₹{amounts[0]:,.2f}")
print(f"The last order is ₹{amounts[-1]:,.2f}")
print(f"The first 3 orders are ₹{amounts[0]:,.2f} , ₹{amounts[1]:,.2f}  and ₹{amounts[2]:,.2f}   ")

avg_order_value = sum(amounts) / len(amounts)

print(f"The average order value is ₹{avg_order_value:,.2f}")
