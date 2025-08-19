student = {"name":"Rahul", "age":20, "marks":85}
print(student["name"])
print(student.get("marks"))

student.update({"age":21})
print(student)

student.pop("marks")
print(student)
