from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
import random

def days_until_date_random_forest():
    # Генерация синтетических данных
    random.seed(42)  # Для воспроизводимости результатов
    data = []

    for _ in range(1000):
        current_month = random.randint(1, 12)
        target_month = random.randint(current_month, 12)
        current_day = random.randint(1, 31)
        target_day = random.randint(current_day, 31)
        data.append((current_month, current_day, target_month, target_day))
    
    X = [(current_month, current_day, target_month) for current_month, current_day, target_month, _ in data]
    y = [target_day - current_day for _, current_day, _, target_day in data]

    # Обучение модели случайного леса
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Предсказание
    current_month, current_day, target_month = datetime.today().month, datetime.today().day, 12
    prediction = model.predict([[current_month, current_day, target_month]])[0]
    
    if prediction > 0:
        return f"До указанной даты осталось примерно {int(prediction)} дней"
    else:
        return f"Указанная дата уже прошла примерно {-int(prediction)} дней назад"

# Пример использования:
result = days_until_date_random_forest()
print(result)
