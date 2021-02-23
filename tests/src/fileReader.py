import csv
import os

class FileReader:

    def __init__(self):
        self.fileByLines = []
        self.file = None
        self.filePath = None

    def openFile(self, filePath):
        self.filePath = filePath
        print("Loading: " + self.filePath)
        self.file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, self.filePath), 'r')
        for line in csv.reader(self.file, delimiter=','):
            self.fileByLines.append(line)
        return self.fileByLines

    def closeFile(self):
        print("Closing: "+self.filePath)
        self.file.close()
