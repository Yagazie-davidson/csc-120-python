print("Welcome")
temperature = eval(input("Enter temperature in celsius: "))
if temperature < -273.15:
    print("Temperature is invalid because it is below absolute zero")
elif temperature == -273.15:
    print("Temperature is absolute zero")
elif temperature > -273.15 and temperature < 0:
    print("Temperature is below freezing")
elif temperature == 0:
    print("Temperature is at freezing point")
elif temperature > 0 and temperature < 100:
    print("Temperature is in the normal range")
elif temperature == 100:
    print("Temperature is at boiling point")
elif temperature > 100:
    print("Temperature is above boiling point")