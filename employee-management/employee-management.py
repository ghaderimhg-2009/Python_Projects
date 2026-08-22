employee = {
    "name":"mohammad",
    "family":"ghaderi",
    "age":17,
    "city":"isfahan",
    "job":"python developer",
    "salary":25000000 
}

print(f"list1:{employee} \n")

employee["salary"] = "40000000"
print(f"list2:{employee} \n")

employee["phone"]="09916901234"
print(f"list3:{employee} \n")

del employee["city"]
print(f"list4:{employee} \n")

print(f"list5:{employee.keys()} \n")

print(f"list6:{employee.values()} \n")

print(f"list7:{employee.items()} \n")

print("====================")
print("  EMPLOYEE PROFILE  ")
print("====================")
print(f"Name:{employee['name']} {employee['family']}")
print(f"Age:{employee['age']}")
print(f"Job:{employee['job']}")
print(f"Salary:{employee['salary']} Toman")
print(f"Phone:{employee['phone']}")
print("--------------------")
print("Thank You For Visiting")
print("My Profile.")
print("Have A Great Day!")
print("====================")