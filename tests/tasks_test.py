import unittest
from src.tasks import Task
from src.task_decider import get_preferred_option

class TestTask(unittest.TestCase):
    def setUp(self):
        self.wash_dishes = Task("Wash Dishes", 10, ["Do Ironing", "Clean Windows"])
        self.cook_dinner = Task("Cook Dinner", 15, ["Wash Dishes", "Wash Clothes"])
        self.clean_windows = Task("Clean Windows", 20, ["Wash Clothes", "Cook Dinner"])
        self.ironing = Task("Do Ironing", 10, ["Cook Dinner", "Clean Windows"])
        self.wash_clothes = Task("Wash Clothes", 40, ["Do Ironing", "Wash Dishes"])

    def test_task_has_name(self):
        self.assertEqual("Wash Dishes", self.wash_dishes.name)

    def test_task_has_duration(self):
        self.assertEqual(10, self.wash_dishes.duration)

    def test_preferred_task_1(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.wash_dishes, self.cook_dinner))

    def test_preferred_task_2(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.clean_windows,self.wash_dishes))

    # def test_preferred_task_not_work(self):
    #     self.assertEqual("Cook Dinner", get_preferred_option(self.clean_windows,self.wash_dishes))

    def test_preferred_task_3(self):
        self.assertEqual("Clean Windows", get_preferred_option(self.wash_dishes,self.clean_windows))

    def test_preferred_task_4(self):
        self.assertEqual("Do Ironing", get_preferred_option(self.ironing,self.wash_clothes))

    def test_preferred_task_5(self):
        self.assertEqual("Do Ironing", get_preferred_option(self.wash_clothes,self.ironing))
