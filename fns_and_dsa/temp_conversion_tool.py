FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit) :
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius) :
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("=== Temperature Converter ===")

    temp = input('Enter the temprature : ').strip()
    type = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        temprature = float(temp)
    except ValueError:
         raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    if type == 'C':
        result = convert_to_fahrenheit(temprature)
        print(f"{temprature}°C is equal to {result:.2f}°F")

    elif unit == "F":
        result = convert_to_celsius(temprature)
        print(f"{temprature}°F is equal to {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()