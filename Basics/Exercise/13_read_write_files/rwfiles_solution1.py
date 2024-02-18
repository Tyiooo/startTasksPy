f = open("poem.txt", "r")
# print(f.read())
dict = {}
for line in f:
    tokens = line.split(" ")
    for el in tokens:
        if el in dict:
            dict[el] +=1
        else:
            dict[el] = 1
print(dict)

arr = list(dict.values())
print(max(arr))

for word, count in dict.items():
    if count == max(arr):
        print(word)
f.close()
