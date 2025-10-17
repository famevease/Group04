filename = input("Nhập tên file: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("\n--- Nội dung file ---")
        print(content)

except FileNotFoundError:
    print("Lỗi: File không tồn tại!")

except Exception as e:
    print("Có lỗi xảy ra:", e)
