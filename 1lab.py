from Crypto.Util.number import getRandomInteger
from Crypto.PublicKey import ECC


def base_point_get():
    # Отримайте базову точку G
    curve = ECC.generate(curve='P-256')
    return curve.pointQ


def scalar_mult(k, a):
    # Помножте точку a на скаляр k
    curve = ECC.generate(curve='P-256')
    return k * a


def check_equation():
    G = base_point_get()
    k = getRandomInteger(256)
    d = getRandomInteger(256)

    H1 = scalar_mult(d, G)
    H2 = scalar_mult(k, H1)

    H3 = scalar_mult(k, G)
    H4 = scalar_mult(d, H3)

    result = H2 == H4

    return result


# Виконайте перевірку рівняння
equation_result = check_equation()
print("Equation Result:", equation_result)
