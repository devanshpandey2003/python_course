with open("output.txt", "x") as output_file:
    output_file.write("This is the first line in the output file.\n")


user_input = input("Enter text to write to the file: ")

try:
    with open("output.txt", "w") as output_file:
        output_file.write(user_input + "\n")
        print("Data successfully written to output.txt.\n")

except Exception as e:
    print("Error: file not found.")


additional_input = input("Enter additional text to append: ")
try:
    with open("output.txt", "a") as output_file:
        output_file.write(additional_input + "\n")
        print("Data successfully appended.\n")

except Exception as e:
    print("Error: file not found.")

try:
    with open("output.txt", "r") as read_file:
        content = read_file.read()
        print(content)


except Exception as e:
    print("Error: file not found.")
