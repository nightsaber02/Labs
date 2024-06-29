class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    # Геттери
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def price(self):
        return self.__price

    # Сеттери з валідацією
    @product_id.setter
    def product_id(self, value):
        self.__validate_product_id(value)
        self.__product_id = value

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @category.setter
    def category(self, value):
        self.__validate_category(value)
        self.__category = value

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    # Приватні методи валідації
    def __validate_product_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Invalid product ID")

    def __validate_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Invalid product name")

    def __validate_category(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Invalid product category")

    def __validate_price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Invalid product price")
