print("Welcome to a centimeter to inch converter")

length_centimeter = eval(input("Enter length in centimeter: "))
if length_centimeter < 0 :
    print("Entry is invalid, try again")
else:
    length_inch = length_centimeter * 2.54
    print("Length in inches is", length_inch)

