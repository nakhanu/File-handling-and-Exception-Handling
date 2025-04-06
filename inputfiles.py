try:
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        outfile.write(infile.read().upper())
    print("File successfully modified and saved to output.txt ✅")
except FileNotFoundError:
    print("Input file not found.")