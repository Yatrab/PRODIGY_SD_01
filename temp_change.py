def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

while True:
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    print("4. Quit")
    choice = input("Select conversion type (1/2/3/4): ")

    if choice == '4':
        break

    try:
        temperature = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")
        continue

    if choice == '1':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{temperature} Celsius is equal to {fahrenheit} Fahrenheit and {kelvin} Kelvin")
    elif choice == '2':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{temperature} Fahrenheit is equal to {celsius} Celsius and {kelvin} Kelvin")
    elif choice == '3':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{temperature} Kelvin is equal to {celsius} Celsius and {fahrenheit} Fahrenheit")
    else:
        print("Invalid choice. Please select a valid option.")