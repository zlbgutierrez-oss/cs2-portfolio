# Ask the user to enter a student score
score = int(input("Enter student score (0-100): "))

# Validate that the score is within the allowed range
if score < 0 or score > 100:
    print("Invalid Score.")
# Determine the appropriate performance classification
elif score >= 90:
    print("Outstanding")
elif score >= 80:
    print("Very Satisfactory")
elif score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")
