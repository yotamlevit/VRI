

def quadratic_equation(a, b, c):
    """

    """
    d = (b**2) - (4*a*c)
    return (-b - d ** 0.5) / (a * 2), (-b + d ** 0.5) / (a * 2) if d >= 0 else (None, None)