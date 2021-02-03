# nested loop - 3.10


# for loop else - else will run only when break does not get executed
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# for loop
for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")

# chain comparison operator
# age should be between 18 and 65
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")


# logical operator and or not (short curcuit)
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")


# ternary operator
age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# conditional
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("it's nice")
else:
    print("It's cold")
print("Done")


# input
x = input("x: ")
print(type(x))
y = int(x)+1
print(f"x: {x}, y: {y}")

# type conversion
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy
# ""
# 0
# None
# truthy

# # string
# course = "  Py"
# print(course.strip())
# print(course.find("P"))
# print(course.replace("Py","Python Programming"))
# print("Py" in course)
# print("py" not in course)

# # numbers
# x = 1
# x = 1.1
# x = 1 + 2j # a + bi
# print(x)
# print(11/3)
# print(11%3)
# print(10**3) # 10 to the power 3

# x =10
# x = x+ 3
# x +=3
# print(x)
