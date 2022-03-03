import unittest
from src.tasks import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.wash_dishes = Task("Wash Dishes", 10)
        self.cook_dinner = Task("Cook Dinner", 15)
        self.clean_windows = Task("Clean Windows", 20)

    def test_task_has_name(self):
        self.assertEqual("Wash Dishes", self.wash_dishes.name)

    def test_task_has_duration(self):
        self.assertEqual(10, self.wash_dishes.duration)

    def test_preferred_task_1(self):
        self.assertEqual("Clean Windows", self.wash_dishes.get_preferred_option(self.wash_dishes))

    def test_preferred_task_2(self):
        self.assertEqual("Cook Dinner", self.clean_windows.get_preferred_option(self.clean_windows))