from datetime import datetime
import random
import re

def get_days_from_today(date):
    now = datetime.today().date()
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f"date {date} must be in format year-month-day")
        return 0
    days_from_today = now - date_obj
    return days_from_today

print(get_days_from_today("2025-04-6"))

def get_numbers_ticket(min, max, quantity):
    if min < 1 or min >= max or max > 1000 or quantity < min or quantity > max:
        return []
    numbers = []
    while len(numbers) < quantity:
        number = random.randint(min, max)
        if number not in numbers:
            numbers.append(number)
            numbers.sort()
    return numbers

# print(get_numbers_ticket(1, 49, 6))

def normalize_phone(phone_number):
    pattern = r"[\\t\s\-\(\)\\n]"
    replacement = ""
    out_number = re.sub(pattern, replacement, phone_number)
    if out_number.startswith("38"):
        out_number = "+" + out_number
    elif out_number.startswith("0"):
        out_number = "+38" + out_number
    return  out_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
