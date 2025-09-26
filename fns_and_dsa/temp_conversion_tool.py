FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()  # Stop the program if input is invalid

celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
    
def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return fahrenheit

if celsius_or_fahrenheit == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif celsius_or_fahrenheit == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")