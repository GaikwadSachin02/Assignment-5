marks = {'Sachin':20,
         'Rahul':50,
         'Alice':85}
name = input("Enter the student's name: ")
try:
    print("{}'s marks:".format(name),marks[name])
except BaseException:
    print('Student not found.')
