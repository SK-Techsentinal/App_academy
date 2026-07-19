# Collect learner name and marks
name = input("Enter learner's name: ")
subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (subject1 + subject2 + subject3) / 3

# Assign letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass/fail status
status = "Pass" if average >= 50 else "Fail"

# Flag subjects below 40
flags = []
subjects = {"Subject 1": subject1, "Subject 2": subject2, "Subject 3": subject3}
for subject_name, mark in subjects.items():
    if mark < 40:
        flags.append(f"{subject_name} ({mark}) needs intervention")

# Display report card
print(f"\n{'--- Report Card ---':^40}")
print(f"Name: {name}")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")
if flags:
    print("Intervention flags:")
    for f in flags:
        print(f"  - {f}")
else:
    print("Intervention flags: None")