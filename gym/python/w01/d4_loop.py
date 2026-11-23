orders = [
    {"order_id": 1, "customer": "messi", "city": "rosario", "amount": 1000},
    {"order_id": 2, "customer": "suarez", "city": "salto", "amount": 3300},
    {"order_id": 3, "customer": "neymar", "city": "natwal", "amount": 977},
    {"order_id": 4, "customer": "iniesta", "city": "bareclona", "amount": 1233},
]

total = 0
for o in orders:
    print(f"#{o['order_id']} | {o['customer']} | {o['city']} | ₹{o['amount']:,.2f}")
    total += o["amount"]

print(f"Total : ₹{total:,.2f}")
