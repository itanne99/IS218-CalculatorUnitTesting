def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot Divide by 0"