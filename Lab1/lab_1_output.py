def calculate_order_total(items):
    total_price = 0
    total_items = 0
    for item in items:
        price = item['price']
        quantity = item['quantity']
        total_price += price * quantity
        total_items += quantity
    return total_price, total_items

def apply_discounts(total_price, total_items, customer_type):
    if customer_type == 'vip':
        total_price *= 0.9  # 10% discount for VIP
    elif customer_type == 'wholesale':
        total_price *= 0.8  # 20% discount for Wholesale

    # Apply bulk order discount
    if total_items > 100:
        total_price *= 0.95  # 5% discount for orders with more than 100 items

    return total_price

def print_results(total_price, total_items):
    print(f"Total items: {total_items}")
    print(f"Total price: {total_price:.2f}")

def process_orders(orders):
    grand_total_price = 0
    grand_total_items = 0
    for order in orders:
        items = order.get('items', [])
        customer_type = order.get('customer_type', 'regular')

        total_price, total_items = calculate_order_total(items)
        total_price = apply_discounts(total_price, total_items, customer_type)

        grand_total_price += total_price
        grand_total_items += total_items

    print_results(grand_total_price, grand_total_items)

# Test data
orders = [
    {'customer_type': 'regular', 'items': [{'price': 10, 'quantity': 2}, {'price': 5, 'quantity': 3}]},
    {'customer_type': 'vip', 'items': [{'price': 20, 'quantity': 5}, {'price': 15, 'quantity': 1}]},
    {'customer_type': 'wholesale', 'items': [{'price': 30, 'quantity': 10}, {'price': 25, 'quantity': 20}]},
]

process_orders(orders)
