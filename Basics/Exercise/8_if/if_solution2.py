# Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar = int(input("Please, enter your fasting sugar level: "))
if sugar < 80:
    print("Your sugar is low!")
elif sugar > 100:
    print("Your sugar is high!")
else:
    print("Your sugar is normal, keep it up!")