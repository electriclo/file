file = open("C:/Users/feixi_000/Desktop/New folder/file1.txt","r")
contents = file.read()
print (contents)
file.close()

#readlines technique
print ("this program reads the lines of a file into seperate strings.")
with open("file1.txt","r") as file:
  lines = file.readlines()
print (lines)

#writing a file
with open ("file1.txt","w") as optfile:
    optfile.write ("i love python")
optfile.close()

#directories
import os
#get current working directory
current = os.getcwd()

print ("current directory=",current)

print ("this program reads the lines of a file into seperate strings and prints in reverse order")
with open("file2.txt","r") as file:
  lines = file.readlines()
print (lines)
for sites in reversed(lines):
  print (sites.strip())
file.close()