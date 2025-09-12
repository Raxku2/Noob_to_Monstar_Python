from pymongo import MongoClient

# Replace with your Atlas connection string
uri = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/test"

try:
    # Connect to MongoDB
    client = MongoClient(uri)
    db = client["schoolDB"]
    teachers = db["teachers"]

    print("✅ Connected to MongoDB Atlas!")

    # Insert a teacher document
    teacher_data = {"name": "Arjun", "subject": "Mathematics", "experience": 5}
    teachers.insert_one(teacher_data)
    print("Inserted Teacher:", teacher_data["name"])

    # Fetch all teachers
    print("All Teachers:")
    for teacher in teachers.find():
        print(teacher)

except Exception as e:
    print("❌ Error:", e)
