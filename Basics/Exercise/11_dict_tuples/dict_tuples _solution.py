#1
countries = {"China":143, "India":136, "USA":32, "Pakistan":21}

enter = '0'
while enter != "end":
    enter = input("Enter smth: ")
    if enter == '':
        for key in countries:
            print(f"{key}==>{countries[key]}")
    elif enter == "add":
        country = input("Enter country u wanna add: ")
        if country in countries:
            print("This country already exists(")
        else:
            population = input("Enter population u wanna add to this country: ")
            countries[country] = population
    elif enter == "remove":
        country = input("Enter country u wanna remove: ")
        if country in countries:
            del countries[country]
        else:
            print("This country doesnt exist in map(")
    elif enter == "query":
        country = input("Enter country u wanna see population: ")
        print(countries[country])
    else:
        print("Enter some command maybe ))")