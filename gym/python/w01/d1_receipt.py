order_id = 123
customer = "Shariff"
city = "Hyderabad"
item = "Laptop"
price = 92850
qty = 1
total = price * qty
gst_rate = 0.18
gst = total * gst_rate
grand_total = total + gst

print(f"Order#{order_id}")
print(f"Customer name is {customer}")
print(f"{customer} is from {city}")
print(f"{customer} bought {qty} {item} for ₹{price:,.2f}")
print(f"Price of the {item} is ₹{price:,.2f}")
print(f"Sub-total is ₹{total:,.2f}")
print(f"GST amount is ₹{gst:,.2f}")
print(f"Grand total is ₹{grand_total:,.2f}")
