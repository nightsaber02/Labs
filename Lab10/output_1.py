class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Використання базового калькулятора
calculator = BasicCalculator()
print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))

# Використання розширеного калькулятора
advanced_calculator = AdvancedCalculator()
print("Multiplication:", advanced_calculator.multiply(5, 3))
print("Division:", advanced_calculator.divide(5, 3))
