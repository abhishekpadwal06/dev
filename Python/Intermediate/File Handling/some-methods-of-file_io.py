# f.readlines
with open("Lewis.txt", 'r') as f:
    line = f.readline()
    print(line)



# f.writelines
with open("Lewis2.txt", 'w') as f:
    lines = ["Hey, I'm Lewis\n", "How are you?\n", "I'm a F1 driver\n", "I have 7 WDC\n", "I drive for Scuderia Ferrari HP Formula 1 team!"]
    f.writelines(lines)



# seek() and tell()
with open("Lewis2.txt", 'r') as f:
    f.seek(5)   # Move to 5th byte in the file
    data = f.read(5)   # Read the next 5 bytes from the file
    print(data)
    print(f.tell())  # Returns the current position within the file



# f.truncate()
with open("Lewis2.txt", 'w') as f:
    f.write("Hello Lewis")
    f.truncate(6)

with open("Lewis2.txt", 'r') as f:
    line = f.readline()
    print(line)