class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None

# Приклад використання класу
data = [1, 2, 3, 4, 5]
analyzer = DataAnalyzer(data)
print("Total:", analyzer.calculate_total())
print("Average:", analyzer.calculate_average())
print("Minimum:", analyzer.calculate_minimum())
print("Maximum:", analyzer.calculate_maximum())
