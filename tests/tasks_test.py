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