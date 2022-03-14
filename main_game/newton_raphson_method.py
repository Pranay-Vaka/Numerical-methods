import math

def newton_raphson_method(function: str, value: float, prev_value: float) -> float:

    h = 10 ** -7

    math_values = {
            "e": math.e,
            "pi": math.pi,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "arcsin": math.asin,
            "arccos": math.acos,
            "arctan": math.atan,
            "log": math.log
            }

    return prev_value - ((eval(function, {"x": value}.update(math_values))) / ((eval(function, {"x": value + h}.update(math_values)) - eval(function, {"x": value}.update(math_values)) / (h))))


newton_raphson_method("2 * x", 2, 1)
