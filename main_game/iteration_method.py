import math

def iteration_method(function: str, value: float) -> float:

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
    
    return eval(function, math_values)

