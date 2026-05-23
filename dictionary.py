#Q-1
name = input("Enter the name: ").lower()

students = {"ram" : "ram@gmail.com", "shyam": "Shyam@gmail.com"}

if name in students:
    print("The email is", students[name])
else:
    print("Contact not found")



#Q-2
list = { "Milk","Bread", "Eggs"}
bought = {"Bread","Eggs"}

if list.symmetric_difference(bought) == set():
    print("Shopping complete")   
else:
    print(list.symmetric_difference(bought))



#Q-3
class_list = ["ram", "sita", "laxman"]

new_std = input("Enter name of new student: ").lower()

if new_std in class_list:
    print("Name already exists in the list")
else:
    class_list.append(new_std)
    print(class_list)



#Q-4
votes = ["Blue", "Red", "Blue", "Green", "Blue"]

if votes.count("Blue") >= 3:
    print("Blue Wins!")
else:
    print("Blue did not win")



#Q-5
grades = {"Ram":92, "Sita": 88}

name = input("Enter student name: ").title()

if name in grades:
    print(grades[name])
else:
    print("Grade is not available")



#Q-6
applicant = {"name":"Priya", "skills": ["Java","SQL"], "Experience years":1}
required_skill = {"Python","Java"}

if set(applicant.get("skills", [])) & required_skill and applicant["Experience years"] >= 2:
    print(f"{applicant['name']} qualifies")
else:
    print(f"{applicant["name"]} does not qualify")



#Q-7
banned_items = {"scissors", "knife", "lighter"}

name = input("Enter your item name: ").lower()
weight = float(input("Enter your bag weight: "))

if weight <= 7 and name not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")



#Q-8
dict = {
    "emp1": {"name":"Jhon","salary": 7500},
    "emp2": {"name":"Emma","salary": 8000},
    "emp3": {"name":"Shyam","salary": 500},
}

dict["emp3"]["salary"] = 8500
print(dict)



#Q-9
ram = set(input("Ram, enter your 2 items: ").lower().split(","))
Laxman = set(input("Laxman, enter your 2 items: ").lower().split(","))

if not ram.intersection(Laxman):
    print("No common items")
else:
    print("Some common items")



#Q-10
list = [10,20,30]
tuple = (10,20,30)
set = {10,20,30}
dict = {"a":"10", "b": "20", "c": 30}
val = 20

if val in list and val in tuple:
    if "b" in dict and val not in set:
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")



#Q-11
data = {"a":10, "b":20, "a": 30}
print(data)
#The value for a becomes 30 when you initialize a dictionary with duplicate keys.



#Q-12
[1,2,3] #List can not be use as a key in python dictionary.
#It is because list is mutable.



#Q-13
d = {"val":10}
if d.get("score"):
    print("found")
else:
    print("Not Found")
#It prints "not found" because no score is found and by using get method we remove the key error.



#Q-14
items = [10,10,20]

print(len(set(items)))
#the result is 2 since len function counts the index before and after commas.



#Q-15
set = {10,20,30}

new = set.add(40)
print(set)
#set.add adds 40 properly.



#Q-16
menu = { "pizza": 15,
        "burger": 10,
        "salad": 8}

order = "pizza"

if order in menu:
    print(menu[order])
else:
    print("Item not found")



#Q-17
student_data = {"name": "Sam", "score": 85}

score = student_data.get("score")
if score >= 80:
    student_data.update({"Status":"Pass"})
    print(student_data)
else:
    student_data.update({"Status":"Review"})
    print(student_data)



#Q-18
database = {"admin": "1234", "user": "abcd"}

user_input = "admin"
user_pass = "1234"

if user_input in database and user_pass in database["admin"]:
    print("Login Successful")
else:
    print("login failed")



#Q-19
emails = ["ram123@gmail.com", "hari77@gmail.com"]
blacklisted = {"hari77@gmail.com"}

current_email = "hari77@test.com"

if current_email in emails and current_email in blacklisted:
    print("Email Sent")
else:
    print("Blocked")



#Q-20
inventory = {"A1": 50, "B2": 0, "C2": 10}
restricted_zones = {"B2","Z9"}
target = "B2"

if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("Dispatched")
    else:
        print("Invalid zone")
else:
    print("target not in inventory")



#Q-21
valid_courses = {"python", "robotics", "java"}
hs_grade = [9,10,11,12]

student_name = input("Enter student's name: ").lower()
course = input("Enter the course: ").lower()
grade = int(input("Enter the grade: "))

students_record = {"student_name": student_name, "course": course, "grade": grade}

if not course in valid_courses:
    print(f"{student_name} selected invalid course")
if course in valid_courses:
    if grade < 9:
        print("Grade too low")
    elif grade > 12:
        print("Grade too high")
    else:
        if course == "robotics" and grade == 9:
            print(f"{student_name} is not eligible for {course} as grade is too low")
        else:
            print(f"{student_name} is approved for {course}")
