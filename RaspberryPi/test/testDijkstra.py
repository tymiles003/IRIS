'''
This file is used for Week 7 demo of Dijkstra's algorithm.
'''

from main.main import printWelcomeMsg
from main.main import downloadFile

def testDijkstra():
    printWelcomeMsg()
    
    while True:
        print('\n=============== NEW TEST CASE ===============\n')
        buildingName = input('Enter building name: ')
        storey = input('Enter storey: ')
        startNodeId = input('Enter start node ID: ')
        endNodeId = input('Enter end node ID: ')
        
        try:
            url = 'http://showmyway.comp.nus.edu.sg/getMapInfo.php?Building=XXX&Level=YYY'
            url.replace('XXX', 'buildingName')
            url.replace('YYY', 'storey')
            fileName = 'mapOf' + buildingName.title() + "Storey" + storey + '.json'
            downloadFile(url, fileName)
        except:
            continue

if __name__ == '__main__':
    testDijkstra()