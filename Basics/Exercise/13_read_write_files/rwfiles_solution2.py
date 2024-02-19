with open("stocks.csv", "r", newline='') as file:
    # reader = csv.DictReader(file)
    # for row in reader:
    #    print(f"{row['Company Name']} - {row['Price']} - {row['Earnings Per Share']} - {row[' Book Value']}")
    with open("output1.csv", "w", newline="") as file1:
        file1.write('Company Name,PE Ratio,PB Ratio\n')
        next(file)
        #writer = csv.DictWriter(file1, fieldnames=columns)
        #writer.writeheader()
        for string in file:
            #print('Company Name' + row['Company Name'])
            row = string.split(',')
            file1.write(f"{row[0]},"
                        f"{float(int(row[1]) / int(row[2])):.2f},"
                        f"{float(int(row[1]) / int(row[3])):.2f}\n")
