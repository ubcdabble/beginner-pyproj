
import argparse
import csv
import os
from datetime import date

filename = 'expenses.csv'

currentDate = date.today()

def processExpense():

    parser = argparse.ArgumentParser(description='Create, edit, delete, or summarize expenses')
    
    # subparser = parser.add_subparsers(dest='command', description='Command to execute')
    parser.add_argument('command', help='Add expense')
    
    parser.add_argument('-d','--description', help='Description of expense')
    parser.add_argument('-t','--type', dest='expense_type', help='Type of expense [food, goods, commute, misc, services]')
    parser.add_argument('-a','--amount', help='Expense amount')
    parser.add_argument('-m','--month', help='Filter results to a month')
    parser.add_argument('--id', help='ID of the expense to select')
    
    
    args = parser.parse_args()

    print(args)
    print(args.command)
    
    newCSV()
    
    match args.command:
        case 'add' | 'Add':
            addExpense(args.description, args.expense_type, args.amount)
        case 'list' | 'List':
            print('list')
        case 'summary' | 'Summary':
            print('summary')
        case 'delete' | 'Delete':
            print('delete')
        case _:
            print(f'Error: {args.command} is an unknown command. Please try again.')

def newCSV():
    file_exists = os.path.exists(filename)
    if not file_exists:
        writeCSV([('ID','Date','Description','Type','Amount')])   # Header

def readCSV():
    
    with open(filename, mode = 'r', newline = '') as file:
        reader = csv.reader(file)
        data = list(reader)

    return data

def writeCSV(newFile):
    
    with open(filename, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        
        writer.writerows(newFile)

def addExpense(description,type,amount):
        
    fileCSV = readCSV()
        
    for row in fileCSV:
        if row[0] == 'ID':
            ID = 1
        else:
            ID = int(row[0]) + 1
            
    fileCSV.append([ID, currentDate, description, type, amount])

    writeCSV(fileCSV)

    

if __name__ == '__main__':
    processExpense()