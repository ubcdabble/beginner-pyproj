import argparse
import urllib.request
import json

def getUserName(githubUrl):
    with urllib.request.urlopen(githubUrl) as f:
        data = json.load(f)
    
    processEvents(data)
    
    
def processUserName():
    parser = argparse.ArgumentParser(description='Github User Activity Tracker')
    parser.add_argument('username', help='Username to search')

    args = parser.parse_args()
    
    githubUrl = f'https://api.github.com/users/{args.username}/events'
    
    return githubUrl

def processEvents(data):
    for event in data:
        eventType = event['type']
        eventRepo = event['type']['repo']['name']
        
        

if __name__ == '__main__':
    userName = processUserName()
    getUserName(userName)