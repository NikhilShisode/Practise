# 4.8


def save_user(**user):
    print(user)


save_user(id=1, name="Nikhil", age=23)


def increment(number, by=1):  # default value
    return number + by


print(increment(number=2, by=4))  # keyword argument


def multiply(*numbers):
    print(type(numbers))
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome!")


def get_greeting(name):
    return f"hi {name}"


message = get_greeting("Nikhil")
file = open("content.txt", "w")
file.write(message)

# greet("Nikhil")

# 1 - perform a task
# 2 - return a value
