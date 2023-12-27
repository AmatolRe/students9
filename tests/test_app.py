import unittest
from unittest.mock import patch
from app import print_students_sorted_by_dob
import io  # Добавляем импорт модуля io

class TestApp(unittest.TestCase):

    @patch('app.data_service.get_students_sorted_by_dob')
    def test_print_students_sorted_by_dob(self, mock_get_sorted):
        mock_get_sorted.return_value = [
            {"name": "Иванов Иван", "dob": "2000-01-02"},
            {"name": "Петров Петр", "dob": "1999-12-31"}
        ]
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            print_students_sorted_by_dob()
            self.assertIn("Иванов Иван\t2000-01-02", fake_out.getvalue())
            self.assertIn("Петров Петр\t1999-12-31", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
