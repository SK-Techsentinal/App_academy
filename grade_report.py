students = [
    {"name": "Thabo", "maths": 78, "english": 65, "science": 82},
    {"name": "Amara", "maths": 91, "english": 88, "science": 95},
    {"name": "Sipho", "maths": 45, "english": 52, "science": 38},
    {"name": "Lerato", "maths": 67, "english": 71, "science": 60},
    {"name": "Fatima", "maths": 55, "english": 48, "science": 62},
]

results = []

# Process each student
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

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

    status = "Pass" if average >= 50 else "Fail"

    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status,
    })


# Class statistics
if results:
    averages = [r["average"] for r in results]
    class_average = round(sum(averages) / len(averages), 2)
    highest = max(averages)
    lowest = min(averages)

    # Display class report
    print(f"\n{'--- Class Report ---':^40}")
    for r in results:
        print(f"{r['name']:<10} Avg: {r['average']:<7} Grade: {r['grade']:<3} Status: {r['status']}")

    print(f"\nClass Average: {class_average}")
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")

    # Search loop
    while True:
        search_name = input("\nSearch for a student by name (or type 'exit' to quit): ").strip()
        if search_name.lower() == "exit":
            print("Goodbye!")
            break

        found = False
        for r in results:
            if r["name"].lower() == search_name.lower():
                print(f"{r['name']}: Average {r['average']}, Grade {r['grade']}, Status {r['status']}")
                found = True
                break

        if not found:
            print("Student not found. Try again.")
