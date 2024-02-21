import math

def regular_polygon_area(n, s):
    cot_angle = math.cos(math.pi / n) / math.sin(math.pi / n)
    area = math.ceil(0.25 * n * s ** 2 / cot_angle)
    return area

# Пример использования программы
num_sides = int(input("Введите количество сторон многоугольника: "))
side_length = float(input("Введите длину стороны многоугольника: "))

polygon_area = regular_polygon_area(num_sides, side_length)
print("Площадь правильного многоугольника:", polygon_area)