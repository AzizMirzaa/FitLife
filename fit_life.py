# Проект FitLife - MVP версия 1.0

# 1. Знакомство

user_name = input("Как вас зовут?\n")
user_name = user_name.title()
user_age = input("Сколько вам лет?\n")
user_age_int = int(user_age)

# 2. Сбор данных

user_weight = input("Напишите ваш вес, пожалуйста:\n")
user_weight_float = float(user_weight)


user_height = input("Ваш рост, пожалуйста, в метрах, например: 1.75\n")

user_height_float = float(user_height)


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)

# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight_float / (user_height_float ** 2)

round(bmi, 1)
truncated_bmi = int(bmi * 10) / 10

# Подсчет воды: вес * 30 мл

water_needed_ml = user_weight_float * 30

# Переводим в литры:
water_needed_litres = water_needed_ml / 1000

# 4. Вывод красивого результата

print(f"Здравствуйте, {user_name}")

print(f"Ваш индекс массы тела: {truncated_bmi:.1f}")
# Я уточнил у ИИ, как убрать оставшиеся цифры,

# Чтобы вместо 22.38595995559559 отображалось 22.3

print(f"Рекомендуемая норма воды: {water_needed_litres}")

print("Расчет окончен. Будьте здоровы!")
