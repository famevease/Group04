filename = input("Enter file name: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("\nFile content:")
        print(content)

except FileNotFoundError:
    print("Error: File does not exit!")
