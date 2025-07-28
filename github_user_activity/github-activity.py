import argparse
import urllib.request
import json

def getUserName(githubUrl):
    with urllib.request.urlopen(githubUrl) as f:
        data = json.load(f)
    
    print(data)
    # processEvents(data)
    
    
def processUserName():
    parser = argparse.ArgumentParser(description='Github User Activity Tracker')
    parser.add_argument('username', help='Username to search')

    args = parser.parse_args()
    
    githubUrl = f'https://api.github.com/users/{args.username}/events'
    
    return githubUrl

def processEvents(data):
    
    print(data)
    
    repos = {}
    repoEvents = {}
    
    for event in data:
        print(event)
        
        # eventType = event['type']
        # eventRepo = event['repo']['name']
    
        # if eventRepo in repos:
        #     # Check the actions
        #     if repos[eventRepo][]
                
        # else:
        #     repos[eventRepo] = {{}}
        #     repos[eventRepo][f'Type: {eventType}'] = 1

if __name__ == '__main__':
    userName = processUserName()
    getUserName(userName)