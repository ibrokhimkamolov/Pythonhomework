import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

fahrenheit_array = np.array([32, 68, 100, 212, 77])

celsius_array = vectorized_conversion(fahrenheit_array)

print("Temperatures in Celsius:", celsius_array)
