def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    finally:
        return f"The result of the division is: {result}"

total = safe_divide(10, 0)
print(total)
