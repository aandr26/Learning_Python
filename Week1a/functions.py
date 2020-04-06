# computes the area of a triangle
def triangle_area(base, height):
    area = (1.0/2) * base * height
    return area

# triangle_area function
a1 = triangle_area(3, 8)
print (a1)
a2 = triangle_area(14, 2)
print (a2)

# converts fahrenheit to celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# test fahrenheit to celsius
c1 = fahrenheitToCelsius(32)
c2 = fahrenheitToCelsius(212)
print (c1, c2)

# converts fahrenheit to kelvin
def fahrenheitToKelvin(fahrenheit):
    celsius = fahrenheitToCelsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# test fahrenheit to kelvin
k1 = fahrenheitToKelvin(32)
k2 = fahrenheitToKelvin(212)
print (k1,k2)

# prints general kenobi
def kenobi():
    print ("Hello, there!")

# test general kenobi
kenobi()
k = kenobi()
print (k)
