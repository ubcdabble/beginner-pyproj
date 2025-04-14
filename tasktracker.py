import os
import json

filename = 'tasks.json'
foldername = '~/Documents/Projects/beginner-pyproj/tasktracker'

folderpath = os.path.expanduser(foldername)
print(folderpath)

filepath = os.path.join(folderpath, filename)
os.makedirs(folderpath, exist_ok=True)

if os.path.exists(filepath):
    with open(filepath, 'r') as taskfile:
        print(taskfile.read())

else:   
    with open(filepath, 'w') as taskfile:
        username = input('What is your name: ')
        taskfile.write(f"{username}'s Task List")

    print(f'File created at {filepath}')

# def taskSelect():
#     print()
    
# def checkJSON():
#     if os.path.exists(filename):
#         print('Welcome back!')
#     else:
#         print('Hello new user')

# test = input("Please enter something")
# print(f'You entered: {test}')