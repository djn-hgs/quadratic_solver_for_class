import math

def calc_discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c

def solve_quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    D = calc_discriminant(a, b, c)
    if D < 0:
        raise ValueError("The discriminant cannot be negative")

    solution1 = (-b - math.sqrt(D)) / (2 * a)
    solution2 = (-b + math.sqrt(D)) / (2 * a)
    return solution1, solution2



