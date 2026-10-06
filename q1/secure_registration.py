ALLOWED_SECTIONS = ["Dahlia"]
ALLOWED_CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]
ALLOWED_ATTENDANCE = ["Present", "Absent", "Late"]


def check_name(name):
    if name == "":
        return "Student name is required."
    return ""


def check_section(section):
    if section not in ALLOWED_SECTIONS:
        return "Please enter a valid section."
    return ""


def check_club(club):
    if club not in ALLOWED_CLUBS:
        return "Please choose a valid club."
    return ""


def check_email(email):
    if "@" not in email:
        return "Email must contain @."
    if "." not in email:
        return "Email must contain a period (.)."
    if " " in email:
        return "Email must not contain spaces."
    return ""


def check_attendance(status):
    if status not in ALLOWED_ATTENDANCE:
        return "Attendance must be Present, Absent, or Late."
    return ""


def match_allowed(value, allowed_list):
    for item in allowed_list:
        if value.lower() == item.lower():
            return item
    return value


def main():
    print("=== PSHS Club Registration ===")

    student_name = input("Student Name: ").strip()
    section = match_allowed(input("Section: ").strip(), ALLOWED_SECTIONS)
    club = match_allowed(input("Club Choice (Robotics/Science/Mathematics/Programming): ").strip(), ALLOWED_CLUBS)
    email = input("School Email: ").strip()
    attendance = match_allowed(input("Attendance Status (Present/Absent/Late): ").strip(), ALLOWED_ATTENDANCE)

    errors = []
    for message in (check_name(student_name),
                    check_section(section),
                    check_club(club),
                    check_email(email),
                    check_attendance(attendance)):
        if message != "":
            errors.append(message)

    print()
    if errors:
        print("--------------------------------")
        print("REGISTRATION REJECTED")
        print("--------------------------------")
        for message in errors:
            print("Error:", message)
    else:
        print("--------------------------------")
        print("REGISTRATION ACCEPTED")
        print("--------------------------------")
        print("Student:", student_name)
        print("Section:", section)
        print("Club:", club)
        print("Email:", email)
        print("Attendance:", attendance)


main()
