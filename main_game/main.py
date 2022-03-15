from newton_raphson_method import newton_raphson_method
from iteration_method import iteration_method

"""
def user_decision():
    while True:
        user_input = input("You want to use the newton raphson method (type in '1') or iteration (type in '2')")
        if user_input == "1":
            print("Ok, newton raphson method it is!")
            while True:
                user_function = input("What is the functio")
            newton_raphson()
            break
        elif user_input == "2":
            print("Ok, iteration method it is!")
            iteration()
            break
        else:
            print("Wrong input!")
            print("You can only input 1 for newton raphson method and 2 for iteration")
"""


def newton_raphson(function: str, initial_guess: float):
    value = initial_guess
    prev_value = initial_guess

    for i in range(10000):
        value = newton_raphson_method(function, value, prev_value)
        print(value)
        
        if float("%.3g" % prev_value) == float("%.3g" % value):
            break

        else:
            prev_value = value

    print(float("%.3g" % value))


def iteration():
    pass


newton_raphson("((2 * x) ** 1/2) + (x ** (-1/2)) - 5", 5)
