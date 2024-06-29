class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

class ProductSearchService:
    def search_product(self, products, query):
        # Пошук товару за запитом
        results = [product for product in products if query.lower() in product.name.lower()]
        return results

class ProductDisplayService:
    def display_product(self, product):
        # Відображення інформації про товар
        print(f"Name: {product.name}")
        print(f"Price: {product.price}")
        print(f"Type: {product.type}")

class ProductOrderService:
    def order_product(self, product, quantity):
        # Замовлення товару
        print(f"Ordered {quantity} of {product.name}")

# Приклад використання класів
products = [
    Product("Laptop", 1500, "Electronics"),
    Product("Smartphone", 800, "Electronics"),
    Product("Book", 20, "Books")
]

search_service = ProductSearchService()
display_service = ProductDisplayService()
order_service = ProductOrderService()

# Пошук товарів
query = "laptop"
found_products = search_service.search_product(products, query)

# Відображення знайдених товарів
for product in found_products:
    display_service.display_product(product)

# Замовлення товару
if found_products:
    order_service.order_product(found_products[0], 2)
