import os

user = input("Enter the username to generate tags for: ")
count = 0
list = []
scriptDir = os.path.dirname(__file__)
listDir = "tagList.txt"
fullDir = os.path.join(scriptDir, listDir)

while count < 10000:
    list.append(count)
    count  += 1

for i in list:
    if i < 1000:
        list[i] = "{:04}".format(i)
list[i] = str(list[i])
list.remove(list[0])
count = 0

while count < 9999:
    list[count] = user+"#"+str(list[count])
    count+=1

z = open(fullDir,"w")
for k in list:
    z.write("'")
    z.write(k)
    z.write("', ")
z.close
print("Successfully wrote a list of all possible Discord tags with the username: "+"'"+user+"'"+", to the file: "+fullDir)