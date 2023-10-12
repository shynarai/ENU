from datetime import datetime

def days_until_date(day, month):
    # Получаем текущую дату
    today = datetime.today()
    
    # Формируем дату в текущем году с указанным днем и месяцем
    target_date = datetime(today.year, month, day)
    
    # Если дата еще не наступила в текущем году
    if target_date > today:
        days_until = (target_date - today).days
        return f"До указанной даты осталось {days_until} дней"
    else:
        next_year_target_date = datetime(today.year + 1, month, day)
        days_until = (next_year_target_date - today).days
        return f"До указанной даты следующего года осталось {days_until} дней"

# Пример использования:
result = days_until_date(25, 12)  # До Рождества осталось (или уже прошло) несколько дней
print(result)
