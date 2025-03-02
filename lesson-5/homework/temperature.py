def convert_cel_to_far(c):
    print(f"{c} degrees C = {c * 9/5 +32:.2f} degrees F")


def convert_far_to_cel(f):
    first = f - 32
    print(f"{f} degrees F = {first * 5/9:.2f} degrees C")


celsius = int(input("Enter a temperature in degrees C: "))
convert_far_to_cel(celsius)

fahrenheit = int(input("Enter a temperature in degrees F: "))
convert_cel_to_far(fahrenheit)