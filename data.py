import json

class DataService:
    def __init__(self, data_file):
        self.data_file = data_file
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student_data):
        self.students.append(student_data)
        self.save_data()

    def get_students(self):
        return self.students
    
    def get_students_sorted_by_dob(self):
        return sorted(self.students, key=lambda x: x['dob'])

# Если data.py запускается как скрипт, он может предоставить тестовые данные
if __name__ == "__main__":
    # Инициализация сервиса данных с тестовыми данными
    data_service = DataService('test_students_data.json')