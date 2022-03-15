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
    
    return prev_value - ((eval(function, math_values, {"x": value})) / ((eval(function, math_values, {"x": value + h})) - eval(function, math_values, {"x": value}) / (h)))
