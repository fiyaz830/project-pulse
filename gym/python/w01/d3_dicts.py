order = {"order_id" : 999, "customer": "Shaik", "city": "Rajahmundry", "amount":1250}

print(f"Order #{order['order_id']} is from customer {order['customer']} in city {order['city']} of amount ₹{order['amount']:,.2f}")

print(order.get("coupon"))
print(order.get("coupon", "none"))
order["status"] = "Completed"

print(order)

print(order.get("amount", 0))
print(order.get("discount", 0))
print(order)
