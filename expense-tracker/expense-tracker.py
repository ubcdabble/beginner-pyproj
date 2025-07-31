
import argparse

def processExpense():

    parser = argparse.ArgumentParser(description='Create, edit, delete, or summarize expenses')
    
    # subparser = parser.add_subparsers(dest='command', description='Command to execute')
    parser.add_argument('command', help='Add expense')
    
    parser.add_argument('-d','--description', help='Description of expense')
    parser.add_argument('-t','--type', help='Type of expense [food, goods, commute, misc, services]')
    parser.add_argument('-a','--amount', help='Expense amount')
    parser.add_argument('-m','--month', help='Filter results to a month')
    
    
    args = parser.parse_args()

    print(args)
    print(args.command)
    
    match args.command:
        case 'add' | 'Add':
            print('add')
        case 'list' | 'List':
            print('list')
        case 'summary' | 'Summary':
            print('summary')
        case 'delete' | 'Delete':
            print('delete')
        case _:
            print(f'Error: {args.command} is an unknown command. Please try again.')

if __name__ == '__main__':
    processExpense()