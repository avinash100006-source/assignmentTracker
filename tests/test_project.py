import unittest
from datetime import datetime
from input_validator import valid_date
from progress_tracker import show_progress

class TestProject(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(valid_date("2026-09-30"))

    def test_invalid_date(self):
        self.assertFalse(valid_date("30-09-2026"))

    def test_empty_progress(self):
        # The function should run without errors for an empty task list.
        show_progress([])

if __name__ == "__main__":
    unittest.main()
