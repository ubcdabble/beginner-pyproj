import argparse
import urllib.request

def getUserName():
    print('Hi')
    
def processUserName():
    parser = argparse.ArgumentParser(description='Github User Activity Tracker')
    parser.add_argument('username', help='Username to search')

    args = parser.parse_args()
    
    githubUrl = f'https://api.github.com/users/{args.username}/events'
    
    # print(urllib.request.urlretrieve(githubUrl))
    
    with urllib.request.urlopen(githubUrl) as f:
        print(f.read().decode('utf-8'))

if __name__ == '__main__':
    processUserName()
    # getUserName()