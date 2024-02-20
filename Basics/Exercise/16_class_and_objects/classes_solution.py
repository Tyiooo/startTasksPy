class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

employee_egor = Employee(123, "Egor4ik")
print(str(employee_egor.id) + " " + employee_egor.name)

try:
    del employee_egor.id
    print(str(employee_egor.id) + " " + employee_egor.name)
except AttributeError as e:
    print("Id successfully deleted")

try:
    del employee_egor
    print(str(NameError.id) + " " + employee_egor.name)
except AttributeError as e:
    print("Object successfully deleted")
