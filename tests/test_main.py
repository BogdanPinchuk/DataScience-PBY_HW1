import unittest

from unittest import TestCase
from apps.main import *

if __name__ == "__main__":
    unittest.main()


class TestRectPerAndArea(TestCase):
    def test_rectangle_per_and_area_positive_int(self):
        actual = rect_per_and_area(1, 1)
        expected = 'Площа = 1.00, Периметр = 4.00'
        self.assertEqual(expected, actual)

    def test_rectangle_per_and_area_positive_float(self):
        actual = rect_per_and_area(1.2, 3.4)
        expected = 'Площа = 4.08, Периметр = 9.20'
        self.assertEqual(expected, actual)

    def test_rectangle_per_and_area_positive_tol3(self):
        actual = rect_per_and_area(1.23, 45.6, 3)
        expected = 'Площа = 56.088, Периметр = 93.660'
        self.assertEqual(expected, actual)

    def test_rectangle_per_and_area_negative(self):
        actual = rect_per_and_area(-1, -1)
        expected = 'Довжина і ширина мають відʼємні значення "-1" і "-1" відповідно!'
        self.assertEqual(expected, actual)

    def test_rectangle_per_and_area_negative_length(self):
        actual = rect_per_and_area(-1, 1)
        expected = 'Довжина має відʼємне значення "-1"!'
        self.assertEqual(expected, actual)

    def test_rectangle_per_and_area_negative_width(self):
        actual = rect_per_and_area(1, -1)
        expected = 'Ширина має відʼємне значення "-1"!'
        self.assertEqual(expected, actual)


class TestCheckNumEvenAndCalcSquare(TestCase):
    def test_check_num_even_and_calc_square_even(self):
        actual = check_num_even_and_calc_square(2)
        expected = 'Число 2 парне? True. Квадрат = 4'
        self.assertEqual(expected, actual)

    def test_check_num_even_and_calc_square_odd(self):
        actual = check_num_even_and_calc_square(3)
        expected = 'Число 3 парне? False. Квадрат = 9'
        self.assertEqual(expected, actual)


class TestCheckNumPositive(TestCase):
    def test_check_num_positive_true(self):
        actual = check_num_positive(1)
        expected = 'Число додатне'
        self.assertEqual(expected, actual)

    def test_check_num_positive_false(self):
        actual = check_num_positive(-1)
        expected = ''
        self.assertEqual(expected, actual)

    def test_check_num_positive_zero(self):
        actual = check_num_positive(0)
        expected = ''
        self.assertEqual(expected, actual)


class TestCompareNumbers(TestCase):
    def test_compare_numbers_1_2(self):
        actual = compare_numbers(1, 2)
        expected = 2
        self.assertEqual(expected, actual)

    def test_compare_numbers_3_2(self):
        actual = compare_numbers(3, 2)
        expected = 3
        self.assertEqual(expected, actual)

    def test_compare_numbers_equal(self):
        actual = compare_numbers(2, 2)
        expected = 2
        self.assertEqual(expected, actual)


class TestAnalyzeKnowledgeLevel(TestCase):
    def test_analyze_knowledge_level_negative(self):
        actual = analyze_knowledge_level(-1)
        expected = 'Невірно введено оцінку студента "-1"!'
        self.assertEqual(expected, actual)

    def test_analyze_knowledge_level_overflow(self):
        actual = analyze_knowledge_level(101)
        expected = 'Невірно введено оцінку студента "101"!'
        self.assertEqual(expected, actual)

    def test_analyze_knowledge_level_50(self):
        actual = analyze_knowledge_level(50)
        expected = 'Незадовільно'
        self.assertEqual(expected, actual)

    def test_analyze_knowledge_level_70(self):
        actual = analyze_knowledge_level(70)
        expected = 'Задовільно'
        self.assertEqual(expected, actual)

    def test_analyze_knowledge_level_80(self):
        actual = analyze_knowledge_level(80)
        expected = 'Добре'
        self.assertEqual(expected, actual)

    def test_analyze_knowledge_level_95(self):
        actual = analyze_knowledge_level(95)
        expected = 'Відмінно'
        self.assertEqual(expected, actual)
