import os
import csv

# Получаем путь к текущей директории, где находится скрипт
current_directory = os.path.dirname(os.path.abspath(__file__))

# Строим путь к файлу относительно текущей директории
file_path = os.path.join(current_directory, 'data.csv')

# Два словаря для хранения данных по каждому году
data_2021 = {}
data_2022 = {}

# Открытие и чтение CSV-файла
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Получаем заголовки (например, "Country", "2021", "2022")

    # Чтение и распределение данных по словарям
    for row in reader:
        country = row[1].strip()  # Извлекаем страну и убираем пробелы

        # Извлекаем значения для 2021 и 2022 годов
        try:
            value_2021 = row[2].strip()
            value_2022 = row[3].strip()

            # Проверяем, что данные не пустые или некорректные
            if value_2021 not in ['SAS', '..']:  # Пропускаем ненужные данные
                if country not in data_2021:
                    data_2021[country] = {}
                data_2021[country][row[0]] = value_2021  # Добавляем показатель и его значение

            if value_2022 not in ['SAS', '..']:  # Пропускаем ненужные данные
                if country not in data_2022:
                    data_2022[country] = {}
                data_2022[country][row[0]] = value_2022  # Добавляем показатель и его значение

        except ValueError:
            continue  # Пропускаем строки с ошибками в данных

# Выводим все данные за 2021 год
print("\nВсе данные за 2021 год:")
for country, indicators in data_2021.items():
    print(f"{country}: {indicators}")

# Выводим все данные за 2022 год
print("\nВсе данные за 2022 год:")
for country, indicators in data_2022.items():
    print(f"{country}: {indicators}")

# Нахождение максимума и минимума по иммунизации за 2021 год
max_bcg_2021_value = -1  # Начальное значение для поиска максимума
min_bcg_2021_value = float('inf')  # Начальное значение для поиска минимума
max_bcg_2021_country = ""
min_bcg_2021_country = ""

# Проходим по всем странам в data_2021
for country in data_2021:
    value = data_2021[country].get("Immunization, BCG (% of one-year-old children)", None)

    # Если значение есть и оно корректное
    if value:
        value = float(value)  # Преобразуем значение в число

        # Проверка на максимальное значение
        if value > max_bcg_2021_value:
            max_bcg_2021_value = value
            max_bcg_2021_country = country

        # Проверка на минимальное значение
        if value < min_bcg_2021_value:
            min_bcg_2021_value = value
            min_bcg_2021_country = country

# Нахождение максимума и минимума по иммунизации за 2022 год
max_bcg_2022_value = -1  # Начальное значение для поиска максимума
min_bcg_2022_value = float('inf')  # Начальное значение для поиска минимума
max_bcg_2022_country = ""
min_bcg_2022_country = ""

# Проходим по всем странам в data_2022
for country in data_2022:
    value = data_2022[country].get("Immunization, BCG (% of one-year-old children)", None)

    # Если значение есть и оно корректное
    if value:
        value = float(value)  # Преобразуем значение в число

        # Проверка на максимальное значение
        if value > max_bcg_2022_value:
            max_bcg_2022_value = value
            max_bcg_2022_country = country

        # Проверка на минимальное значение
        if value < min_bcg_2022_value:
            min_bcg_2022_value = value
            min_bcg_2022_country = country

# Выводим результаты
print(f"Максимум по иммунизации BCG за 2021 год: {max_bcg_2021_country} с значением {max_bcg_2021_value}")
print(f"Минимум по иммунизации BCG за 2021 год: {min_bcg_2021_country} с значением {min_bcg_2021_value}")

print(f"Максимум по иммунизации BCG за 2022 год: {max_bcg_2022_country} с значением {max_bcg_2022_value}")
print(f"Минимум по иммунизации BCG за 2022 год: {min_bcg_2022_country} с значением {min_bcg_2022_value}")

# Выводим результаты по максимальному и минимальному значению по иммунизации
print(
    f"\nМаксимум по иммунизации BCG за 2021 год: {max_bcg_2021_country} с значением {data_2021[max_bcg_2021_country].get('Immunization, BCG (% of one-year-old children)', 0)}")
print(
    f"Минимум по иммунизации BCG за 2021 год: {min_bcg_2021_country} с значением {data_2021[min_bcg_2021_country].get('Immunization, BCG (% of one-year-old children)', 0)}")

print(
    f"\nМаксимум по иммунизации BCG за 2022 год: {max_bcg_2022_country} с значением {data_2022[max_bcg_2022_country].get('Immunization, BCG (% of one-year-old children)', 0)}")
print(
    f"Минимум по иммунизации BCG за 2022 год: {min_bcg_2022_country} с значением {data_2022[min_bcg_2022_country].get('Immunization, BCG (% of one-year-old children)', 0)}")

# Рейтинг по смертности от туберкулеза

# Сортируем данные по смертности от туберкулеза за 2021 год
data_2021_death_rate = {country: float(data_2021[country].get("Tuberculosis death rate (per 100,000 people)", 0))
                        for country in data_2021}
sorted_2021_death_rate = sorted(data_2021_death_rate.items(), key=lambda x: x[1], reverse=True)

# Сортируем данные по смертности от туберкулеза за 2022 год
data_2022_death_rate = {country: float(data_2022[country].get("Tuberculosis death rate (per 100,000 people)", 0))
                        for country in data_2022}
sorted_2022_death_rate = sorted(data_2022_death_rate.items(), key=lambda x: x[1], reverse=True)

# Выводим рейтинг по смертности за 2021 год
print("\nРейтинг по смертности от туберкулеза за 2021 год:")
for rank, (country, death_rate) in enumerate(sorted_2021_death_rate, 1):
    print(f"{rank}. {country}: {death_rate} случаев на 100,000 людей")

# Выводим рейтинг по смертности за 2022 год
print("\nРейтинг по смертности от туберкулеза за 2022 год:")
for rank, (country, death_rate) in enumerate(sorted_2022_death_rate, 1):
    print(f"{rank}. {country}: {death_rate} случаев на 100,000 людей")

# Расчет средних значений по обнаружению случаев туберкулеза
print("\n" + "="*60)
print("СРЕДНИЕ ЗНАЧЕНИЯ ПО УРОВНЮ ОБНАРУЖЕНИЯ СЛУЧАЕВ ТУБЕРКУЛЕЗА")
print("="*60)

# Собираем данные по обнаружению случаев туберкулеза за 2021 год
detection_2021_values = []
for country in data_2021:
    value = data_2021[country].get("Tuberculosis case detection rate (%, all forms)", None)
    if value:
        try:
            detection_2021_values.append(float(value))
        except ValueError:
            continue

# Собираем данные по обнаружению случаев туберкулеза за 2022 год
detection_2022_values = []
for country in data_2022:
    value = data_2022[country].get("Tuberculosis case detection rate (%, all forms)", None)
    if value:
        try:
            detection_2022_values.append(float(value))
        except ValueError:
            continue

# Вычисляем и выводим средние значения
if detection_2021_values:
    avg_2021 = sum(detection_2021_values) / len(detection_2021_values)
    print(f"Среднее значение за 2021 год: {avg_2021:.1f}%")
else:
    print("Нет данных по обнаружению случаев туберкулеза за 2021 год")

if detection_2022_values:
    avg_2022 = sum(detection_2022_values) / len(detection_2022_values)
    print(f"Среднее значение за 2022 год: {avg_2022:.1f}%")
else:
    print("Нет данных по обнаружению случаев туберкулеза за 2022 год")

# Анализ изменений по успешности лечения
print("\n" + "="*60)
print("ИЗМЕНЕНИЯ ПО ПОКАЗАТЕЛЮ УСПЕШНОСТИ ЛЕЧЕНИЯ (2021 → 2022)")
print("="*60)

# Собираем и сравниваем данные по успешности лечения
for country in data_2021:
    if country in data_2022:
        value_2021 = data_2021[country].get("Tuberculosis treatment success rate (% of new cases)", None)
        value_2022 = data_2022[country].get("Tuberculosis treatment success rate (% of new cases)", None)
        
        if value_2021 and value_2022:
            try:
                val_2021_float = float(value_2021)
                val_2022_float = float(value_2022)
                change = val_2022_float - val_2021_float
                trend = "↑ рост" if change > 0 else "↓ снижение" if change < 0 else "→ без изменений"
                print(f"{country}: {val_2021_float}% → {val_2022_float}% ({change:+.1f}%) {trend}")
            except ValueError:
                continue
