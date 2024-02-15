# 1 Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
list = [2200, 2350, 2600, 2130, 2190]
print(f"1. In Feb, how many dollars you spent extra compare to January? "
      f"Answer is {list[1] - list[0]}")
print(f"2. Find out your total expense in first quarter "
      f"(first three months) of the year. Answer is {list[0] + list[1] + list[2]}")
print(f"3. Find out if you spent exactly 2000 dollars in any month. Answer is {2000 in list}")
list.append(1980)
print(f"4. June month just finished and your expense is 1980 dollar."
      f" Add this item to our monthly expense list. list[len(list)-1] is {list[len(list)-1]}")
list[3] = list[3] - 200
print(f"5. You returned an item that you bought in a month of April and got a refund of 200$."
      f" Make a correction to your monthly expense list based on this"
      f" list[3] = list[3] - 200 is {list[3]}")
# 2 You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

heros = ['spider man','thor','hulk','iron man','captain america']
print(f"1. Length of the list is {len(heros)}")

heros.append("black panther")
print(f"2. Add 'black panther' at the end of this list: {heros}")

heros.remove("black panther")
heros.insert(3, "black panther")
print(f"3. You realize that you need to add 'black panther' after 'hulk'"
      f",so remove it from the list first and then add it after 'hulk': {heros}")

heros[1:3] = ['doctor strange']
print(f"4. Now you don't like thor and hulk because they get angry easily"
      f" :) So you want to remove thor and hulk from list and replace"
      f" them with doctor strange (because he is cool)."
      f" Do that with one line of code: {heros}")

heros.sort()
print(f'5. Sort the heros list in alphabetical order (Hint. Use dir() '
      f'functions to list down all functions available in list) {heros}')
#print(dir(list))