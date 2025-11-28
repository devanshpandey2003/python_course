import math


def calculate(number: int) -> None:

    if number < 0:
        number = abs(number)

    print(f" Square root: {math.sqrt(number)}")
    print(f" Logarithm: {math.log(number)}")
    print(f" Sine: {math.sin(number)}")


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    calculate(num)
