from Crypto.Util.number import getRandomInteger
from Crypto.PublicKey import ECC


def base_point_get():
    # Отримати базову точку G
    curve = ECC.generate(curve='P-256')
    return curve.pointQ

def ec_point_gen(x, y):
    # Створити точку ЕК з координатами (x, y)
    curve = ECC.generate(curve='P-256')
    return curve.point(x, y)

def is_on_curve_check(point):
    # Перевірити, чи належить точка point до кривої
    curve = ECC.generate(curve='P-256')
    return curve.contains(point)

def add_ec_points(a, b):
    # Додати точки a і b на ЕК
    curve = ECC.generate(curve='P-256')
    return a + b

def double_ec_point(a):
    # Подвоїти точку a на ЕК
    curve = ECC.generate(curve='P-256')
    return 2 * a

def scalar_mult(k, a):
    # Помножити точку a на скаляр k
    curve = ECC.generate(curve='P-256')
    return k * a

def ec_point_to_string(point):
    # Перетворити точку в рядок
    return f"{point.x},{point.y}"

def string_to_ec_point(s):
    # Перетворити рядок в точку
    x, y = map(int, s.split(","))
    curve = ECC.generate(curve='P-256')
    return curve.point(x, y)

def print_ec_point(point):
    # Вивести координати точки на ЕК
    print(f"({point.x}, {point.y})")


G = base_point_get()
k = getRandomInteger(256)
d = getRandomInteger(256)

H1 = scalar_mult(d, G)
H2 = scalar_mult(k, H1)

H3 = scalar_mult(k, G)
H4 = scalar_mult(d, H3)

result = H2 == H4

print(result)
