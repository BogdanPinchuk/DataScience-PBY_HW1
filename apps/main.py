# Task 1
def rect_per_and_area(length, width, tolerance=2):
    if length < 0.0 and width < 0.0:
        result = f"Довжина і ширина мають відʼємні значення \"{length}\" і \"{width}\" відповідно!"
    elif length < 0.0:
        result = f"Довжина має відʼємне значення \"{length}\"!"
    elif width < 0.0:
        result = f"Ширина має відʼємне значення \"{width}\"!"
    else:
        perimeter = 2 * (length + width)
        area = length * width
        result = f"Площа = {area:.{tolerance}f}, Периметр = {perimeter:.{tolerance}f}"
    return result


# Task 2
def check_num_even_and_calc_square(number):
    even_number = number % 2 == 0
    square_number = number ** 2
    result = f"Число {number} парне? {even_number}. Квадрат = {square_number}"
    return result


# Task 3
def check_num_positive(number):
    return "Число додатне" if number > 0 else ""


# Task 4
def compare_numbers(number1, number2):
    return number1 if number1 > number2 else number2


# Task 5
def analyze_knowledge_level(grade):
    if grade < 0 or grade > 100:
        result = f"Невірно введено оцінку студента \"{grade}\"!"
    elif grade < 60:
        result = "Незадовільно"
    elif grade <= 74:
        result = "Задовільно"
    elif grade <= 89:
        result = "Добре"
    else:
        result = "Відмінно"
    return result
