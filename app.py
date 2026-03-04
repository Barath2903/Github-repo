"""Simple utility module for Git integration assignment."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def power(base, exponent):
    return base ** exponent


if __name__ == "__main__":
    print("5-function utility project initialized")
