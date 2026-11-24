# Подключаем модуль math для извлечения квадратного корня
import math


# Функция ввода: запрашивает коэффициенты и возвращает их
def read_coefficients():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    return a, b, c


# Функция расчёта: находит корни уравнения ax² + bx + c = 0
def solve(a, b, c):
    # Считаем дискриминант
    d = b ** 2 - 4 * a * c
    # Если дискриминант отрицательный, действительных корней нет
    if d < 0:
        return None
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2


# Процедура вывода: печатает результат на экран
def show_roots(roots):
    if roots is None:
        print("Действительных корней нет")
    else:
        print("x1 =", roots[0])
        print("x2 =", roots[1])


# Основная часть программы
a, b, c = read_coefficients()
if a == 0:
    print("Коэффициент a не может быть равен 0")
else:
    show_roots(solve(a, b, c))