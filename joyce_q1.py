with open ("file2.txt","r") as file:
     lines = file.readlines()
print (lines)
for sites in reversed(lines):
    print (sites.strip())
file.close()