#2
stocks = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}
enter = '0'
while enter != "end":
    enter = input("Enter smth: ")
    if enter == "print":
        for i in stocks:
            print(f'{i} ==> {stocks[i]} ==> avg: {sum(stocks[i])/len(stocks[i]):.2f}')
    elif enter == "add":
        stock, price = input("Enter stock u wanna add: "), int(input("Enter price u wanna add: "))
        if stock in stocks:
            stocks[stock].append(price)
        else:
            stocks[stock] = [price]
