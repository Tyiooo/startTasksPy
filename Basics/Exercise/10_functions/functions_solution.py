#1-2
def calculate_area(shape, base, height):
    if shape == "rectangle":
        return base*height
    else:
        return 1/2*base*height

print(calculate_area("triangle", 1, 2))

#3
def print_pattern(length):
    s=''
    for i in range(length):
        s+='*'
        print(s)

print_pattern(3)
