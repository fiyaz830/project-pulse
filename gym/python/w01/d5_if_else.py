orders = [
    {"order_id": 1, "customer": "messi", "city": "rosario", "amount": 1000},
    {"order_id": 2, "customer": "suarez", "city": "salto", "amount": 3300},
    {"order_id": 3, "customer": "neymar", "city": "natwal", "amount": 977},
    {"order_id": 4, "customer": "iniesta", "city": "bareclona", "amount": 1233},
    {"order_id": 5, "customer": "dhoni", "city": "ranchi", "amount": 777},
    {"order_id": 6, "customer": "xavi", "city": "bareclona", "amount": 7676},
]

total_rev = 0
order_count = 0
for o in orders:
    total_rev += o["amount"]
    if o["amount"] > 1000:
        order_count += 1

print(f"Total revenue is ₹{total_rev:,.2f}")
print(f"Count of orders with amount > 1000 are {order_count}")


city_counts = {}

for o in orders:
    city = o["city"]
    city_counts[city] = city_counts.get(city, 0) + 1

print(city_counts)
