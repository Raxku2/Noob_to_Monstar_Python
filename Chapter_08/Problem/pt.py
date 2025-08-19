student={"name":"Rahul","age":20,"marks":85}
print(student["name"])
print(student.get("marks"))
student["age"]=21
student["city"]="Kolkata"
student.pop("marks")
print(student.keys())
print(student.values())
for k,v in student.items(): print(k,v)
print("name" in student)
student.clear(); print(student)
