# Fundamentals of Cybersecurity and Data Privacy

**Activity:** PSHS Secure Club Registration System
**Name:** Your Name
**Section:** Dahlia
**Quarter:** 1

---

## Activity Overview

In this activity, I studied an online scam and made safe rules for collecting information in a simple PSHS Club Registration System.

My goal was to make a program that asks only for the information it really needs, and only accepts answers that are correct and make sense.

---

# Part A - Cybersecurity Threat Analysis

## Assigned Case

**Case Number:** 1
**Case Title:** Fake Login Alert

> A message says the student's account will be disabled. It asks the student to click a link and type their username and password.

---

### 1. What cybersecurity threat is shown?

This is **phishing**. Phishing is when a scammer pretends to be someone you trust, like the school or an email company, to trick you into giving your username and password on a fake website.

### 2. What warning signs make the situation suspicious?

- **It tries to scare me.** It says my account will be disabled so I will panic and click without thinking.
- **It asks for my password.** Real companies and schools do not ask for passwords through a link in a message.
- **The link looks strange.** The website address may look almost real but has a different spelling or an unfamiliar ending.
- **I did not expect it.** I never asked for any change to my account.
- **It sounds general or has wrong grammar.** Many scam messages are sent to many people at once.

### 3. What may be affected?

- Data
- Account
- Application
- Device
- Network
- Financial information

> The **account** is hurt first because the scammer gets my username and password. My **data**, like files, messages, and grades, can be seen or stolen. Other **applications** that use the same login can also be opened. If the link also installs harmful software, my **device** can get infected. If I use the same password on other sites, my **financial information**, like saved payment details, can be in danger too. The **network** can be affected only if the infected device connects to the school Wi-Fi.

### 4. What information could be exposed or misused?

My username, password, school email, personal messages and files, and contact list. If I use the same password for other accounts, those can be opened too. The scammer could also pretend to be me and send fake messages to my classmates and teachers.

### 5. What should the user do to reduce the risk?

- **Do not click** the link and do not reply.
- **Check** if the message is real by opening the official website myself (typing the address) or by asking my teacher or the school IT office.
- **Report** the message and then delete it.
- If I already typed my password, **change it right away** and turn on two-step login (a code is needed every time I sign in).
- Use a **different password** for each account and keep my device updated.

---

# Part B - Data Privacy and Secure Data Capture

A proposed Club Registration System wants to collect the following information.
I decided if each item is really necessary.

| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | COLLECT | We need to know who is registering. |
| Section | COLLECT | We need to know which class the student belongs to. |
| Club Choice | COLLECT | This is the main reason for the registration. |
| School Email | COLLECT | The club needs a way to contact the student. |
| Attendance Status | COLLECT | It is needed to record who came to the club. |
| Password | DO NOT COLLECT | A club form never needs a password. If the data leaks, someone could take over the student's account. |
| OTP | DO NOT COLLECT | An OTP is a secret code that proves it is really me. Scammers often ask for it to get into accounts, so no real form should ask for it. |
| Home Address | DO NOT COLLECT | It is not needed for a club, and it is private information that could be misused. |
| Parent Bank Account | DO NOT COLLECT | Money information is not needed here, and it could cause serious harm if stolen. |

---

## Privacy Question

Why is it safer to collect only information that the program actually needs?

> If the program never collects a piece of information, nobody can steal or misuse it. So if the data is ever leaked, less harm is done. It also shows respect for students and their parents, and it makes the program simpler and easier to keep safe.

---

# Part C - Security-Focused Validation Rules

I filled in this table before writing my program.

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Any name that is not blank, like `Maria Santos` | Records with no name cannot be used | (blank) | The name must not be empty, even after removing extra spaces | Student name is required. |
| Section | A section given by the teacher, like `Dahlia` | Students put in a section that does not exist, and messy records | `Rose` | The section must be one of the allowed sections | Please enter a valid section. |
| Club Choice | `Robotics`, `Science`, `Mathematics`, or `Programming` | Joining a club that does not exist | `Gaming` | The club must be one of the four clubs on the list | Please choose a valid club. |
| School Email | Text with `@` and `.`, like `student@pshs.edu.ph` | Wrong or fake emails, so the club cannot contact the student | `studentpshs.edu.ph` | It must have `@`, it must have `.`, and it must have no spaces | Email must contain @. / Email must contain a period (.). |
| Attendance Status | `Present`, `Absent`, or `Late` | Wrong attendance records | `Excused` | It must be one of the three allowed words | Attendance must be Present, Absent, or Late. |

---

## Secure Data Capture Questions

### 1. What should your program accept?

> My program should accept a name that is not blank, the section Dahlia, one of the four clubs (Robotics, Science, Mathematics, Programming), an email that has `@` and `.`, and an attendance of Present, Absent, or Late.

### 2. What should your program reject?

> It should reject a blank name, a section or club that is not on the list, an email without `@` or `.` (or with spaces), and any attendance that is not Present, Absent, or Late.

### 3. How do your validation rules help reduce incorrect or unsafe input?

> The rules check every answer before the program accepts it. This stops mistakes and strange answers from getting into the records. Accepting only answers from an approved list is a simple but strong way to keep a program safe, because the program only takes what it expects.

---

# Part D - Secure Program Implementation

## Program

I made a simple **PSHS Club Registration System**.
The program collects only:

- Student Name
- Section
- Club Choice
- School Email
- Attendance Status

It does **not ask for passwords, OTPs, banking information, or any other unnecessary personal information**.

---

## Source Code File

[`secure_registration.py`](secure_registration.py)

---

## Final Code

```python
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
```

---

## Security Practices Applied

### Required Input

> The `check_name()` function rejects a blank name. I also used `.strip()` on every answer, so a name made of only spaces counts as blank too.

### Allowed Values

> Section, club choice, and attendance only accept words from lists I made at the top of the program (`ALLOWED_SECTIONS`, `ALLOWED_CLUBS`, and `ALLOWED_ATTENDANCE`). Anything else, like `Gaming`, is rejected. Capital or small letters do not matter, so `programming` is accepted as `Programming`.

### Format Check

> The email must have `@` and `.` and no spaces. This is a simple check that fits my level. It cannot prove that the email is real, but it catches obvious mistakes.

### Error Messages

> Clear error messages tell the user exactly what went wrong, so they can fix it quickly. They also show that the program is rejecting the answer on purpose and did not simply break.

### Data Minimization

> I did **not** collect passwords, OTPs, home addresses, or banking information. A club registration does not need them, and collecting them would only add risk if the data were leaked.

---

# Part E - Testing and Reflection

## Testing

| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid (`Ana Cruz`, `Dahlia`, `Programming`, `ana@pshs.edu.ph`, `Present`) | Registration accepted | `REGISTRATION ACCEPTED` with the five details shown | PASS |
| 2 | Blank student name | Rejected: Student name is required. | `REGISTRATION REJECTED` / `Error: Student name is required.` | PASS |
| 3 | Invalid section (`Rose`) | Rejected: Please enter a valid section. | `REGISTRATION REJECTED` / `Error: Please enter a valid section.` | PASS |
| 4 | Invalid club choice (`Gaming`) | Rejected: Please choose a valid club. | `REGISTRATION REJECTED` / `Error: Please choose a valid club.` | PASS |
| 5 | Email missing `@` (`anapshs.edu.ph`) | Rejected: Email must contain @. | `REGISTRATION REJECTED` / `Error: Email must contain @.` | PASS |
| 6 | Email missing `.` (`ana@pshsedu`) | Rejected: Email must contain a period (.). | `REGISTRATION REJECTED` / `Error: Email must contain a period (.).` | PASS |
| 7 | Invalid attendance status (`Excused`) | Rejected: Attendance must be Present, Absent, or Late. | `REGISTRATION REJECTED` / `Error: Attendance must be Present, Absent, or Late.` | PASS |
| 8 | Different valid inputs (`Maria Santos`, `Dahlia`, `Robotics`, `maria@pshs.edu.ph`, `Late`) | Registration accepted | `REGISTRATION ACCEPTED` with Maria Santos, Dahlia, Robotics, maria@pshs.edu.ph, Late | PASS |

Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.

---

# Reflection

### 1. What is one cybersecurity threat that can affect an application or user?

> Phishing. A scammer sends a fake message that looks real to steal passwords or personal information.

### 2. How can users reduce the risk of phishing or suspicious messages?

> I should not click unknown links or download unknown files. I should check who sent the message and look at the website address carefully. I should never share my password or OTP with anyone. I can also turn on two-step login and tell a teacher or the IT office about suspicious messages.

### 3. How can validation rules improve the security of user input?

> They make sure the program accepts only answers it expects. This stops mistakes and strange or harmful input before the program uses it.

### 4. Why should a program avoid collecting unnecessary personal information?

> Information that is not collected cannot be leaked or misused. It lowers the harm if the data is stolen, protects the privacy of students, and keeps the program simple.

### 5. How did SG7's input validation concepts become security practices in SG8?

> In SG7, I used input validation to make my programs work properly, like checking for blank answers and correct values. In SG8, I used the same checks to protect the program and its users. Rejecting wrong input, accepting only approved answers, and collecting less information all became ways to keep data safe, not just ways to avoid errors.

---

# Files for This Activity

- [`secure_registration.py`](secure_registration.py)
- [`cyber_security.md`](cyber_security.md)

---

[← Back to Main Portfolio](../README.md)
