with open("sample.txt", "w") as sample_file:
    sample_file.write(
        "Hii this is the assignement 4 of file handling in python.\nWe are learning file handling in python.\nThis is very interesting."
    )

try:
    with open("sample.txt", "r") as read_file:
        content = read_file.readlines()
        i: int = 1
        print("Reading the file content")
        for line in content:
            line.rstrip("\n")
            print(f"Line {i}: {line}")
            i += 1

except FileNotFoundError as e:
    print("Error: The file 'sample.txt' was not found.")
