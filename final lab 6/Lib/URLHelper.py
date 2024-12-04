import sys


class URLHelper:

    URIValue = ""

    def __init__(self, currentRLFolderFileName) -> None:
        self.URIValue = ""
        self.ServerURLPath = currentRLFolderFileName
   
    def readserverURLFile(self):
        try:
            # Open function to open the file
            # (same directory) in append mode and
            URLfile1 = open(self.ServerURLPath,"r+")
           

            for line in URLfile1:
                # Print each line
                self.URIValue = line.strip()
                print(self.URIValue)

            #self.URIValue = URLfile1.readline(1)
            print(f"Server URI Value is : {self.URIValue}")
            URLfile1.close()
            return self.URIValue
        except Exception as error:
            print(f"Error occured in the URLHelper. readserverURLFie() with error : {error}")

    def writeServerURLFile(self, URLValue):
        try:
            # store its reference in the variable file1
            # and "MyFile2.txt" in D:\Text in file2
            self.URIValue = URLValue
            URLfile2 = open(self.ServerURLPath,"w+")
            URLfile2.writelines(URLValue) 
            URLfile2.close() 
            print(f"Server URI Value is : {self.URIValue} into the File : {self.ServerURLPath} ") 
        except Exception as error:
            print(f"Error occured in the URLHelper. WriteserverURLFie() with error : {error}")