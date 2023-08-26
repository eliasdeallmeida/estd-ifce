class Node():
    def __init__(self, data = None, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setPrevious(self, previous):
        self.previous = previous
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasPrevious(self):
        return self.previous != None
    
    def hasNext(self):
        return self.next != None
