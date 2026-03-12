def build_country_coords(countries, capitals, coords):
    country_to_coords = {}
    for i in range(len(countries)):
        country = countries[i]
        lat, lon = coords[i]
        lat = float(lat)
        lon = float(lon)
        country_to_coords[country] = (lat, lon)
    return country_to_coords


countries = ["Россия", "Франция", "Германия", "Италия"]
capitals = ["Москва", "Париж", "Берлин", "Рим"]
coords = [
    ("55.7558", "37.6176"),
    ("48.8566", "2.3522"),
    ("52.5200", "13.4050"),
    ("41.9028", "12.4964")
]

result = build_country_coords(countries, capitals, coords)

print("Результат:")
for country, coord in result.items():
    print(f"{country}: {coord}")

def tests():
    print("\nЗапуск тестов...")

assert result["Германия"] == (52.5200, 13.4050), "Ошибка: неверные координаты для Германии"
assert result["Италия"] == (41.9028, 12.4964), "Ошибка: неверные координаты для Италии"

countries1 = ["Россия", "Франция"]
capitals1 = ["Москва", "Париж"]
coords1 = [("55.7558", "37.6176"), ("48.8566", "2.3522")]
result1 = build_country_coords(countries1, capitals1, coords1)
expected1 = {"Россия": (55.7558, 37.6176), "Франция": (48.8566, 2.3522)}
assert result1 == expected1, "Ошибка в тесте 2"

print("Все тесты пройдены!")