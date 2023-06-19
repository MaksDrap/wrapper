class ECPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def base_point_get():
    # Отримати базову точку G
    # Реалізуйте відповідний код
    return ECPoint(x, y)

def ec_point_gen(x, y):
    # Створити точку ЕК з координатами (x, y)
    # Реалізуйте відповідний код
    return ECPoint(x, y)

def is_on_curve_check(point):
    # Перевірити, чи належить точка point до кривої
    # Реалізуйте відповідний код
    return is_on_curve

def add_ec_points(a, b):
    # Додати точки a і b на ЕК
    # Реалізуйте відповідний код
    return c

def double_ec_point(a):
    # Подвоїти точку a на ЕК
    # Реалізуйте відповідний код
    return c

def scalar_mult(k, a):
    # Помножити точку a на скаляр k
    # Реалізуйте відповідний код
    return c

def ec_point_to_string(point):
    # Перетворити точку в рядок
    # Реалізуйте відповідний код
    return s

def string_to_ec_point(s):
    # Перетворити рядок в точку
    # Реалізуйте відповідний код
    return point

def print_ec_point(point):
    # Вивести координати точки на ЕК
    # Реалізуйте відповідний код
    print(f"({point.x}, {point.y})")


G = base_point_get()
k = SetRandom(256)
d = SetRandom(256)

H1 = scalar_mult(d, G)
H2 = scalar_mult(k, H1)

H3 = scalar_mult(k, G)
H4 = scalar_mult(d, H3)

result = H2 == H4

print(result)
