try:
   with open("sample.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Operation completed.")