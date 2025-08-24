
import argparse
import csv
import os
from datetime import date, datetime

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
            listExpense()
        case 'summary' | 'Summary':
            summaryExpense(args.month)
        case 'delete' | 'Delete':
            deleteExpense(args.id)
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
        
    data = readCSV()
        
    for row in data:
        if row[0] == 'ID':
            ID = 1
        else:
            ID = int(row[0]) + 1
            
    data.append([ID, currentDate, description, type, amount])

    writeCSV(data)

def listExpense():
    
    data = readCSV()
    
    for row in data:
        
        # ID    Date    Description     Type    Amount
        # row[0] row[1] row[2]          row[3]  row[4]
        print("# {:<3} {:<12} {:<15} {:<10} {:<10}".format(row[0], row[1], row[2].capitalize(), row[3].capitalize(), row[4]))    

def summaryExpense(month):
    
    numDays = {
        '1': 31,
        '2': 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }
    
    data = readCSV()
    
    sum = 0
    count = 0
    
    if month is None:
        for row in data:
            if row[0] != 'ID':
                sum += float(row[4])
                count += 1
        
        average = sum / count
    
    else:
        for row in data:
            dateStr = row[1]
            dateObj = datetime.strptime(dateStr, "%Y-%m-%d")
            
            if str(dateObj.month) == month:
                sum += float(row[4])
                count += 1
        
        average = sum/count
            
    print(average)

def deleteExpense(id):

    data = readCSV
    
    newID = 1
    
    data = [row for row in data if row[0] != str(id)]
    for row in data:
        if row[0] != 'ID':
            row[0] = newID
            newID += 1
    
    print(f'The expense sheet has been updated. ID {id} has been deleted.')        
    print(data)
    writeCSV(data)

if __name__ == '__main__':
    processExpense()