#1
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
counter = 0
for elem in result:
    if elem == "heads":
        counter+=1
print(f"Num of heads: {counter}\n")

#2
for i in range(1, 11):
    if i % 2 != 0:
        print(i**2)


#3
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]
number = int(input("Enter expense, pls: "))
month = -1
for i in range(len(expense_list)):
    if number == expense_list[i]:
        month = i
        break
if month != -1:
    print(f"Your expense amount was in {month_list[month]}")
else:
    print("We dont find this expense among our data(")


#4
for i in range(5):
    answer = input("are you tired?")
    if answer == "yes":
        break
    else:
        continue
if i == 4:
    print("congratulations !!!")
else:
    print("you didn't finish the race")

#5
s=''
for i in range(5):
    s+='*'
    print(s)