import json
from data import DataService

# Создаем экземпляр сервиса данных
data_service = DataService('students_data.json')

def print_students_sorted_by_dob():
    students_sorted = data_service.get_students_sorted_by_dob()
    print("ФИО\t\t\tДата Рождения")
    for student in students_sorted:
        print(f"{student['name']}\t{student['dob']}")

def main():
    while True:
        action = input("Введите 'list' для вывода списка студентов, или 'exit' для выхода: ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'list':
            print_students_sorted_by_dob()

if __name__ == "__main__":
    main()
