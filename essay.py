from datetime import datetime

def days_until_target(target_date):
    # Определяем текущую дату
    current_date = datetime.today()

    # Рассчитываем разницу в днях
    days_difference = abs((target_date - current_date).days)

    return days_difference

# Пример использования
target_date = datetime(2023, 12, 31)  # Заданная дата
days_left = days_until_target(target_date)

if target_date > datetime.today():
    print(f"До заданной даты осталось {days_left} дней.")
else:
    print(f"От заданной даты прошло {days_left} дней.")
