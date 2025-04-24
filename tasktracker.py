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
        # to_do_dict = {
        #     'To Do': None
        # }
        # in_prog_dict = {
        #     'In Progress': None
        # }
        # done_dict = {
        #     'Done': None
        # }
        # json_data.append(to_do_dict)
        # json_data.append(in_prog_dict)
        # json_data.append(done_dict)
           
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
    delete_task.add_argument('identifier', help="Identifier (ID number or task name)")
    
    mark_in_progress = sub_parser.add_parser('mark-in-progress')
    mark_in_progress.add_argument('identifier', help="Identifier (ID number or task name)")
    
    mark_done = sub_parser.add_parser('mark-done')
    mark_done.add_argument('identifier', help="Identifier (ID number or task name)")
    
    list_tasks = sub_parser.add_parser('list')
    list_tasks.add_argument('status', help="List type to view: done, todo, in-progress")
    
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
        case 'delete' | 'mark-in-progress' | 'mark-done':
            print('delete, mark in progress, mark done')
        case 'list':
            print('list')

def addTask(taskname):
    
    with open(filepath, 'r') as taskfile:
        data = json.load(taskfile)
    
    creationTime = str(datetime.now().time())
    
    print(data)
    data.append({
        'id':len(data),
        'description': taskname,
        'status': 'todo',
        'createdAt': creationTime,
        'updatedAt': creationTime
    })
    
    print(data)
    
    with open(filepath, 'w') as taskfile:
        json.dump(data, taskfile, indent=4)
    
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

if __name__ == '__main__':
    createFile()
    processRequest()