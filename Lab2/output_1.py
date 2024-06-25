class User:
    def __init__(self, name, age, gender, height, weight, scores):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.scores = scores

    def calculate_total_score(self):
        return sum(self.scores)

    def is_adult(self):
        return self.age >= 18

    def get_user_details(self):
        total_score = self.calculate_total_score()
        adult_status = self.is_adult()
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Height": self.height,
            "Weight": self.weight,
            "Total Score": total_score,
            "Adult": adult_status
        }

def print_user_details(details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Приклад виклику функції
user = User("John", 25, "Male", 175, 70, [85, 90, 75, 88, 92])
user_details = user.get_user_details()
print_user_details(user_details)
