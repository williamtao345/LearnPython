def say_hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    print("Welcome aboard.")


say_hello("William", "Tao")
say_hello(first_name="William", last_name="Tao")


# Calculates and returns the square of a number
def square(number):
    return number * number


print(square(2))
