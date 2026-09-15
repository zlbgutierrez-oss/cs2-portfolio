VALID_GRADES = ["7", "8", "9", "10", "11", "12"]
EMAIL_DOMAIN = "@brc.pshs.edu.ph"

student_name = input("Enter student name: ").strip()
age_input = input("Enter age: ").strip()
grade_level = input("Enter grade level: ").strip()
email = input("Enter email: ").strip()
registration_code = input("Enter registration code: ").strip()

errors = []

if student_name == "":
    errors.append("Student name is required.")

age = None
try:
    age = int(age_input)
    if age < 11 or age > 18:
        errors.append("Age must be from 11 to 18.")
except ValueError:
    errors.append("Age must be a number.")

if grade_level not in VALID_GRADES:
    errors.append("Invalid grade level. Must be 7-12.")

username = email[:-len(EMAIL_DOMAIN)] if email.endswith(EMAIL_DOMAIN) else ""

if not email.endswith(EMAIL_DOMAIN) or username == "":
    errors.append("Invalid email. Must be a valid @brc.pshs.edu.ph address.")

if len(registration_code) != 6 or not registration_code.isalnum():
    errors.append("The registration code must contain exactly 6 alphanumeric characters.")

print("------------------------------")

if not errors:
    print("REGISTRATION ACCEPTED")
    print("------------------------------")
    print("Student:", student_name)
    print("Age:", age)
    print("Grade Level:", grade_level)
    print("Email:", email)
else:
    print("REGISTRATION REJECTED")
    print("------------------------------")
    for e in errors:
        print("-", e)
