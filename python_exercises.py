"""Beginner Python exercises 1-15.

Run this file and select an exercise number.  Each exercise is isolated in a
function so importing this module does not unexpectedly read from stdin.
"""

import math


def exercise_1():
    a, b = map(float, input().split())
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    if b != 0:
        print("Quotient:", a / b)
        print("Remainder:", a % b)
    else:
        print("Division by zero is not allowed")


def exercise_2():
    radius = float(input())
    print(math.pi * radius * radius)


def exercise_3():
    principal, rate, time = map(float, input().split())
    print((principal * rate * time) / 100)


def exercise_4():
    choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ").upper()
    temperature = float(input())
    if choice == "C":
        print((temperature * 9 / 5) + 32)
    elif choice == "F":
        print((temperature - 32) * 5 / 9)
    else:
        print("Invalid choice")


def exercise_5():
    number = int(input())
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by 3")
    elif number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Neither")


def exercise_6():
    a, b = map(int, input().split())
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Equal")


def exercise_7():
    number = int(input())
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


def exercise_8():
    a, b, c = map(int, input().split())
    print("All are equal" if a == b == c else "Not all equal")


def exercise_9():
    print("Eligible to vote" if int(input()) >= 18 else "Not eligible to vote")


def exercise_10():
    character = input()[0]
    if character.isupper():
        print("Uppercase")
    elif character.islower():
        print("Lowercase")
    elif character.isdigit():
        print("Digit")
    else:
        print("Special character")


def exercise_11():
    print("Odd" if int(input()) & 1 else "Even")


def exercise_12():
    a, b = map(int, input().split())
    a ^= b
    b ^= a
    a ^= b
    print(a, b)


def exercise_13():
    number = int(input())
    print("n << 1 =", number << 1)
    print("n >> 1 =", number >> 1)


def exercise_14():
    number, bit = map(int, input().split())
    print("Set" if number & (1 << bit) else "Not set")


def exercise_15():
    print(bin(int(input())).count("1"))


EXERCISES = {
    1: exercise_1,
    2: exercise_2,
    3: exercise_3,
    4: exercise_4,
    5: exercise_5,
    6: exercise_6,
    7: exercise_7,
    8: exercise_8,
    9: exercise_9,
    10: exercise_10,
    11: exercise_11,
    12: exercise_12,
    13: exercise_13,
    14: exercise_14,
    15: exercise_15,
}


if __name__ == "__main__":
    try:
        selected = int(input("Choose an exercise (1-15): "))
        EXERCISES[selected]()
    except (ValueError, KeyError):
        print("Please choose a valid exercise number from 1 to 15.")
