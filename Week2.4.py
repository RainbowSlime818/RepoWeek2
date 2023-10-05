# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

students = int(input("How many students attended today?"))
size = int(input("How many sweets are left?"))

sweetper = size//students
leftover = size-(sweetper*students)

if (leftover == 1):
    print("Each student will get", sweetper, "sweets with", leftover, "sweet left over")
else:
    print("Each student will get",sweetper,"sweets with",leftover,"sweets left over")

