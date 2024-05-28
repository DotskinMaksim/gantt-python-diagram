import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# Данные для диаграммы Ганта
tasks = [
    {"name": "Итерация 1: Анализ требований и прототипирование", "start": "2024-06-01", "end": "2024-06-14"},
    {"name": "Итерация 2: Разработка модуля сбора данных", "start": "2024-06-15", "end": "2024-06-28"},
    {"name": "Итерация 3: Создание системы мониторинга в реальном времени", "start": "2024-06-29", "end": "2024-07-12"},
    {"name": "Итерация 4: Разработка модуля управления запасами", "start": "2024-07-13", "end": "2024-07-26"},
    {"name": "Итерация 5: Разработка системы планирования логистики", "start": "2024-07-27", "end": "2024-08-09"},
    {"name": "Итерация 6: Создание модуля безопасности и контроля", "start": "2024-08-10", "end": "2024-08-23"},
    {"name": "Итерация 7: Интеграция модулей и тестирование", "start": "2024-08-24", "end": "2024-09-06"},
    {"name": "Итерация 8: Финальные улучшения и подготовка к запуску", "start": "2024-09-07", "end": "2024-09-20"}
]

# Преобразование дат в формат datetime
for task in tasks:
    task["start"] = datetime.datetime.strptime(task["start"], "%Y-%m-%d")
    task["end"] = datetime.datetime.strptime(task["end"], "%Y-%m-%d")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))

# Добавление задач на диаграмму
for i, task in enumerate(tasks):
    ax.barh(task["name"], (task["end"] - task["start"]).days, left=task["start"], color='skyblue')

# Настройка осей
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.xticks(rotation=45)

# Добавление меток и заголовков
plt.xlabel('Дата')
plt.ylabel('Задачи')
plt.title('Диаграмма Ганта для проекта разработки ПО')

plt.tight_layout()
plt.show()
