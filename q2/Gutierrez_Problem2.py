
def calculate_average(s1, s2, s3):
    return (s1 + s2 + s3) / 3

def get_performance(avg):
    if avg >= 85:
        return "Mastery"
    elif avg >= 70:
        return "Developing"
    else:
        return "Needs Review"

def is_eligible(avg, tasks):
    return avg >= 85 and tasks >= 3


s1 = float(input("Enter Score 1: "))
s2 = float(input("Enter Score 2: "))
s3 = float(input("Enter Score 3: "))
tasks = int(input("Completed Tasks: "))

avg = calculate_average(s1, s2, s3)

print(f"\nAverage: {avg:.2f}")
print("Performance:", get_performance(avg))
print("Eligible for Challenge:", is_eligible(avg, tasks))


# Documentation Questions
# 1. calculate_average returns a number,
#    get_performance returns a string,
#    is_eligible returns a Boolean.
# 2. The average is passed as an argument.
# 3. The student is not eligible if tasks are below 3.
# 4. return lets us reuse results in the program.
