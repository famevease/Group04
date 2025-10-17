f_out = open("outro.txt", "wb")
with f_out:
    f_out.write(b"Today's sky is blue")

numbers = [10, 20, 30, 40]
n = bytearray(numbers)
with open("numbers.bin", "wb") as file:
    file.write(n)

