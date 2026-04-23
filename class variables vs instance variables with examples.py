class Student:
    # 1. Class Variable (Shared by all students)
    school_name = "Global Public School"

    def __init__(self, name, roll_no):
        # 2. Instance Variables (Unique to each student)
        self.name = name
        self.roll_no = roll_no

# Objects create karte hain
s1 = Student("Aman", 101)
s2 = Student("Priya", 102)

# Instance variables access karna
print(f"Student 1: {s1.name}, Roll: {s1.roll_no}, School: {s1.school_name}")
print(f"Student 2: {s2.name}, Roll: {s2.roll_no}, School: {s2.school_name}")

# --- Difference Tab Dikhta Hai Jab Hum Value Badalte Hain ---

# Class variable ko change karna (Saari class ke liye badal jayega)
Student.school_name = "International Academy"

print("\n--- After changing Class Variable ---")
print(f"{s1.name}'s school: {s1.school_name}")
print(f"{s2.name}'s school: {s2.school_name}")

# Instance variable ko change karna (Sirf usi object par asar padega)
s1.name = "Aman Kumar"

print("\n--- After changing Instance Variable ---")
print(f"S1 Name: {s1.name}")
print(f"S2 Name: {s2.name}") # S2 ka naam wahi rahega