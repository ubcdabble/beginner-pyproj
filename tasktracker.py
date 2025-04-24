import os
import json
import argparse

filename = 'tasks.json'
foldername = '~/Documents/Projects/beginner-pyproj/tasktracker'

folderpath = os.path.expanduser(foldername)
filepath = os.path.join(folderpath, filename)

def createFile():
    
    os.makedirs(folderpath, exist_ok=True)

    if os.path.exists(filepath):
        with open(filepath, 'r') as taskfile:
            y = json.load(taskfile)
        print(y)
            
    else:   
        with open(filepath, 'w') as taskfile:
            json.dump([], taskfile, indent=4) 
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
            print('add')
        case 'update':
            print('update')
        case 'delete' | 'mark-in-progress' | 'mark-done':
            print('delete, mark in progress, mark done')
        case 'list':
            print('list')

def addTask(taskname, status):
    with open(filepath, 'w') as taskfile:
        json.dump('[]', taskfile, indent=4)
    



if __name__ == '__main__':
    createFile()
    processRequest()