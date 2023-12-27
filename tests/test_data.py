import unittest
from data import DataService

class TestDataService(unittest.TestCase):

    def setUp(self):
        self.data_service = DataService('test_students_data.json')
        self.data_service.students = [
            {"name": "Иванов Иван", "dob": "2000-01-02"},
            {"name": "Петров Петр", "dob": "1999-12-31"},
            {"name": "Сидоров Сидор", "dob": "2001-06-15"}
        ]

    def test_get_students_sorted_by_dob(self):
        sorted_students = self.data_service.get_students_sorted_by_dob()
        self.assertEqual(sorted_students[0]['name'], "Петров Петр")
        self.assertEqual(sorted_students[1]['name'], "Иванов Иван")
        self.assertEqual(sorted_students[2]['name'], "Сидоров Сидор")

if __name__ == '__main__':
    unittest.main()
