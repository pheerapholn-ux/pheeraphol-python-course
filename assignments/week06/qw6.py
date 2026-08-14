# เขียน function ชื่อ calculate_circle
def calculate_circle(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius *radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle Calculation:")
radius = 5
area, circumference = calculate_circle(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()
