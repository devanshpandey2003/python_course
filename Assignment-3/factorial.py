def factorial(n: int) -> int:
    """
    calculate factorial of a non-negative number
    :param n: non-negative integer

    """
    if n <= 0:
        return -1
    if n == 1:
        return n

    return n * factorial(n - 1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Factorial is only defined for non-negative integer.")
    else:
        print(f"Factorial of {num} if {factorial(num)}")
