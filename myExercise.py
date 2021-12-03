import sys
file = open(sys.argv[1])
names = sys.argv[2]
#names = input("please give the names: ")
#file = open("students.txt")
info = {}
for line in file:
    sp = line.split(":")
    info[sp[0]] = sp[1][:-1]

names = names.split(",")

for person in names:
    try:
        print("Name:",person,"University:",info[person])
    except:
        print("No record of {} found.".format(person))

file.close()