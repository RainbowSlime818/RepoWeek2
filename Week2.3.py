# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

students = int(input("How many students?"))
size = int(input("Required group size?"))

groupnum = students//size
leftover = students-(groupnum*size)

if (leftover == 1):
    print("There will be", groupnum, "groups with", leftover, "student left over")
else:
    print("There will be",groupnum,"groups with",leftover,"students left over")

