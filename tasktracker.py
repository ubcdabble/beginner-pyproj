import os
import json
import argparse
from datetime import datetime

filename = 'tasks.json'
foldername = '~/Documents/Projects/beginner-pyproj/tasktracker'

folderpath = os.path.expanduser(foldername)
filepath = os.path.join(folderpath, filename)

TO_DO_INDEX = 0
IN_PROGRESS_INDEX = 1
DONE_INDEX = 2

def createFile():
    
    os.makedirs(folderpath, exist_ok=True)

    if os.path.exists(filepath):
        with open(filepath, 'r') as taskfile:
            y = json.load(taskfile)
        print(y)
            
    else:
        json_data = []
        
        with open(filepath, 'w') as taskfile:
            json.dump(json_data, taskfile, indent=4) 
        print(f'File created at {filepath}')

def processRequest():
    parser = argparse.ArgumentParser(description="Create or edit a task list")
    sub_parser = parser.add_subparsers(dest='command', description="Command")
    
    add_task = sub_parser.add_parser('add')
    add_task.add_argument('task', help="Task name")
    
    update_task = sub_parser.add_parser('update')
    update_task.add_argument('id', help="ID number")
    update_task.add_argument('task', help="Task name")
    
    delete_task = sub_parser.add_parser('delete')
    delete_task.add_argument('id', help="ID number")
    
    mark_in_progress = sub_parser.add_parser('mark-in-progress')
    mark_in_progress.add_argument('id', help="ID number")
    
    mark_done = sub_parser.add_parser('mark-done')
    mark_done.add_argument('id', help="ID number")
    
    list_tasks = sub_parser.add_parser('list')
    list_tasks.add_argument('status', nargs='?', help="List type to view: done, todo, in-progress")
    
    args = parser.parse_args()
    
    print(f'You want to {args.command}')
    
    match args.command:
        case 'add':
            print(args.task)
            addTask(args.task)
        case 'update':
            print(args.id)
            print(args.task)
            updateTask(args.id, args.task)
        case 'delete':
            deleteTask(args.id)
        case 'mark-in-progress':
            markTask(args.id, 'in-progress')
        case 'mark-done':
            markTask(args.id, 'done')
        case 'list':
            listTask(args.status)

def addTask(taskname):
    
    with open(filepath, 'r') as taskfile:
        data = json.load(taskfile)
    
    creationTime = str(datetime.now().time())
    
    print(data)
    
    idList = []
    for i in range(len(data)):
        idList.append(data[i]["id"])
    
    idList.sort()
    lastId = idList[-1]
    newId = lastId + 1

    for i in range(len(idList)):
        if i != idList[i]:
            newId = i
            break
        
    data.append({
        'id': newId,
        'description': taskname,
        'status': 'todo',
        'createdAt': creationTime,
        'updatedAt': creationTime
    })
    
    print(data)
    
    with open(filepath, 'w') as taskfile:
        json.dump(data, taskfile, indent=4)
        
    print(f'Task added successfully: (ID: {newId})')
    
def updateTask(id, taskname):
    print('In update task!')
    with open(filepath, 'r') as taskfile:
        data = json.load(taskfile)
    
    for dicts in data:
        print(dicts)
        print(dicts['id'])
        if dicts['id'] == int(id):
            print('Found you bitch')
            updateTime = str(datetime.now().time())
            dicts['description'] = taskname
            dicts['updatedAt'] = updateTime
            
            print(dicts)
    
    with open(filepath, 'w') as taskfile:
        json.dump(data, taskfile, indent=4)

def deleteTask(id):
    with open(filepath, 'r') as taskfile:
        data = json.load(taskfile)
    print(data)
    
    data =  [dicts for dicts in data if dicts['id'] != int(id)]
    
    print(data)
    
    with open(filepath, 'w') as taskfile:
        json.dump(data, taskfile, indent=4)
        
def markTask(id, status):
    with open(filepath, 'r') as taskfile:
        data = json.load(taskfile)
    
    for dicts in data:
        if dicts['id'] == int(id):
            dicts['status'] = status
    
    with open(filepath, 'w') as taskfile:
        json.dump(data, taskfile, indent=4)

def listTask(status):
    print('inside list task')
    
    with open(filepath, 'r') as taskfile:
        data = json.load(taskfile)
    
    match status:
        case 'done':
            for dict in data:
                if dict['status'] == 'done':
                    print(dict)
        case 'todo':
            for dict in data:
                if dict['status'] == 'todo':
                    print(dict)
        case 'in-progress':
            for dict in data:
                if dict['status'] == 'in-progress':
                    print(dict)
        case _:
            for dict in data:
                print(dict)
    

if __name__ == '__main__':
    createFile()
    processRequest()