import math
#3
def circle_calc(r):
    area = math.pi * r**2
    circumference = 2 * math.pi * r
    diameter = 2 * r
    return area, circumference, diameter

radius = int(input("Enter radius of a circle: "))
area, circumference, diameter = circle_calc(radius)
print(f"area: {area:.2f} \ncircumference : {circumference:.2f}\ndiameter : {diameter}")