print("Welcome a temperature converter")

temp = eval(input("Enter temperature number: "))
unit = input("Enter unit, celsius or fahrenheit: ")

if "celsius" in unit:
    temp_fehrenheit = temp + 32
    print("Temperature in Fahrenheit is", temp_fehrenheit)
elif "fahrenheit" in unit:
    temp_celsius = temp - 32
    print("Temperature in celsius is", temp_celsius)
else:
    print("Invalid unit")
