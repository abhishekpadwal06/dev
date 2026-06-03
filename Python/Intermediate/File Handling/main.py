# Reading from a file       ('r' mode is by default!)
f = open("myfile1.txt")     # U can also write it as f = open("myfile.txt", 'r')
text = f.read()
print(text)
f.close()

# Writing to a file
f = open("myfile2.txt", 'w')
f.write("Hey Lewis, wassup?")
f.close()

# Appending to a file
f = open("myfile2.txt", 'a')
f.write("\nHow are you man?")
f.close()

with open("myfile2.txt", 'a') as f:
    f.write("\nI am using with method, hence there's no need to use f.close")
