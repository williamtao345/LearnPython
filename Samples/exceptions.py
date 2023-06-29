try:
    age = int(input("Age: "))
    risk = 1000/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")
