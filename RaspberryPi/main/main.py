'''
This file contains the 'main()' function, which is the starting point of the program. High-level algorithms such as task
scheduling, thread instantiations, are defined here.
'''

import json
import shutil
import threading
import urllib.request

from pprint import pprint

def main():
    url = 'http://showmyway.comp.nus.edu.sg/getMapInfo.php?Building=COM1&Level=2'
    fileName = 'mapOfCom1Level2.json'
    
    downloadFile(url, fileName)
    
    # to open a file named 'fileName' as json file
    with open(fileName) as jsonFile:
        mapInfoRaw = json.load(jsonFile)
    
    northAt = mapInfoRaw['info']['northAt']
    nodesList = mapInfoRaw['map']
    
    node1X = mapInfoRaw['map'][0]['nodeId']
    
    pprint(mapInfoRaw)
    print('northAt: ' + northAt)
#     print('map: ' + nodesList[0])
    
    print(node1X)

# download the file from 'url' and save it locally as 'fileName'
def downloadFile(url, fileName):
    with urllib.request.urlopen(url) as response, open(fileName, 'wb') as file:
        shutil.copyfileobj(response, file)

if __name__ == '__main__':
    main()