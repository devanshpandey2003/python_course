student_marks: dict = {"Alice": 85, "Bob": 92, "Charlie": 78}


def get_student_mark(name: str) -> None:
    if name not in student_marks:
        print("Student not found.")

    print(f"{name}'s  marks: {student_marks.get(name)}")


if __name__ == "__main__":
    name = input("Enter student name from the list (Alice, Bob, Charlie): ")
    name = name.capitalize()
    get_student_mark(name)
