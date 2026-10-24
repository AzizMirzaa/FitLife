# Проект FitLife - MVP версия 1.0

import sys

sys.stdout.reconfigure(encoding="utf-8")

WATER_NORM = 30
ML_IN_LITR = 1000

# 1. Знакомство

user_name = input("Как вас зовут?\n").strip()
user_name = user_name.title()

# Сбор данных

while True:
    try:
        user_age = int(input("Сколько вам лет?\n"))

        user_weight = float(
            input("Напишите ваш вес, пожалуйста."
                  "(Пример: 74.3 или без точки 70)\n"))
        user_height = float(
            input("Ваш рост, пожалуйста."
                  "В метрах, например: 1.75\n"))
        break
    except ValueError:
        print("Ошибка! Проверьте правильность введённых данных.")

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)

# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл

water_needed_ml = user_weight * WATER_NORM

# Переводим в литры:
water_needed_litres = water_needed_ml / ML_IN_LITR

# 4. Вывод красивого результата

print(f"Здравствуйте, {user_name}")

print(f"Ваш индекс массы тела: {bmi}")

print(f"Рекомендуемая норма воды: {water_needed_litres}")

print("Расчет окончен. Будьте здоровы!")
