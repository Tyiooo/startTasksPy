# 1ii Write a program that asks user to enter two cities and it
# tells you if they both are in same country or not.
# For example if I enter mumbai and chennai,
# it will print "Both cities are in India" but if I enter mumbai and
# dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1, city2 = input("Enter 2 cities, pls : "), input()

if city1 in india and city2 in india:
    print("Your cities in India!")
elif city1 in pakistan and city2 in pakistan:
    print("Your cities in Pakistan!")
elif city1 in bangladesh and city2 in bangladesh:
    print("Your cities in Bangladesh!")
else:
    print("They don't belong to same country(")