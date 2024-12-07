# Demonstrate writing data to a file

file = open("Nour1.txt", "w")
file.write("Hello BSTCS\n")
file.write("Good Day")
file.close()

# Demonstrate reading data from a file.


fileReading = open("Nour1.txt", "r")
Read = fileReading.read()
fileReading.close()
print(Read.lower())
