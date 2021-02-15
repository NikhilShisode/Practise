command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)
# while loop
number = 100
print(number // 2)  # int division //
print(number / 2)  # float division /
while number > 0:
    print(number)
    number //= 2

# iterable objects
print(type(range(5)))  # complex type
# string is also iterable
for x in "Python":
    print(x)
# list is also iterable
for x in [1, "a", {"test": True}, True]:
    print(x)


for x in range(5):
    for y in range(3):
        print(f"({x},{y})")


course1 = "pythyon"
print(course1.upper())
print(course1.count("y", 1, -3))

# concatinaition
# formatted string (string literals in js) - f"{expression} text {expression}"
# first = "Mosh"
# last = "Hamedani"
# full = f"{first} {len(first)} {last} {2 + 2}"
# print(full)

# # string literals """ """
# course = "31a\n2b"
# # slice - iterator(start:end+1)
# print("word ", course[:])

# students_count = 1000
# print(students_count)
# 2 + 3
# x = 1
# print("*" * 3)
# y = 2
# unit_price = 3
