import datetime

# Цифры в формате «электронного табло» (7 строк, ширина — 5 символов)
DIGIT_PATTERNS = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "*****"
    ],
    '2': [
        " *** ",
        "*   *",
        "    *",
        "  ** ",
        " *   ",
        "*    ",
        "*****"
    ],
    '3': [
        " *** ",
        "*   *",
        "    *",
        "  ** ",
        "    *",
        "*   *",
        " *** "
    ],
    '4': [
        "   * ",
        "  ** ",
        " * * ",
        "*  * ",
        "*****",
        "   * ",
        "   * "
    ],
    '5': [
        "*****",
        "*    ",
        "*    ",
        " ****",
        "    *",
        "*   *",
        " *** "
    ],
    '6': [
        " *** ",
        "*   *",
        "*    ",
        "**** ",
        "*   *",
        "*   *",
        " *** "
    ],
    '7': [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   ",
        "*    ",
        "*    "
    ],
    '8': [
        " *** ",
        "*   *",
        "*   *",
        " *** ",
        "*   *",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        " *** "
    ]
}

def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_age(birth_year, birth_month, birth_day):
    """Вычисляет возраст пользователя на текущий момент."""
    today = datetime.date.today()
    age = today.year - birth_year
    # Корректировка, если день рождения ещё не наступил в текущем году
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age

def get_weekday(day, month, year):
    """Возвращает день недели для заданной даты."""
    date = datetime.date(year, month, day)
    weekdays = [
        "Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"
    ]
    return weekdays[date.weekday()]

def print_date_as_stars(day, month, year):
    """Выводит дату в формате дд мм гггг, где цифры нарисованы звёздочками."""
    # Форматируем дату: день и месяц — 2 цифры, год — 4 цифры
    date_str = f"{day:02d}{month:02d}{year:04d}"
    # Разделяем каждую цифру
    digits = [d for d in date_str]
    # Получаем шаблоны для каждой цифры
    lines = [''] * 7
    for digit in digits:
        pattern = DIGIT_PATTERNS[digit]
        for i in range(7):
            lines[i] += pattern[i] + " "  # Добавляем пробел между цифрами
    # Выводим результат
    print("Дата рождения (в стиле электронного табло):")
    for line in lines:
        print(line)

def main():
    print("Программа для обработки даты рождения")
    print("-" * 40)
    try:
        day = int(input("Введите день рождения: "))
        month = int(input("Введите месяц рождения: "))
        year = int(input("Введите год рождения: "))

        # Проверка корректности даты
        try:
            datetime.date(year, month, day)
        except ValueError:
            print("Ошибка: введена некорректная дата!")
            return

        # Вызов функций
        weekday = get_weekday(day, month, year)
        leap = is_leap_year(year)
        age = get_age(year, month, day)

        # Вывод результатов
        print("\nРезультаты:")
        print(f"День недели: {weekday}")
        print(f"Год {'високосный' if leap else 'не високосный'}")
        print(f"Возраст: {age} лет")

        print_date_as_stars(day, month, year)

    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа!")

if __name__ == "__main__":
    main()
