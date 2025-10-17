#bai1
f = open("output.txt", "w")
f.write("I'm a student\n")

#bai2
x = 1/7
f.write(f"{x:.5f}")
f.write("\n")

#bai3
a, b = map(int, input("Input a and b: \n").split()) # How to type multiple numbers in one line: use "list", "map" and "split"
c=a+b
f.write(str(c))
f.write("\n")

#bai4
filename = input("Enter file name: ")

try:
    with open(filename, 'r', encoding='utf-8') as ff:
        content = ff.read()
        f.write("\nFile content:")
        f.write(content)

except FileNotFoundError:
    f.write("Error: File does not exit!")

